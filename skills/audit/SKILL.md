---
name: audit
disable-model-invocation: true
description: 在独立上下文中验收待审 todo：实测判定验收标准，只读记录质量建议。
---

# 独立验收

交子代理隔离执行，传入 todo 路径（读绑定的 spec 与 AC）和改动范围。
Read-Only：不改代码与 `docs/todos/`，只写 `docs/audit/` 报告。

## 判定验收标准

- Execute Every AC：逐条实跑对应命令或测试，文档和转述不算证据。
- 三态结论：通过、未通过（附命令、期望与实际）、无法判定（缺可执行检查或与标准脱节）。
- Scope & Creep：只判已有 AC，不新增要求，不评 spec 优劣；diff 出现超出规格或越过「不做的」边界的改动时，单列范围蔓延。

## 质量建议

跳过 QA 已覆盖项，每条写 `文件:行号 — 观察 — 依据`（仅供 `/skill:plan` 拆前置重构，不影响验收结论）。
- Repo Overrides Baseline：项目规范明确允许的写法不报问题；代码坏味道一律标为建议而非硬错。
- 关注依据：`AGENTS.md`、`docs-rules.md`、架构边界或状态隐患，以及以下 Fowler Code Smell：
  Duplicated Code、Speculative Generality、Mysterious Name、Primitive Obsession、Data Clumps、Feature Envy、Repeated Switches、Shotgun Surgery、Divergent Change、Middle Man。

## 报告骨架

```md
结论：通过 / 退回开发 / 退回规划

## 验收

- AC1 通过 — <实跑命令>
- AC2 未通过 — <实跑命令>：期望 <X>，实际 <Y>
- 范围蔓延（如有）— <文件:行号>：<超出规格的额外改动>

## 质量建议

- <文件:行号> — <观察> — <依据>
```

只要有未通过项（即使同时存在无法判定），结论记「退回开发」；写完提示下一步：`/skill:docs-commit`、`/skill:coding` 或 `/skill:plan`。
