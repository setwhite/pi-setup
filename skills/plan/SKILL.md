---
name: plan
disable-model-invocation: true
description: 统一前置规划：按复杂度推进澄清与 ADR、架构与测试边界、规格与验收、任务拆解。
---

# 前置规划

按复杂度跳步：单模块功能从「Spec」开始；架构不变跳过「架构与 Seam」。文档归属见 `../_shared/docs-rules.md`，架构规则见 `../_shared/design-rules.md`。

## 1. 澄清与 ADR

- Frontier Rounds：按决策依赖分轮提问；每轮只问当前能拍板、互不依赖的问题并给推荐方案（用户答「是」即采纳）；下游问题留下一轮。
- Ubiquitous Language：新领域术语当场按 `/skill:docs-glossary` 写入 `docs/GLOSSARY.md`。
- ADR 门槛：改动难回退、存在真实备选且后来者会追问原因时写入 `docs/adr/`；Append-Only（不写状态、不改旧档，推翻时新建一条注明取代旧档）。

```md
## 决定

## 为什么

## 代价
```

## 2. 架构与 Seam（结构变化时跑）

- Deletion Test：假设删掉该模块，复杂度跟着消失说明只是薄包装，散落到多个调用方才说明有深度。
- Real Seam：只有一种实现不强行抽接口，至少两种实现（如生产与测试替身）才建抽象边界。
- Design It Twice：核心接口拿不准时，先出 2 到 3 个不同约束的备选方案（极简入口 vs 灵活扩展），比接口简洁度和改动集中度再拍板。
- Fitness Functions：依赖方向、禁循环导入与禁跨模块引用，写成 `import-linter`、`dependency-cruiser` 或架构单测。
- Testing Seam：测试唯一能碰的公开边界，越少越好，取覆盖本轮行为的最高层；先交用户确认再写 `docs/ARCHITECTURE.md`；每份 spec 必须有归属模块。

## 3. Spec

写入 `docs/specs/`；有待定项另加「未决」每行一条，解决即删：

```md
## 问题

## 契约

## 验收

## 不做的
```

- Contract：只写散文说不清的结构（状态机、schema、类型、API、失败路径），不抄代码；前置原型跑出精确类型或状态机时只摘核心片段。
  - Parse, Don't Validate：系统入口解析为强类型，内部直接信任类型。
  - Make Illegal States Unrepresentable：用枚举、联合类型或显式状态机表达领域状态，不用布尔标志拼接。
- Non-Goals：「不做的」是正式边界，扩范围先改此节。
- Falsifiable AC：从 `AC1` 连续编号，每条只依赖单个 todo，写清目标边界、可执行命令或精确输入输出及失败判据；新功能起点须失败，纯重构全程保持通过。

## 4. Todo 拆解

一次只拆当前阶段，写入 `docs/todos/`。

- Tracer Bullet：端到端垂直切片，单次会话做完并独立验证。
- Expand-Contract：全仓改名或改共享类型等大范围重构不硬塞切片，拆为「新旧并存 → 分批迁移保持全绿 → 删旧」。
- Prefactoring：动功能前先评估前置重构；上轮 `/skill:audit` 质量建议可单拆前置重构 todo。

```md
- [ ] 未开始
- Spec: docs/specs/<spec-file>.md
- 验收: AC1、AC3

## 交付物

## 前置
无
```

拆完请用户确认，确认后提示运行 `/skill:coding`。
