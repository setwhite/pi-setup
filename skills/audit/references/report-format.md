# 审计报告格式

一份报告一个任务：`docs/audit/T<NN>-YYYY-MM-DD.md`，任务号补零两位（与 `docs/todos/T01.md` 同一编号），日期用 `date +%F`，同一天同一任务重审就覆盖。同一任务的历次报告按文件名相邻。

````md
# T03 审计 2025-01-14

VERDICT: pass

## 验

- AC1 达成 — `pnpm vitest run test/checkout.spec.ts`
- AC2 未达成 — `pnpm vitest run test/refund.spec.ts`：期望余额 0，实际 120
- AC3 无法判定 — spec 的「足够快」没有对应检查

## 规范

- src/checkout/cart.ts:88 — 两处同样的折扣算法 — Duplicated Code
- src/checkout/cart.ts:12 — 参数 7 个 — AGENTS：函数参数不超过 5 个

验轴 1 条未达成，规范轴 2 条。最严重：AC2 未达成。
````

- 第一行固定是判定：`pass` 两轴全过，其余情况 `rework`。
- 验轴每条 AC 一行：结论、检查命令、未达成时的实际与期望。
- Finding 格式固定 `文件:行号 — 观察 — 依据`，依据取 AGENTS 条款、AC 编号或 smell 名。
- 命令输出不落盘，下次审计现场重跑。
