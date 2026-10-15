---
name: plan
disable-model-invocation: true
description: 需求对齐、调研、PLAN、ARCHITECTURE、TODO
---

# 规划流程

## 原则

- design-only：只产出文档，不写实现代码。
- package by feature：按功能（feature）组织，不按层（layer）组织。
- single source of truth：决策与理由存 PLAN；签名、异常、字段以代码 docstring 为准；模块 README 只写用法与取舍。

## Step 1 — 调研

- 联网搜索一手来源：官方文档、源码、Release Notes。
- github项目聚焦：核心痛点、架构与依赖、活跃度、取舍、open issues。

完成标准：每个结论附可验证链接，收敛到影响选型的关键问题。

## Step 2 — 追问到共识

- 需求具体则直接进入 Step 3。
- 不具体则先提问，不猜测。
- 就方方面面进行多轮追问，单轮聚合同类前提。
- 涵盖：目标与用户、MVP 范围、不做项、技术约束、验收标准、外部依赖。

完成标准：需求无歧义，或用户明确表示无需追问。

## Step 3 — 写 `docs/PLAN.md`

- 决策用表格：`决策 | 一句话理由 | 出处指针`。仅有取舍争议的决策展开段落。
- 包含为什么做、技术选型、不做项、阶段划分（标注 MVP）。

完成标准：用户批准。

## Step 4 — 写 `docs/ARCHITECTURE.md`和模块 README

- 声明模块表、依赖方向、代码放置规则、模块 README 位置、测试约定。
- Coverage check：PLAN 的 MVP 都有模块承接。
- 模块 README 写内部契约（签名, 异常, 字段）、用法与取舍

完成标准：用户批准。

## Step 5 — 写 `docs/TODO.md`

- 按开发顺序，把 PLAN 的阶段拆为原子任务（单次会话可完成）。
- 格式：

  ```markdown
  - [ ] T1 任务标题
    - 交付物：…
    - 验收：
      - AC1 …
      - AC2 …
    - 验收证据指针：
      - AC1 …
      - AC2 …
    - 前置：无（或填 T0）
  ```

- 「验收证据指针」保持留空，由 coding 填写

完成标准：用户批准。
