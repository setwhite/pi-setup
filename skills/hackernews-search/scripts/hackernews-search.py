#!/usr/bin/env python3
"""Hacker News search skill script (Python stdlib only).

支持两种模式：
- 搜索模式（Algolia）：按关键词搜索 HN 帖子/评论
- Feed 模式（Firebase）：获取 top/new/best 首页帖子
"""

from __future__ import annotations

import json
import os
import sys
import time
from typing import Any, Dict, List, NoReturn
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

SEARCH_BASE = "https://hn.algolia.com/api/v1"
FIREBASE_BASE = "https://hacker-news.firebaseio.com/v0"
REQUEST_TIMEOUT_SECONDS = 10
EXCERPT_MAX_LENGTH = 300
MAX_FEED_ITEMS = 30
MAX_SEARCH_ITEMS = 30


def print_usage() -> None:
    print(
        "Usage:\n"
        "  # Search mode\n"
        "  python hackernews-search.py '{\"query\":\"rust async\",\"count\":5}'\n"
        "  python hackernews-search.py '{\"query\":\"python\",\"count\":5,\"type\":\"comment\"}'\n"
        "  # Feed mode\n"
        "  python hackernews-search.py '{\"mode\":\"top\",\"count\":10}'\n"
        "  python hackernews-search.py '{\"mode\":\"new\",\"count\":10}'\n"
        "  python hackernews-search.py '{\"mode\":\"best\",\"count\":10}'\n\n"
        "No auth or API key required.\n"
    )


def die(message: str, *, body: Any = None) -> NoReturn:
    payload: Dict[str, Any] = {"error": message, "exit_code": 1}
    if body is not None:
        payload["body"] = str(body)
    print(json.dumps(payload, ensure_ascii=False))
    raise SystemExit(1)


def parse_payload(raw: str) -> Dict[str, Any]:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        die(f"Invalid JSON payload: {exc}")
    if not isinstance(data, dict):
        die("Payload must be a JSON object")
    return data


def parse_count(payload: Dict[str, Any], max_val: int) -> int:
    raw = payload.get("count", payload.get("Count", 10))
    try:
        count = int(raw)
    except (TypeError, ValueError):
        return 10
    return max(1, min(max_val, count))


def _http_get(url: str) -> Dict[str, Any]:
    """发送 GET 请求，解析 JSON。"""
    req = Request(url, headers={"User-Agent": "hackernews-search-skill/1.0"})
    try:
        with urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        die(f"HTTP {exc.code}: {exc.reason}")
    except URLError as exc:
        die(f"HTTP request failed (network error): {exc.reason}")
    except json.JSONDecodeError:
        die("Non-JSON response from API")


# ─── Search mode (Algolia) ────────────────────────────────────────────

VALID_SEARCH_TYPES = {"story", "comment", "all"}


def _parse_search_type(payload: Dict[str, Any]) -> str:
    t = payload.get("type") or payload.get("Type") or "story"
    t = str(t).strip().lower()
    if t not in VALID_SEARCH_TYPES:
        die(f"Invalid type '{t}', must be one of {sorted(VALID_SEARCH_TYPES)}")
    return t


def _build_algolia_tags(search_type: str) -> str:
    if search_type == "story":
        return "story"
    elif search_type == "comment":
        return "comment"
    else:
        return "(story,comment)"


def _build_search_item(hit: Dict[str, Any], search_type: str) -> Dict[str, Any]:
    is_story = search_type in ("story", "all") and bool(hit.get("title"))
    item: Dict[str, Any] = {
        "url": hit.get("url"),
        "hn_url": f"https://news.ycombinator.com/item?id={hit['objectID']}",
    }

    if is_story:
        item["title"] = hit.get("title", "")
        item["type"] = "story"
        item["points"] = hit.get("points", 0)
        item["num_comments"] = hit.get("num_comments", 0)
        # story_text 是 Show HN / Ask HN 的正文
        story_text = hit.get("story_text")
        if story_text:
            item["excerpt"] = _truncate(_strip_html(story_text))
    else:
        item["type"] = "comment"
        # 评论用所属帖子标题作为 title
        story_title = hit.get("story_title") or ""
        item["title"] = f"[评论] {story_title}" if story_title else "[评论]"
        item["story_title"] = story_title
        item["story_url"] = hit.get("story_url")
        comment_text = hit.get("comment_text") or ""
        if comment_text:
            item["excerpt"] = _truncate(_strip_html(comment_text))

    item["author"] = hit.get("author", "")
    item["created_at"] = hit.get("created_at", "")
    return item


def search_hn(query: str, count: int, search_type: str) -> Dict[str, Any]:
    tags = _build_algolia_tags(search_type)
    params = {
        "query": query,
        "tags": tags,
        "hitsPerPage": str(count),
    }
    url = f"{SEARCH_BASE}/search?{urlencode(params)}"
    data = _http_get(url)

    items = [_build_search_item(hit, search_type) for hit in data.get("hits", [])]
    return {
        "item_count": len(items),
        "items": items,
        "total_hits": data.get("nbHits", 0),
        "page": data.get("page", 0),
    }


# ─── Feed mode (Firebase) ────────────────────────────────────────────

VALID_FEEDS = {"top", "new", "best"}


def _parse_feed_mode(payload: Dict[str, Any]) -> str:
    mode = payload.get("mode") or payload.get("Mode") or ""
    mode = str(mode).strip().lower()
    if mode not in VALID_FEEDS:
        die(f"Invalid mode '{mode}', must be one of {sorted(VALID_FEEDS)}")
    return mode


def _fetch_item(item_id: int) -> Dict[str, Any]:
    url = f"{FIREBASE_BASE}/item/{item_id}.json"
    return _http_get(url)


def _build_feed_item(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "title": item.get("title", ""),
        "url": item.get("url"),
        "hn_url": f"https://news.ycombinator.com/item?id={item['id']}",
        "points": item.get("score", 0),
        "num_comments": item.get("descendants", 0),
        "author": item.get("by", ""),
        "type": item.get("type", "story"),
    }


def feed_hn(mode: str, count: int) -> Dict[str, Any]:
    # 1) 拿 ID 列表
    url = f"{FIREBASE_BASE}/{mode}stories.json"
    ids = _http_get(url)

    if not isinstance(ids, list):
        die(f"Unexpected response from Firebase: expected list, got {type(ids).__name__}")

    # 2) 逐个取详情
    items: List[Dict[str, Any]] = []
    for item_id in ids[:count]:
        item = _fetch_item(item_id)
        # 只保留 story 类型，跳过 job/poll
        if item and item.get("type") == "story":
            items.append(_build_feed_item(item))

    return {
        "item_count": len(items),
        "items": items,
        "feed": mode,
    }


# ─── Helpers ──────────────────────────────────────────────────────────

def _strip_html(text: str) -> str:
    """移除 HTML 标签并解码实体（&amp; &#x27; 等）。"""
    import html as _html
    import re
    text = re.sub(r"<[^>]+>", " ", text)
    text = _html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def _truncate(text: str) -> str:
    if len(text) <= EXCERPT_MAX_LENGTH:
        return text
    return text[:EXCERPT_MAX_LENGTH] + "…"


# ─── Main ─────────────────────────────────────────────────────────────

def main() -> None:
    if len(sys.argv) >= 2 and sys.argv[1] in {"-h", "--help"}:
        print_usage()
        raise SystemExit(0)

    if len(sys.argv) < 2:
        print_usage()
        die("Missing JSON payload argument")

    payload = parse_payload(sys.argv[1])

    # 判断模式
    mode = (payload.get("mode") or payload.get("Mode") or "").strip().lower()
    query = (payload.get("query") or payload.get("Query") or "").strip()

    if mode:
        # Feed 模式
        feed_mode = _parse_feed_mode(payload)
        count = parse_count(payload, MAX_FEED_ITEMS)
        result = feed_hn(feed_mode, count)
    elif query:
        # 搜索模式
        count = parse_count(payload, MAX_SEARCH_ITEMS)
        search_type = _parse_search_type(payload)
        result = search_hn(query, count, search_type)
    else:
        die("query or mode is required")

    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
