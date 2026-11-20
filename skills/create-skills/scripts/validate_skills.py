"""Skill 结构与风格自动校验脚本（零第三方依赖）。

检查项：
1. YAML frontmatter 必填字段（name、description）。
2. disable-model-invocation 与 description 触发词是否一致。
3. 相对文件引用（../_shared/、references/、scripts/）与 /skill:<name> 是否有效。
4. 单个 SKILL.md 是否超过 200 行。
5. AGENTS.md（若同级存在）是否误引用 skill。
6. 正文是否误用 Markdown 强调或表格。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

MAX_LINES = 200


def strip_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`]+`", "", text)


def validate(skills_root: Path) -> int:
    errors: list[str] = []
    warnings: list[str] = []

    skill_files = sorted(skills_root.glob("*/SKILL.md"))
    if not skill_files:
        print(f"未在 {skills_root} 下找到任何 */SKILL.md")
        return 1

    skill_names = {sf.parent.name for sf in skill_files}

    # Check sibling AGENTS.md if present
    agents_md = skills_root.parent / "AGENTS.md"
    if agents_md.is_file():
        agents_text = agents_md.read_text(encoding="utf-8")
        if "/skill:" in agents_text:
            errors.append("AGENTS.md 不应引用 /skill:*（保持与手动 skill 解耦）")

    all_md = list(skills_root.rglob("*.md"))
    if agents_md.is_file():
        all_md.append(agents_md)

    for md in sorted(all_md):
        rel = md.relative_to(skills_root.parent)
        raw = md.read_text(encoding="utf-8")
        no_code = strip_code(raw)
        if "**" in no_code or "__" in no_code:
            errors.append(f"[style] {rel} 包含加粗强调（** 或 __）")
        if re.search(r"(?<!\*)\*(?!\s|\*)[^*\n]+(?<!\s)\*(?!\*)", no_code):
            errors.append(f"[style] {rel} 包含斜体强调（*...*）")
        if re.search(r"(?<![A-Za-z0-9_])_(?!\s)[^_\n]+(?<!\s)_(?![A-Za-z0-9_])", no_code):
            errors.append(f"[style] {rel} 包含斜体强调（_..._）")
        if re.search(r"^\s*\|", raw, re.M):
            errors.append(f"[style] {rel} 包含 Markdown 表格")

    for sf in skill_files:
        rel = sf.relative_to(skills_root.parent)
        text = sf.read_text(encoding="utf-8")
        lines = text.splitlines()
        if len(lines) > MAX_LINES:
            warnings.append(f"[length] {rel} 共 {len(lines)} 行，超过 {MAX_LINES} 行上限，建议拆入 references/")

        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            errors.append(f"[frontmatter] {rel} 缺少 YAML frontmatter")
            continue
        fm = m.group(1)
        is_manual = "disable-model-invocation: true" in fm
        desc_m = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not desc_m:
            errors.append(f"[frontmatter] {rel} 缺少 description")
            continue
        desc = desc_m.group(1)
        if is_manual and "当" in desc and "时使用" in desc:
            errors.append(f"[trigger] {rel} 为人工触发 skill，description 不应含触发词")
        if not is_manual and "时使用" not in desc:
            errors.append(f"[trigger] {rel} 为自动触发 skill，description 缺少「…时使用」")

        for ref in re.findall(r"`(\.\./_shared/[^`]+|references/[^`]+|scripts/[^`]+)`", text):
            if not (sf.parent / ref).resolve().exists():
                errors.append(f"[ref] {rel} 引用不存在的路径：{ref}")
        for sk in re.findall(r"/skill:([a-z0-9-]+)", text):
            if sk not in skill_names:
                errors.append(f"[ref] {rel} 引用不存在的 skill：/skill:{sk}")

    if warnings:
        print(f"警告（{len(warnings)}）：")
        for w in warnings:
            print(f"  - {w}")
    if errors:
        print(f"错误（{len(errors)}）：")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"校验通过：共 {len(skill_files)} 个 skill，零错误。")
    return 0


if __name__ == "__main__":
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd() / "skills"
    raise SystemExit(validate(target))
