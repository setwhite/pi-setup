---
name: audit
disable-model-invocation: true
description: 独立审计：逐条核对 acceptance criteria 与代码质量（含 ruff 与 basedpyright），仅给意见不改文件。
---

# 审计流程

**audit independence**：必须在未参与编写的新会话中运行（segregation of duties）。
**read-only**：严禁修改 `docs/TODO.md` 或任何仓库文件（non-interference）。

## Step 1 — 准备材料

1. 读取 `docs/TODO.md` 确认 acceptance criteria 与证据指针。
2. 检查 Git 状态：用 `git status` 与 `git diff` 确认改动范围（change scope）。

**Completion criterion**：明确改动范围与 acceptance criteria。

## Step 2 — 深度核查

1. **验收核对（conformance check）**：逐条核对 acceptance criteria；证据仅认当前会话运行输出（first-hand evidence）。
2. **quality gate**：亲自运行 `uv run ruff check`、`uv run basedpyright` 与测试（reproducible verification）。
3. **合规对照（compliance audit）**：对照 `AGENTS.md` 逐条检查，违规项必须精准引用条款与文件位置（traceability）。

**Completion criterion**：每条 acceptance criterion 得出「达成 / 未达成 + 证据」，质量问题精确定位。

## Step 3 — 输出意见

- 格式（audit finding）：`文件位置 + 观察事实 + 依据（AGENTS.md 条款或 acceptance criterion）`。
- 只报 findings，不打分、不定性、不提供实现方案（non-prescriptive review），是否返工由用户裁决（finding disposition；状态仅在用户确认勾选时更改）。

**Completion criterion**：意见精确定位到文件，未做任何文件修改。
