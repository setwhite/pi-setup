---
name: coding
disable-model-invocation: true
description: 开发流程：领取 docs/todos/ 任务，TDD，运行 QA。
---

# 开发流程

前提：`docs/todos/` 里有未完成的任务。

## Step 1 — 结算与领取

1. 结算 `[~]` 任务（查法见 `../_shared/docs-rules.md`）。按 `docs/audit/` 里该任务最新报告处理：
   - `pass` 且覆盖每条 AC → 告知用户。用户批准后改 `[x]`，再调 `/skill:docs-commit`。
   - `re-coding` → 本次只修报告里失败的 AC。回 Step 2。不领新任务。
   - `re-plan` → 本次不写代码。停止并提示用户运行 `/skill:plan`。
   - 没有报告 → 停止。提示先运行 `/skill:audit`。
   - `## 质量` 的 finding 不阻塞 `[x]`。要处理就另开任务，或下一阶段经 `/skill:plan` 拆成 prefactor 任务。不要并入本次修复。
2. 取首个 `[ ]` 且前置全 `[x]` 的任务文件。用户指定 ID 时，前置未勾选就停止并告知。
3. 任务缺「验收」，或要碰的 seam 没在 `docs/ARCHITECTURE.md` 确认过：停止并提问。不猜。

**完成条件**：每个 `[~]` 都有结算结论。任务目标、接口契约、seam 明确。

## Step 2 — 红绿 TDD

测试规则见 `../_shared/testing.md`。

1. 用 todo 工具。每次只做一个切片的开发与单测：在 `docs/ARCHITECTURE.md` 列出的 seam 上做一轮 Red → Green，再下一个切片。
2. 公开入口的契约（参数、返回值、异常、边界）按 `/skill:docs-docstring` 写。

重构不在这轮循环里。任务验收通过后，重构当独立任务。

意外红（不是刚写的那条）：一眼能定位是改动打断了别的断言，就在循环里修。看两遍仍解释不通，停止并提示用户运行 `/skill:debug`。

`re-coding` 同理：第一条 Red 复现报告里失败的 AC，再改。同一 AC 连续两轮 `re-coding` 仍红，停止并问用户：转 `/skill:debug` 还是 `/skill:arch`。

**完成条件**：任务的每条 AC 都有能运行的自动化检查，且全绿。

## Step 3 — 收工交付

1. 运行 QA：Lint + Type Check + 回归 Test。最后运行一次全套测试。
2. 模块的用法或取舍有变，更新 `docs/modules/<module>.md`。
3. 验收证据是本次会话运行过的命令与输出。不写入文件。`/skill:audit` 在新会话现场重新运行。
4. 把任务文件的复选框改成 `[~] 待审`。提示用户在新会话运行 `/skill:audit`。

本会话只到 `[~]`。pass 后的 `[x]` 与 `/skill:docs-commit` 在下次 coding 会话 Step 1 处理。

**完成条件**：QA 全绿，每条 AC 有能重新运行的检查，任务状态为待审。
