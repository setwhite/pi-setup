"""项目文档机械巡检脚本（零第三方依赖）。

只做确定性高的文档结构检查（TODO 扫描交给 rg）：
1. Markdown 相对路径断链检查。
2. 重复一级标题（AGENTS.md 除外）与跳级标题检查。
3. docs/ 子目录内残留的手动 README.md 索引提醒。
4. docs/todos/ 是否缺少 Spec 路径绑定。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)")


def strip_fenced_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def check_markdown(md_file: Path, root: Path, issues: list[str]) -> None:
    rel = md_file.relative_to(root)
    raw = md_file.read_text(encoding="utf-8", errors="replace")
    clean = strip_fenced_code(raw)

    h1_count = 0
    prev_level = 0
    for lineno, line in enumerate(clean.splitlines(), 1):
        m = re.match(r"^(#{1,6})\s+", line)
        if not m:
            continue
        level = len(m.group(1))
        if level == 1:
            h1_count += 1
        if prev_level and level > prev_level + 1:
            issues.append(f"[heading] {rel}:{lineno} 跳级标题 H{prev_level} -> H{level}")
        prev_level = level
    if h1_count > 1 and md_file.name != "AGENTS.md":
        issues.append(f"[heading] {rel} 存在 {h1_count} 个一级标题")

    for target in LINK_RE.findall(clean):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (md_file.parent / target).resolve().exists():
            issues.append(f"[link] {rel} 断链 -> {target}")


def check_docs(root: Path) -> int:
    issues: list[str] = []
    docs_dir = root / "docs"

    for md in sorted(root.glob("*.md")):
        check_markdown(md, root, issues)

    if docs_dir.is_dir():
        for md in sorted(docs_dir.rglob("*.md")):
            rel = md.relative_to(root)
            if md.name == "README.md" and md.parent != docs_dir:
                issues.append(f"[index] {rel} 无需手动维护子目录 README 索引")
            if md.parent.name == "todos":
                text = md.read_text(encoding="utf-8", errors="replace")
                if not re.search(r"Spec[:：]\s*docs/specs/", text):
                    issues.append(f"[trace] {rel} 缺少 Spec 路径绑定")
            check_markdown(md, root, issues)

    if issues:
        print(f"发现 {len(issues)} 项文档问题：")
        for i in issues:
            print(f"  - {i}")
        return 1

    print("文档结构、断链与追踪检查通过。")
    return 0


if __name__ == "__main__":
    target_root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    raise SystemExit(check_docs(target_root))
