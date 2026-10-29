# 项目文档通用规则

写项目文档的 skill 先读这一份。

## 位置

- 文档进 `docs/`：`specs/`、`adr/`、`decisions/`、`research/`、`modules/`、`todos/`、`audit/` 各一个子目录。

文件名按四类：

| 类 | 制式 | 例 |
|---|---|---|
| 单例 | `UPPER_SNAKE.md` | `docs/ARCHITECTURE.md`、`docs/GLOSSARY.md`、`docs/GLOSSARY-MAP.md`、`docs/todos/README.md` |
| 有序条目 | `NNNN-slug.md`，编号 4 位补零，取目录最大号加一 | `specs/0001-checkout.md`、`adr/0003-pg-vs-mysql.md`、`decisions/0007-refund-window.md`、`research/0002-stripe-api.md` |
| 任务与验收 | `T<NN>.md`、`T<NN>-YYYY-MM-DD.md`，任务号补零两位、全局连续 | `todos/T01.md`、`audit/T01-2025-01-14.md` |
| 模块 | `<module>.md` | `modules/checkout.md` |

- 一个条目一份文件，不拼成一份大文件；第一次用就建目录。
- 有序条目首行是 H1：`# <NNNN> <标题>`。
- 引用写 `ADR-NNNN`、`DEC-NNNN`。`adr/` 与 `decisions/` 各自编号，同号可并存。多 context 术语表布局见 `/skill:docs-glossary`。
- 报告落盘看消费方：跨会话消费（audit → coding）落盘 `docs/audit/`；当次会话消费（maintain、debug、docs-pr）不落盘。
- 任务格式见 `/skill:plan`；阶段表在 `docs/todos/README.md`。
- 一个文件只写一类事实；内容长到要滚动找，就拆成目录，目录内 `README.md` 当索引。
- 根 `README.md` 的结构与写法见 `/skill:docs-readme`。README「文档」小节只收四类：架构、术语、模块、ADR；`specs/`、`research/`、`decisions/`、`todos/`、`audit/` 不进。
- 仓库根的 `README.md`、`AGENTS.md` 是入口，不算文档，不搬。有内容才建目录。

## 写什么

只写代码读不出来的：不变量、绕开某个坑的原因、必须保持的顺序、口头约定。

## 归属

一个事实只有一个载体。写之前查表；不属于当前载体，就写路径或命令。

| 事实 | 载体 |
|---|---|
| 行为、契约、默认值、错误、目录布局、`--help` 输出、类型签名 | 代码与测试 |
| 难回退、有真实备选的选型 | `docs/adr/` |
| 规划期用户拍板的取舍（够不上 ADR 门槛的） | `docs/decisions/` |
| 模块职责、允许的依赖方向 | `docs/ARCHITECTURE.md` |
| 模块的用法与取舍 | `docs/modules/<module>.md` |
| 术语 | `docs/GLOSSARY.md` |
| 任务做什么、验收跑什么、做到哪一步 | `docs/todos/` |
| 这轮做什么、不做什么 | `docs/specs/` |
| 验收结论 | `docs/audit/` |
| 外部世界的现状 | `docs/research/` |

spec 的「实现决定」在实现后归代码与 ADR：正文只留指针。

代码与文档冲突时，改文档。

## 落盘前

1. 删掉这段，读者会少知道什么？答不出就删整句，不修字。
2. `rg` 搜同一句话的第二次出现。有就删一处，留指针。

## 进度

查进行中的任务：`rg -l '^- \[~\]' docs/todos/`。spec、ADR、架构、模块文档不写状态与进度，只描述现状，随代码改。
