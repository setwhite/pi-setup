---
name: plan
disable-model-invocation: true
description: 调研、追问、plan、todo
---

# Plan

产出 `PLAN.md`（决策）、`docs/ARCHITECTURE.md`（模块地图）、`docs/TODO.md`（任务队列），不动代码。

## Step 1 — 联网调研

根据需求，联网调研方案，分析:

- 解决了什么问题
- 采用什么架构、依赖哪些技术
- 目前是否活跃（最近提交 / 发布 / 社区讨论）
- 哪些设计值得复用，哪些要避开

**完成标准**：结论要附来源链接。

## Step 2 — 追问至共识

根据调研追问用户，确认技术选项、系统架构、MVP 范围、开发顺序；能查代码库的不问用户。

**完成标准**：用户确认达成共识。

## Step 3 — 写 PLAN.md

当前工作目录写 `PLAN.md`，含调研结论、技术选型、系统架构、MVP 范围。系统架构按业务模块划分，不按技术分层。

写入后停下，请用户 review；按反馈改到批准为止。

**完成标准**：PLAN.md 已写入并获用户批准。

## Step 4 — 写 ARCHITECTURE.md

写 `docs/ARCHITECTURE.md`：模块清单（每条链到模块 README）与模块间依赖方向。入口与契约归模块 README。

**完成标准**：docs/ARCHITECTURE.md 已写入。

## Step 5 — 写 TODO.md

写 `docs/TODO.md`，把 PLAN.md 拆成按开发顺序排列的任务，每条含交付物、验收标准、状态（初始为未开始）；不写实现细节。

新模块的交付物含 README.md、公共入口、类型与契约、测试。

**完成标准**：每条任务有交付物与验收标准，状态为未开始。
