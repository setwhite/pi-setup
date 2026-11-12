---
name: audit
disable-model-invocation: true
description: 独立审计一个待审任务：判定 AC，质量问题只记录。
---

# 审计

交给子代理跑，别用当前会话的上下文。交给它三样：spec 路径、改动范围、要审的 AC 编号。

只读。不改代码，不改 `docs/todos/`。唯一写入是报告。

## 判 AC

- 自己跑每条 AC 对应的检查。文件里写的、别人报的不算证据。
- 每条给一个判定：达成、未达成、无法判定。无法判定是没有可运行的检查，或检查与 AC 说的不是一件事。
- 只判已有 AC。不新增，不评 spec 完整性。
- 未达成的写明命令、期望与实际。

## 查质量

工具能查的（lint、类型、格式）不重复报。每条写 `文件:行号 — 观察 — 依据`。

依据取 AGENTS.md 的条款、`../_shared/docs-rules.md` 的「归属」，都没有就用 smell 名。

质量线索不影响判定。它留给下一轮，或由 `/skill:todo` 拆成 prefactor 任务。

## Smell 清单

- Duplicated Code：同一形状的代码散在多处。
- Speculative Generality：没有调用方的参数、钩子、抽象。
- Mysterious Name：名字看不出做什么、存什么。
- Primitive Obsession：字符串或基本类型顶着领域概念。
- Data Clumps：几个字段或参数总一起出现。
- Shotgun Surgery：一处改动要散着改多个文件。
- Divergent Change：一个文件为几件不相干的事被改。
- Middle Man：只做转发。

## 报告

写 `docs/audit/NNNN-YYYY-MM-DD.md`，与任务同号。同一天同一任务重审就覆盖。

```md
结论：回 coding

## 验收

- AC1 达成 — `pnpm vitest run test/checkout.spec.ts`
- AC2 未达成 — `pnpm vitest run test/refund.spec.ts`：期望余额 0，实际 120

## 质量

- src/checkout/cart.ts:88 — 两处同样的折扣算法 — Duplicated Code
```

结论三选一：可交付、回 coding、回 spec。同时出现未达成与无法判定，记回 coding。

报告写完提示用户：可交付就跑 `/skill:docs-commit`，其余按结论跑 `/skill:coding` 或 `/skill:spec`。
