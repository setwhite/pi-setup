---
name: coding
disable-model-invocation: true
description: 开发流程：领取 TODO 任务，TDD，跑 QA。
---

# 开发流程

前提：`docs/TODO.md` 存在。

## Step 1 — 领取任务

1. 取首个 `- [ ]` 且前置已勾选的任务。指定 ID 时，前置未勾选则停止并报告。
2. 若该任务的「验收证据指针」非空，即为待审：停止并报告。
3. 任务状态修改（`[ ]` ↔ `[x]`），必须用户批准。

完成标准：任务目标、接口契约明确。

## Step 2 — 红绿TDD

1. 用 todo 工具，每次只做 1 步开发 + 单测。
2. Red：针对公开接口写失败的单元测试。
3. Green：写最少实现，使测试通过。
4. Refactor：测试全绿，改进代码。

完成标准：步骤实现与测试都通过

## Step 3 — 收工交付

1. 运行 QA：Lint + Type Check + 回归Test
2. `docs/TODO.md`填入对应任务的验收证据指针
3. 若模块的用法或取舍有变，更新模块 README。
4. 提醒用户 audit
5. 获得 audit 意见后修改，并询问用户是否提交

完成标准：QA 全绿、验收证据指针都有。
