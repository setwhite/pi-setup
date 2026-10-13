---
name: plan
disable-model-invocation: true
description: 需求对齐与规划，产出 PLAN、ARCHITECTURE、TODO 三份文档，每份获批后进入下一份。
---

# 规划流程

用法：`/skill:plan <需求描述>`。

## 原则

- **design-only**：只产出文档，不写实现代码，不建源码目录。
- **package by feature**：按功能（feature）组织包，不按层（layer）组织。
- **single source of truth**：每条事实只存一处。决策与理由存 PLAN；签名、异常、字段以代码 docstring 为准；模块 README 只写用法与取舍。
- **progressive summarization**：阶段全部 `[x]` 后，由用户要求压缩为一行并附指针。

| 文档 | 职责 |
| --- | --- |
| `docs/PLAN.md` | 目标、决策（decision log）、不做项、阶段划分（标注 MVP） |
| `docs/ARCHITECTURE.md` | 模块表（名 + 职责）、依赖方向（无循环）、代码放置、模块 README 位置、测试约定 |
| `docs/TODO.md` | 原子任务清单，含验收标准（AC）与证据指针 |
| 模块 README | 用法与取舍 |

## Step 1 — 需求对齐

- 需求具体则直接进入 Step 2。不具体则先提问，不猜测。提问覆盖：目标与用户、MVP 范围、不做项、技术约束、验收标准、外部依赖。
- 用 `ask_user_question` 提问：单次 ≤4 题，每题 2–4 个选项，推荐项置顶并标注 `(Recommended)`。

**完成标准**：需求无歧义，或用户明确表示无需追问。

## Step 2 — 调研

- 用 `web_search`、`web_fetch` 查一手来源：官方文档、源码、Release Notes。本地参考代码用 `rg`、`fd`。
- GitHub 项目用 `gh` 查最近 push、最近 release、open issues 数量，量化活跃度。

**完成标准**：每个结论附可验证链接。

## Step 3 — 写 PLAN.md

- 决策用表格：`决策 | 一句话理由 | 出处`。仅有取舍争议的决策展开段落。
- 必须包含不做项与阶段划分（标注 MVP）。
- 选型提问的推荐项，依据 Step 2 的调研结果给出。

**完成标准**：用户批准（approval gate）。

## Step 4 — 写 ARCHITECTURE.md

- 声明模块表、依赖方向、代码放置规则、模块 README 位置、测试约定。
- Coverage check：PLAN 的每个 MVP 都有模块承接。

**完成标准**：用户批准。

## Step 5 — 写 TODO.md

- 按开发顺序，把 PLAN 的阶段拆为原子任务（单次会话可完成）。
- 格式：

  ```markdown
  - [ ] T1 任务标题
    - 交付物：…
    - 验收：
      - AC1 …
      - AC2 …
    - 验收证据：
    - 前置：无（或填 T0）
  ```

- 「验收证据」保持留空，由 coding 填写：每条 AC 对应 `测试文件::用例` 与执行命令，另列改动文件。

**完成标准**：用户批准。TODO 获批后才能进入 coding。
