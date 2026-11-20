---
name: plan
disable-model-invocation: true
description: 统一前置规划：按复杂度推进澄清与 ADR、架构与 seam、spec 与 AC、todo 拆解。
---

# 前置规划

按复杂度跳步：单模块功能从「Spec」起步；结构不变跳过「架构与 Seam」。
文档归属见 `../_shared/docs-rules.md`。

## 1. 澄清与 ADR

- Clarification Batch：一次问清不做项、验收边界与外部依赖，每题给候选方案；能从代码推出的不问。
- Ubiquitous Language：新术语当场按 `/skill:docs-glossary` 写入 `docs/GLOSSARY.md`。
- ADR 门槛：改动难回退（one-way door）、存在真实备选且后来者会追问原因时，写入 `docs/adr/`。
  - Append-Only：不写状态、不改旧档；推翻时新建一条注明取代旧档。

```md
## 决定

## 为什么

## 代价
```

## 2. 架构与 Seam（结构变化时跑）

- Fitness Functions：依赖方向、禁循环导入与禁 deep import 优先写成可执行检查（如 `import-linter`、`dependency-cruiser` 或架构单测），不在文档手写依赖清单。
- Testing Seam：测试唯一能碰的公开边界，数量越少越好，取覆盖本轮行为的最高层；先交用户确认清单再写入 `docs/ARCHITECTURE.md`；每份 spec 必须有承接模块。

## 3. Spec

写入 `docs/specs/`；有未决项时另加「未决」每行一条，解决即删：

```md
## 问题

## 契约

## 验收

## 不做的
```

- Contract：写散文说不清的形状（状态机、schema、类型、API、失败路径），不抄代码。
  - Parse, Don't Validate：在系统入口解析为强类型，内部直接信任类型。
  - Make Illegal States Unrepresentable：用枚举、联合类型或显式状态机表达领域状态，不用布尔标志拼接。
- Non-Goals：「不做的」是正式契约，扩范围先改此节。
- Falsifiable AC：
  - 从 `AC1` 连续编号，每条只依赖单个 todo，可独立判定。
  - 写清目标 seam、可执行命令或精确输入输出、失败判据。
  - 新增行为起点为红；纯重构全程保持绿。

## 4. Todo 拆解

一次只拆当前阶段，写入 `docs/todos/`。

- Tracer Bullet：端到端垂直切片，单次会话做完并可独立验证。
- Prefactoring：动功能前先评估前置重构；上轮 `/skill:audit` 质量线索可单拆 prefactor todo。

```md
- [ ] 未开始
- Spec: docs/specs/<spec-file>.md
- 验收: AC1、AC3

## 交付物

## 前置
无
```

拆完请用户确认；确认后提示运行 `/skill:coding`。
