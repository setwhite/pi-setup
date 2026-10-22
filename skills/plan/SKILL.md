---
name: plan
disable-model-invocation: true
description: 需求对齐：调研、追问到共识，派发 spec 与 ADR。
---

# 需求对齐

只管共识。结构交 `/skill:arch`，任务拆分交 `/skill:slice`，规格交 `/skill:docs-spec`。

## 原则

- design-only：只产出文档，不写实现代码。
- 需求具体就往下走；不具体先问，不猜。多轮追问，单轮聚合同类前提。
- 术语当场定：出现含糊词或与 `docs/GLOSSARY.md` 冲突时调 `/skill:docs-glossary`。

## Step 1 — 调研

只在选型未定、或结论依赖外部事实时搜。github 项目聚焦：核心痛点、架构与依赖、活跃度、取舍、open issues。

- 只认 primary source：官方文档、源码、规范、一手 API，每条结论追到拥有它的源头，二手转述不算。
- 每条声明后面跟来源：链接，或 `路径:行号`。
- 结论、依据、未决问题三段，落盘 `docs/research/主题.md`；之后只引路径，不复述。

完成标准：每个结论附可验证链接；不该搜的时候没有搜。

## Step 2 — 追问到共识

涵盖：目标与用户、MVP 范围、不做项、技术约束、验收标准、外部依赖。

完成标准：需求无歧义，或用户明确表示无需追问。

## Step 3 — 派发

- 每个功能一份 spec，交 `/skill:docs-spec` 落盘——手打，plan 不代写。
- 难以逆转的选型调 `/skill:docs-adr`。
- 结构会变（新模块、依赖方向变化、新 seam）→ 提示跑 `/skill:arch`；不变直接 `/skill:slice`。

完成标准：spec 齐备；够门槛的决策有 ADR，其余明确不建；下一步跑哪个 skill 已点名。
