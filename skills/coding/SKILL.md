---
name: coding
disable-model-invocation: true
description: 开发流程：领取 TODO 任务，TDD 测试先行，收工运行 quality gate（ruff、basedpyright、pytest）。
---

# 开发流程

Entry criteria：`docs/TODO.md` 必须存在。严格遵循 `AGENTS.md` 的 toolchain（`uv`、`ruff`、`basedpyright`）与 approval gate 规则（严禁擅自 commit/push）。

## Step 1 — 领取任务

1. 定位 `docs/TODO.md` 首个 `- [ ]` 且前置已打勾的任务。
2. **state ownership**：任务状态仅由用户在确认勾选时更改，agent 严禁自动修改。遇不明确点立即中断提问（requirements elicitation），拒绝猜测。

**Completion criterion**：任务目标与 interface contract 明确。

## Step 2 — task decomposition + TDD（Red-Green）

1. **baby steps**：每次仅限 1 步开发 + 单测。
2. **Red**：先写失败的单元测试，只针对公开接口（black-box testing）。
3. **Green**：写最少实现让测试通过（强制 `uv run pytest` 等命令，禁用 `pip`/直接 `python`）。
4. 遇到 Bug 必须先用 instrumentation（Log/Print/堆栈）取得证据（hypothesis-driven debugging），严禁 shotgun debugging；连续失败 3 次触发 circuit breaker。

**Completion criterion**：当前步骤的实现与测试全部通过。

## Step 3 — 收工交付

1. 运行 quality gate（强制命令）：
   - Lint: `uv run ruff check`
   - 类型检查: `uv run basedpyright`
   - 测试: `uv run pytest`
2. 将验收证据（测试输出/commit）的指针填入 `docs/TODO.md` 对应任务（traceability）。
3. 按 Rule of Three 实施 refactoring，更新对应模块 README。
4. **保持任务状态不变**（仅用户确认勾选时更改），挂起等待用户 review（approval gate）。

**Completion criterion**：quality gate 全绿、每条 acceptance criterion 均有证据指针（traceability），等待用户审查。
