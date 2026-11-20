---
name: audit
disable-model-invocation: true
description: 在独立上下文中审计待审 todo：实测判定 AC，只读记录质量线索。
---

# 独立审计

交子代理隔离执行；传入 todo 路径（读绑定的 spec 与 AC）与改动范围。
Read-Only：不改代码与 `docs/todos/`，只写 `docs/audit/` 报告。

## 判定 AC

- No Trust Without Execution：逐条实跑对应命令或测试，文档或转述不算证据。
- 三态判定：达成、未达成（附命令、期望与实际）、无法判定（无可执行检查或与 AC 脱节）。
- Scope：只判已有 AC，不新增，不评 spec 完整性。

## 质量线索

跳过 QA 工具已覆盖项；每条写 `文件:行号 — 观察 — 依据`。
依据取 `AGENTS.md`、`docs-rules.md`、架构边界/状态隐患，或重点关注以下 Fowler Smell：
Duplicated Code、Speculative Generality、Mysterious Name、Primitive Obsession、Data Clumps、Shotgun Surgery、Divergent Change、Middle Man。
质量线索不影响验收结论，留给 `/skill:plan` 拆 prefactor。

## 报告骨架

```md
结论：可交付 / 回 coding / 回 spec

## 验收

- AC1 达成 — <实跑命令>
- AC2 未达成 — <实跑命令>：期望 <X>，实际 <Y>

## 质量

- <文件:行号> — <观察> — <依据>
```

同时存在未达成与无法判定记回 coding；写完提示下一步：`/skill:docs-commit`、`/skill:coding` 或 `/skill:plan`。
