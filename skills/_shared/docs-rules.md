# 项目文档通用规则

写项目文档前，先读本文件。

## 位置

文档放进 `docs/`。每个子目录放一类文档：`specs/`、`adr/`、`decisions/`、`research/`、`modules/`、`todos/`、`audit/`。

文件名分四类：

| 类 | 制式 | 例 |
|---|---|---|
| 单例 | `UPPER_SNAKE.md` | `docs/ARCHITECTURE.md`、`docs/GLOSSARY.md`、`docs/GLOSSARY-MAP.md`、`docs/todos/README.md` |
| 有序条目 | `NNNN-slug.md`，编号 4 位补零，取目录最大号加一 | `specs/0001-checkout.md`、`adr/0003-pg-vs-mysql.md`、`decisions/0007-refund-window.md`、`research/0002-stripe-api.md` |
| 任务与验收 | `T<NN>.md`、`T<NN>-YYYY-MM-DD.md`，任务号补零两位、全局连续 | `todos/T01.md`、`audit/T01-2025-01-14.md` |
| 模块 | `<module>.md` | `modules/checkout.md` |

- 一个条目一个文件。不要拼成一个大文件。第一次使用就建目录。
- 有序条目的首行是 H1：`# <NNNN> <标题>`。
- 引用写 `ADR-NNNN`、`DEC-NNNN`。`adr/` 与 `decisions/` 分别编号。同号可以并存。多 context 的术语表布局见 `/skill:docs-glossary`。
- 按消费方决定是否写入文件。跨会话消费（audit → coding）写入 `docs/audit/`。当次会话消费（maintain、debug、docs-pr）不写入。
- 任务格式见 `/skill:plan`。阶段表在 `docs/todos/README.md`。
- 一个文件只写一类事实。内容长到要滚动查找，就拆成目录。目录内的 `README.md` 当索引。
- 根 `README.md` 的结构与写法见 `/skill:docs-readme`。README 的「文档」小节只收四类：架构、术语、模块、ADR。`specs/`、`research/`、`decisions/`、`todos/`、`audit/` 不进。
- 仓库根的 `README.md`、`AGENTS.md` 是入口。它们不算文档，不要搬。有内容才建目录。

## 写什么

只写代码读不出来的内容：不变量、绕开某个坑的原因、必须保持的顺序、口头约定。

## 归属

一个事实只有一个载体。写之前查下表。事实不属于当前载体，就写路径或命令。

| 事实 | 载体 |
|---|---|
| 行为、契约、默认值、错误、目录布局、`--help` 输出、类型签名 | 代码与测试 |
| 难回退、有真实备选的选型 | `docs/adr/` |
| 规划期用户拍板的取舍（够不上 ADR 门槛的） | `docs/decisions/` |
| 模块职责、允许的依赖方向 | `docs/ARCHITECTURE.md` |
| 模块的用法与取舍 | `docs/modules/<module>.md` |
| 术语 | `docs/GLOSSARY.md` |
| 任务做什么、验收运行什么、做到哪一步 | `docs/todos/` |
| 这轮做什么、不做什么 | `docs/specs/` |
| 验收结论 | `docs/audit/` |
| 外部世界的现状 | `docs/research/` |

spec 的「实现决定」在实现后归代码与 ADR。正文只留指针。

代码与文档冲突时，改文档。

## 写入前

1. 问：删除这段，读者会少知道什么？答不出就删除整句，不要改文字。
2. 用 `rg` 搜同一句话的第二次出现。有第二处就删除一处，留指针。

## 进度

查进行中的任务：`rg -l '^- \[~\]' docs/todos/`。spec、ADR、架构、模块文档不写状态与进度。它们只描述现状，随代码改。
