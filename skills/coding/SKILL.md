---
name: coding
disable-model-invocation: true
description: 开发流程：领取 TODO 任务，TDD，跑 QA。
---

# 开发流程

前提：`docs/TODO.md` 存在。

## Step 1 — 领取任务

1. 取首个 `[ ]` 且前置全部 `[x]` 的任务；指定 ID 时前置未勾选就停下报告。
2. 任务缺「验收」，或要碰的接缝没在 `docs/ARCHITECTURE.md` 里确认过：停下问，不猜。
3. 改任务状态要用户批准。

完成标准：任务目标、接口契约、接缝明确。

## Step 2 — 红绿 TDD

测试规则见 `../_shared/testing.md`。

1. 用 todo 工具，每次只做 1 步开发 + 单测：在确认过的接缝上做一轮 Red → Green，再做下一个切片。
2. 公开入口的契约（参数、返回值、异常、边界）调 `/skill:docs-docstring` 写。

重构不在这轮循环里：`/skill:audit` 新会话之后当独立任务。

意外红（不是刚写的那条）：一眼能定位是改动打断了别的断言，就在循环里修；看两遍仍解释不通就停下，让用户跑 `/skill:debug`，别在循环里试。

完成标准：任务的每条 AC 都有能跑的自动化检查，且全绿。

## Step 3 — 收工交付

1. 跑 QA：Lint + Type Check + 回归 Test，最后跑一次全套测试。
2. 模块的用法或取舍有变，就更新模块 README。
3. 验收证据是本次会话跑过的命令与输出，不写进文件；`/skill:audit` 在新会话现场重跑。
4. 状态改 `[~]`，提醒用户在新会话跑 `/skill:audit`。
5. `/skill:audit` 的意见修完后，调 `/skill:docs-commit` 写提交信息，等用户确认。

完成标准：QA 全绿，每条 AC 有可复跑的检查，任务状态为待审。
