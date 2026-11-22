---
name: audit
disable-model-invocation: true
description: 在独立上下文中验收待审 todo 或对抗审查 diff：实跑判定验收标准、验证安全前提，只读记录质量建议。
---

# 独立验收与对抗审查

交子代理隔离执行：有 todo 时传入 todo 路径（读绑定 spec 与 AC）和改动范围，报告写入 `docs/audit/`；无 todo 时审查当前分支 diff 与工作区改动，直接输出报告不落盘。
Read-Only：不改仓库源码与 `docs/todos/`；需要写临时验证脚本时放项目内 `.tmp/`，跑完清理不留残留。

## 1. 判定验收标准（有 todo 时）

- Execute Every AC：逐条实跑对应命令或测试，文档和转述不算证据。
- 三态结论：通过、未通过（附命令、期望与实际）、无法判定（缺可执行检查或与标准脱节）。
- Scope & Creep：只判已有 AC，不新增要求，不评 spec 优劣；diff 出现超出规格或越过「不做的」边界的改动时，单列范围蔓延。

## 2. 对抗复现与爆炸半径

- Prove or Drop：主动尝试打崩改动；只保留能用命令、测试或 `.tmp/` 脚本实跑复现的缺陷，未运行证明的风险一律丢弃（风格与结构问题归入质量建议）。
- One Safety Fact：改动涉及调用方、第三方库边界、协议格式或生命周期时序时，找出安全依赖的 1 个核心事实并实跑证明；无法证明的标为 `unproven`。

## 3. 质量建议

跳过 QA 已覆盖项，每条写 `文件:行号 — 观察 — 依据`（仅供 `/skill:plan` 拆前置重构，不影响验收结论）。
- Repo Overrides Baseline：项目规范明确允许的写法不报问题；代码坏味道一律标为建议而非硬错。
- 关注依据：`AGENTS.md`、`../_shared/design-rules.md`、`../_shared/docs-rules.md`、架构边界或状态隐患，以及以下 Fowler Code Smell：
  Duplicated Code、Speculative Generality、Mysterious Name、Primitive Obsession、Data Clumps、Feature Envy、Repeated Switches、Shotgun Surgery、Divergent Change、Middle Man。

## 报告骨架

```md
结论：通过 / 退回开发 / 退回规划

## 验收

- AC1 通过 — <实跑命令>
- AC2 未通过 — <实跑命令>：期望 <X>，实际 <Y>
- 范围蔓延（如有）— <文件:行号>：<超出规格的额外改动>

## 实跑缺陷与安全前提

- 缺陷（如有）— <复现命令>：<实际输出与违背预期之处>
- 安全前提（如有）— <核心事实>：<已实跑证明命令 / unproven>

## 质量建议

- <文件:行号> — <观察> — <依据>
```

无 todo 时省略「验收」节，结论用「通过 / 存在实跑缺陷」；有 todo 时只要有 AC 未通过或存在实跑缺陷，结论记「退回开发」并提示下一步：`/skill:docs-commit`、`/skill:coding` 或 `/skill:plan`。
