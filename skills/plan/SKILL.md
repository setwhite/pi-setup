---
name: plan
disable-model-invocation: true
description: 需求对齐、调研、规格、ARCHITECTURE、TODO
---

# 规划流程

plan 管一次项目或一个阶段，产出 `docs/ARCHITECTURE.md`、`docs/TODO.md`；规格、调研、决策分别在 `docs/specs/`（`/skill:docs-spec` 落盘）、`docs/research/`、`docs/adr/`，只引用路径，不复述内容。

## 原则

- design-only：只产出文档，不写实现代码。
- package by feature：按功能组织，不按层。
- 决策分三档：难以逆转有真实取舍 → `docs/adr/`；只影响一个模块 → 那个模块的 README；读代码能看出来的不写。
- 签名、异常、字段以代码 docstring 为准，模块 README 只写用法与取舍。

## Step 1 — 调研

- 走 `/skill:docs-research` 的规矩（一手来源、逐条引用），结论落 `docs/research/<主题>.md`。
- github 项目聚焦：核心痛点、架构与依赖、活跃度、取舍、open issues。

完成标准：每个结论附可验证链接，收敛到影响选型的关键问题。

## Step 2 — 追问到共识

- 需求具体就进 Step 3；不具体先问，不猜。多轮追问，单轮聚合同类前提。
- 涵盖：目标与用户、MVP 范围、不做项、技术约束、验收标准、外部依赖。
- 术语当场定：出现含糊词或与 `docs/GLOSSARY.md` 冲突时调 `/skill:docs-glossary`，别让乱词流进 spec。

完成标准：需求无歧义，或用户明确表示无需追问。

## Step 3 — 落规格

- 共识交给 `/skill:docs-spec` 写成 `docs/specs/NNNN-slug.md`——手打 skill，提示用户运行，plan 不代写。
- 难以逆转的选型决策调 `/skill:docs-adr` 写 `docs/adr/`。

完成标准：每个功能都有 spec；够门槛的决策都有 ADR，其余明确不建。

## Step 4 — 写 `docs/ARCHITECTURE.md` 和模块 README

- 声明模块表、依赖方向、代码放置规则、模块 README 位置。
- 测试决定三段：哪些模块被测、测试写在哪个接缝、同类测试的先例。接缝清单摊给用户确认（`../_shared/testing.md`）。
- Coverage check：spec 覆盖的功能都有模块承接。
- 模块 README 写内部契约（签名、异常、字段）、用法与取舍。

完成标准：用户批准，接缝清单已确认。

## Step 5 — 写 `docs/TODO.md`

- 按阶段分组、标注 MVP；阶段内按开发顺序拆原子任务。
- 每个任务是 tracer bullet：垂直切片，穿过要碰的每一层，做完能单独验证，单次会话能做完。
- 拆之前先看有没有 prefactor：先把改动变简单，再做简单的改动。

格式见 `references/todo-format.md`。

完成标准：用户批准。落点与 README 索引按 `../_shared/docs-rules.md`。
