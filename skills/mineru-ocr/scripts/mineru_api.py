"""MinerU 精准解析 API 调用脚本。"""

from __future__ import annotations

import argparse
import sys
import time
import zipfile
from pathlib import Path
from urllib.parse import urlsplit

import requests

BASE_URL = "https://mineru.net/api/v4"
TOKEN_PATH = Path(__file__).resolve().parent.parent / "token.txt"
MODEL_VERSION = "vlm"
POLL_INTERVAL_SECONDS = 5
POLL_TIMEOUT_SECONDS = 3600
HTTP_TIMEOUT_SECONDS = 300
RETRY_ATTEMPTS = 3


def read_token() -> str:
    """读同目录 token.txt；缺失或为空时终止并说明缺什么。"""
    try:
        token = TOKEN_PATH.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        raise SystemExit(f"缺少 token 文件：{TOKEN_PATH}") from None
    except OSError as err:
        raise SystemExit(f"读不到 token 文件 {TOKEN_PATH}：{err}") from err
    if not token:
        raise SystemExit(f"token 文件为空：{TOKEN_PATH}")
    return token


def headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def call(method: str, url: str, **kwargs: object) -> dict:
    """发送请求并返回 data 字段；429 与 5xx 重试，其余错误直接抛出。"""
    last_error = ""
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            resp = requests.request(method, url, timeout=HTTP_TIMEOUT_SECONDS, **kwargs)
        except requests.RequestException as err:
            last_error = str(err)
        else:
            if resp.status_code == 429 or resp.status_code >= 500:
                last_error = f"HTTP {resp.status_code}: {resp.text[:200]}"
            else:
                payload = resp.json()
                if payload.get("code") != 0:
                    raise RuntimeError(
                        f"接口错误 code={payload.get('code')} msg={payload.get('msg')} "
                        f"trace_id={payload.get('trace_id')}"
                    )
                return payload["data"]
        if attempt < RETRY_ATTEMPTS:
            time.sleep(POLL_INTERVAL_SECONDS * attempt)
    raise RuntimeError(f"请求失败 {method} {url}: {last_error}")


def poll(fetch) -> str:
    """轮询任务直到 done，返回 full_zip_url。"""
    deadline = time.monotonic() + POLL_TIMEOUT_SECONDS
    while True:
        data = fetch()
        state = data.get("state")
        if state == "done":
            return data["full_zip_url"]
        if state == "failed":
            raise RuntimeError(f"解析失败：{data.get('err_msg') or '未知原因'}")
        if time.monotonic() > deadline:
            raise RuntimeError(f"轮询超时（{POLL_TIMEOUT_SECONDS}s），最后状态 {state}")
        progress = data.get("extract_progress") or {}
        print(
            f"[{state}] 页 {progress.get('extracted_pages', '?')}/{progress.get('total_pages', '?')}",
            flush=True,
        )
        time.sleep(POLL_INTERVAL_SECONDS)


def parse_url(file_url: str, pages: str | None, token: str) -> str:
    payload = {"url": file_url, "model_version": MODEL_VERSION}
    if pages:
        payload["page_ranges"] = pages
    task_id = call(
        "POST", f"{BASE_URL}/extract/task", headers=headers(token), json=payload
    )["task_id"]
    print(f"task_id={task_id}", flush=True)
    return poll(
        lambda: call("GET", f"{BASE_URL}/extract/task/{task_id}", headers=headers(token))
    )


def parse_file(path: Path, pages: str | None, token: str) -> str:
    entry: dict[str, str] = {"name": path.name}
    if pages:
        entry["page_ranges"] = pages
    data = call(
        "POST",
        f"{BASE_URL}/file-urls/batch",
        headers=headers(token),
        json={"files": [entry], "model_version": MODEL_VERSION},
    )
    batch_id = data["batch_id"]
    upload_url = data["file_urls"][0]
    with path.open("rb") as fh:
        resp = requests.put(upload_url, data=fh, timeout=HTTP_TIMEOUT_SECONDS)
    if resp.status_code != 200:
        raise RuntimeError(f"上传失败 HTTP {resp.status_code}: {resp.text[:200]}")
    print(f"batch_id={batch_id} 已上传，等待解析", flush=True)

    def fetch() -> dict:
        results = call(
            "GET", f"{BASE_URL}/extract-results/batch/{batch_id}", headers=headers(token)
        )
        if not results["extract_result"]:
            raise RuntimeError("批量结果为空")
        return results["extract_result"][0]

    return poll(fetch)


def download(zip_url: str, out_dir: Path) -> None:
    resp = requests.get(zip_url, timeout=HTTP_TIMEOUT_SECONDS)
    resp.raise_for_status()
    out_dir.mkdir(parents=True, exist_ok=True)
    root = out_dir.resolve()
    archive = root / "_result.zip"
    archive.write_bytes(resp.content)
    with zipfile.ZipFile(archive) as zf:
        for name in zf.namelist():
            if not (root / name).resolve().is_relative_to(root):
                raise RuntimeError(f"压缩包路径越界：{name}")
        zf.extractall(root)
    archive.unlink()


def default_out_dir(source: str) -> Path:
    stem = Path(urlsplit(source).path if "://" in source else source).stem or "document"
    return Path("ocr-output") / stem


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="MinerU 文档解析")
    parser.add_argument("source", help="本地文件路径或 HTTP URL")
    parser.add_argument("-o", "--out", help="输出目录")
    parser.add_argument("--pages", help="页码范围，如 2,4-6")
    args = parser.parse_args(argv)

    token = read_token()
    is_url = "://" in args.source
    if is_url:
        zip_url = parse_url(args.source, args.pages, token)
    else:
        path = Path(args.source)
        if not path.is_file():
            print(f"文件不存在：{path}", file=sys.stderr)
            return 1
        zip_url = parse_file(path, args.pages, token)

    out_dir = Path(args.out) if args.out else default_out_dir(args.source)
    download(zip_url, out_dir)
    markdown = out_dir / "full.md"
    print(f"输出目录：{out_dir}")
    if not markdown.is_file():
        print(f"输出目录里没有 {markdown.name}：{markdown}", file=sys.stderr)
        return 1
    print(f"Markdown：{markdown}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
