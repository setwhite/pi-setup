---
name: plan
disable-model-invocation: true
description: requirements elicitation 与 alignment，产出 PLAN、ARCHITECTURE、TODO 三份核心文档。
---

# 规划流程

按顺序产出：`docs/PLAN.md`（decision log）、`docs/ARCHITECTURE.md`、`docs/TODO.md`（backlog）。

## 硬约束

- **design-only**
- **package by feature, not by layer**
- **single source of truth**：每条事实仅在一处维护。`PLAN` 仅保留 decisions 与一句话理由（ADR 精神），契约、字段、签名与取舍归入模块 README。
- **progressive summarization**：阶段完成后，该阶段条目压缩回一行并附带指针。

| 文档 | single responsibility |
| --- | --- |
| `docs/PLAN.md` | 为什么做、技术选型、不做项、阶段划分（decision log） |
| `docs/ARCHITECTURE.md` | 模块清单（名 + 职责）、依赖方向、目录与测试约定 |
| `docs/TODO.md` | 任务清单（`- [ ]` / `- [x]`）、acceptance criteria、验收证据指针、前置依赖 |
| 模块 README | interface contract（签名, 异常, 字段）、用法与取舍 |

---

## Step 1 — 联网调研

1. 检索一手来源（primary sources：官方文档、源码、Release Notes），用 `rg`/`fd` 或搜索工具辅助。
2. 聚焦：核心痛点、架构与依赖、活跃度、取舍。

**Completion criterion**：结论附带可验证链接，收敛至影响选型的关键问题。

## Step 2 — requirements elicitation & alignment

- 就这个计划的方方面面不断盘问用户，直到达成 alignment。
- 遇模糊需求直接截断提问，不盲目猜测。
- 每个问题提供推荐选项及理由（opinionated options），单轮聚合同类前提（batched clarification）。

**Completion criterion**：用户回复确认，达成 alignment。

## Step 3 — 编写 PLAN.md

- 每条 decision 一行：`decision | 一句话理由 | 详细出处指针`（ADR 结构）。仅分歧点展开段落。

**Completion criterion**：`docs/PLAN.md` 写入完毕并获批（approval gate）。

## Step 4 — 编写 ARCHITECTURE.md

- 声明模块表、依赖方向、代码放置规则。coverage check：`PLAN` 中 MVP 均有模块承接（traceability）。

**Completion criterion**：`docs/ARCHITECTURE.md` 写入完毕。

## Step 5 — 编写 TODO.md

- work breakdown：按开发顺序将 `PLAN` 的阶段拆分为 atomic tasks（单次会话可完成的单步任务）。
- 任务格式：
  ```markdown
  - [ ] T1 任务标题
    - 交付物：…
    - 验收：…
    - 验收证据：（测试文件 / 命令输出 / commit）
    - 前置：无
  ```
