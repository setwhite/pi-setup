---
name: coding
disable-model-invocation: true
description: 开发流程：领取 docs/todos/ 任务，TDD，跑 QA。
---

# 开发流程

前提：`docs/todos/` 里有未完成的任务。

## Step 1 — 结算与领取

1. 结算 `[~]`（`rg -l '^- \[~\]' docs/todos/`），按 `docs/audit/` 里该任务最新报告：
   - `pass` 且覆盖每条 AC → 报用户，获批后改 `[x]`，再调 `/skill:docs-commit`。
   - `re-coding` → 本次只修报告里失败的 AC，回 Step 2，不领新任务。
   - `re-slice` → 本次不写代码，停下提示用户跑 `/skill:slice`。
   - 没有报告 → 停下，提示先跑 `/skill:audit`。
   - `## 质量` 的 finding 不阻塞 `[x]`；要处理就另开任务，或下一阶段经 `/skill:slice` 拆成 prefactor 任务，不并入本次修复。
2. 取首个 `[ ]` 且前置全 `[x]` 的任务文件；指定 ID 时前置未勾选就停下报告。
3. 任务缺「验收」，或要碰的 seam 没在 `docs/ARCHITECTURE.md` 确认过：停下问，不猜。

完成标准：每个 `[~]` 都有结算结论，任务目标、接口契约、seam 明确。

## Step 2 — 红绿 TDD

测试规则见 `../_shared/testing.md`。

1. 用 todo 工具，每次只做 1 步开发 + 单测：在确认过的 seam 上做一轮 Red → Green，再下一个切片。
2. 公开入口的契约（参数、返回值、异常、边界）调 `/skill:docs-docstring` 写。

重构不在这轮循环里：任务验收通过后当独立任务。

意外红（不是刚写的那条）：一眼能定位是改动打断了别的断言，就在循环里修；看两遍仍解释不通就停下，让用户跑 `/skill:debug`。

`re-coding` 同理：第一条 Red 复现报告里失败的 AC，再改。同一 AC 连续两轮 `re-coding` 仍红，停下问用户：转 `/skill:debug` 还是 `/skill:arch`。

完成标准：任务的每条 AC 都有能跑的自动化检查，且全绿。

## Step 3 — 收工交付

1. 跑 QA：Lint + Type Check + 回归 Test，最后跑一次全套测试。
2. 模块的用法或取舍有变，更新模块 README。
3. 验收证据是本次会话跑过的命令与输出，不写进文件；`/skill:audit` 在新会话现场重跑。
4. 任务文件的复选框改成 `[~] 待审`，提醒用户在新会话跑 `/skill:audit`。

本会话只到 `[~]`；pass 后的 `[x]` 与 `/skill:docs-commit` 在下次 coding 会话 Step 1 处理。

完成标准：QA 全绿，每条 AC 有可复跑的检查，任务状态为待审。
