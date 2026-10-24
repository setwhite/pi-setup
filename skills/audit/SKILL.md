---
name: audit
disable-model-invocation: true
description: 独立审计：只判 AC，质量问题只记录。
---

# 审计流程

## 前置条件

- 独立会话：在未参与编写的新会话中运行。
- 只读：不改代码与 `docs/todos/`，唯一写入是本次报告（`docs/audit/`）。
- 不执行修复，不调其他 skill，只在报告里点名下一步。

## Step 1 — 准备材料

在 `docs/todos/` 找 `[~]` 的任务（查法见 `../_shared/docs-rules.md`），多个时让用户指定一个；检查 Git 状态，确认改动范围。

**Completion criterion**：明确改动范围与验收标准。

## Step 2 — 逐条核对 AC

1. 自己跑每条 AC 对应的自动化检查；文件里写的、别人报告的不算证据。
2. 每条给一个结论：达成（含用户明确豁免）/ 未达成 / 无法判定（没有可跑的检查，或检查与 AC 说的不是一件事）。
3. 只判 AC：不新增 AC，不评 spec 完整性，不把 AC 之外的改进算作失败。
4. 不跑全套 E2E，全套测试留在收工。

**Completion criterion**：每条 AC 都有结论和证据。

## Step 3 — 检查代码质量（不参与判定）

1. 对照 `AGENTS.md` 与仓库里的规范文件；工具已能查的（lint、类型、格式）不重复报。文档与代码冲突，或同一件事写在两处，也算 finding，依据写 `../_shared/docs-rules.md` 的「归属」。
2. 仓库没写规范处用文末「Smell 清单」兜底：只是判断线索，不是违规认定；冲突时以仓库为准。
3. 每条 finding 写 `文件:行号 — 观察 — 依据`；没有明显问题写「无」，不凑数。

质量 finding 不影响 VERDICT，不要求本轮修复，也不自动开任务；要处理就在下一阶段经 `/skill:plan` 拆成 prefactor 任务，或另开任务。

**Completion criterion**：每条 finding 都能指到依据（AGENTS 条款、`../_shared/docs-rules.md` 的「归属」，或 smell 名）。

## Step 4 — 输出

按文末「报告格式」落盘 `docs/audit/T<NN>-YYYY-MM-DD.md`，并在会话里重述同一份内容。报告是本次验收记录，不是代码质量清零证明；只给意见，不给实现方案。

**Completion criterion**：判定与质量线索已落盘，未修改代码与 `docs/todos/`。

## 报告格式

一份报告一个任务：`docs/audit/T<NN>-YYYY-MM-DD.md`，任务号补零两位（与 `docs/todos/T01.md` 同编号），日期用 `date +%F`，同一天同一任务重审就覆盖；历次报告按文件名相邻。

````md
# T03 审计 2025-01-14

VERDICT: re-coding

## 验收

- AC1 达成 — `pnpm vitest run test/checkout.spec.ts`
- AC2 未达成 — `pnpm vitest run test/refund.spec.ts`：期望余额 0，实际 120

## 质量

- src/checkout/cart.ts:88 — 两处同样的折扣算法 — Duplicated Code
- src/checkout/cart.ts:12 — 参数 7 个 — AGENTS：函数参数不超过 5 个
````

第一行固定是判定：

- `pass`：每条 AC 达成（含用户明确豁免）。下一步由 coding 会话在用户批准后改 `[x]`，再走 `/skill:docs-commit`。
- `re-coding`：至少一条 AC 未达成。写明失败命令与期望 vs 实际，原始输出不落盘。回 `/skill:coding`，只修失败的 AC。
- `re-plan`：至少一条 AC 无法判定。点名哪条及原因；回 `/skill:plan`，只改任务与 AC，不写代码。

同时出现 `re-coding` 与 `re-plan` 先判 `re-coding`；修完复审仍无法判定才判 `re-plan`。`## 验收` 每条 AC 一行：结论、检查命令、未达成时的实际与期望。`## 质量` 每条一行 `文件:行号 — 观察 — 依据`，不影响 VERDICT，`pass` 也可带 finding，没有写「无」。命令输出不落盘，下次现场重跑。

## Smell 清单

（Fowler, Refactoring ch.3）仓库没写规范处靠它找线索，每条是「是什么 → 怎么办」：

- Mysterious Name：名字看不出它做什么、存什么 → 改名；想不出诚实的名字说明设计是浑的。
- Duplicated Code：同一段逻辑形状散在多个 hunk 或文件 → 抽出共同形状，两处都调它。
- Feature Envy：方法摸别人的数据多过自己的 → 挪到它羡慕的数据上。
- Data Clumps：几个字段或参数总同行 → 捆成一个类型传。
- Primitive Obsession：用基本类型或字符串顶替领域概念 → 给它一个小类型。
- Repeated Switches：同一类型上的同一套 switch／if 级联反复出现 → 换多态或共用映射表。
- Shotgun Surgery：一处改动逼着你在多个文件散着改 → 把一起变的东西收进同一模块。
- Divergent Change：一个文件因几件互不相干的事被改 → 拆开，每个模块只为一个原因变。
- Speculative Generality：为规格里没有的需求加的抽象、参数、钩子 → 删掉。
- Message Chains：`a.b().c().d()` 这类长导航，调用方不该依赖 → 用一个方法盖住整条链。
- Middle Man：类或函数几乎只做转发 → 砍掉，直接调真目标。
- Refused Bequest：子类忽略了继承来的大部分东西 → 弃继承，改组合。
