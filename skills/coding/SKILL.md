---
name: coding
disable-model-invocation: true
description: 开发流程：领取 TODO 任务，TDD 先行，收工跑 quality gate 并交付待审。
---

# 开发流程

用法：`/skill:coding`（自动领取）或 `/skill:coding <任务ID>`（指定任务）。

入口条件：`docs/TODO.md` 存在且已获批。遵守 AGENTS.md 的 Tooling、Confirmation、Engineering。

## Step 1 — 领取任务

1. 取首个 `- [ ]` 且前置已勾选的任务。指定 ID 时，前置未勾选则停止并报告。
2. 若该任务的「验收证据」已非空，即为待审：停止并提示用户审查。仅当用户明确要求返工时继续。
3. 无可领取任务：停止并报告。
4. 任务状态（`[ ]` ↔ `[x]`）只由用户修改，agent 不得改动。
5. 目标、AC、接口契约（模块 README 或代码 docstring）不明确，或实现需偏离 PLAN / ARCHITECTURE：立即停止，用 `ask_user_question` 提问，不猜测。

**完成标准**：目标、AC、接口契约明确。

## Step 2 — TDD 循环

任务 ≥3 步时，先用 todo 工具列出步骤，完成后清空。每轮只做 1 步开发 + 1 组单测。

1. **Red**：针对公开接口（黑盒）写单测，运行 `uv run pytest <路径>`，确认失败原因是断言，而非导入错误。
2. **Green**：写最少实现，使测试通过。
3. **Refactor**：全绿后消除重复。同一逻辑 ≥3 次才抽象；重复源于架构时，停止并走 RFC。
4. **Bug**：按 AGENTS.md「Engineering」的 Debugging 与 Circuit breaker 处理。

**完成标准**：本轮测试全绿。

## Step 3 — 收工

1. Quality gate 全部通过：`uv run ruff check`、`uv run basedpyright`、`uv run pytest`。未通过则回到 Step 2。
2. 在 `docs/TODO.md` 填写「验收证据」：每条 AC 对应 `测试文件::用例` 与执行命令；另列改动文件（用 `git status --porcelain` 核对）。
3. 若模块的用法或取舍有变，更新其 README（不复制签名）。
4. 停止，并给出下一步：

   > 下一步：`/new` 后运行 `/skill:audit <任务ID>`。审计通过后，由你勾选 `- [x] <任务ID>`，再运行 `/skill:coding` 领取下一个任务。

**完成标准**：quality gate 全绿，每条 AC 有证据，等待用户审查。
