---
name: coding
disable-model-invocation: true
description: 开发流程：领取 TODO 任务，测试先行，收工运行 ruff、basedpyright 与测试。
---

# 开发流程

前提：`docs/TODO.md` 必须存在。严格遵循 `AGENTS.md` 的**工具链约束**（`uv`、`ruff`、`basedpyright`）与**确认规则**（严禁擅自 commit/push）。

## Step 1 — 领取任务
1. 定位 `docs/TODO.md` 首个 `- [ ]` 且前置已打勾的任务。
2. **严禁自动修改任务状态**：仅在用户确认勾选时才能更改。遇不明确点立即中断提问，拒绝猜测。

**完成标准**：任务目标与接口契约明确。

## Step 2 — Todo 驱动与红绿 TDD
1. 每次执行**仅限 1 步开发 + 单测**（遵循 Todo 驱动）。
2. **Red**：编写失败的单元测试贴公开接口。
3. **Green**：编写最少实现让测试通过（强制使用 `uv run pytest` 等命令，禁用 `pip`/直接 `python`）。
4. 遇到 Bug 必须先加 Log/Print 或查堆栈，严禁「盲猜试错」；连续失败 3 次触发熔断。

**完成标准**：当前步骤的实现与测试全部通过。

## Step 3 — 收工交付
1. 运行质量检查（强制命令）：
   - Lint: `uv run ruff check`
   - 类型检查: `uv run basedpyright`
   - 测试: `uv run pytest`
2. 将验收证据（测试输出/commit）填入 `docs/TODO.md` 对应任务的验收证据指针中。
3. 按 Rule of Three 实施收口重构，更新对应模块 README。
4. **保持任务状态不变**（仅在用户确认勾选时才能更改），挂起等待用户 Review。

**完成标准**：QA 全绿、每条验收标准均有证据指针，等待用户审查。
