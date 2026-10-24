# 项目文档通用规则

写项目文档的 skill 先读这一份。

## 位置

- 文档进 `docs/`：`specs/`、`adr/`、`decisions/`、`research/`、`modules/` 各一个子目录，术语表 `docs/GLOSSARY.md`，架构 `docs/ARCHITECTURE.md`，任务 `docs/todos/`。
- 一个条目一份文件，不拼成一份大文件：spec `NNNN-slug.md`、ADR `NNNN-slug.md`、决策 `D<NN>-slug.md`、任务 `T<NN>.md`、模块 `docs/modules/<module>.md`。
- 任务格式见 `/skill:plan`；阶段表在 `docs/todos/README.md`。
- 一个文件只写一类事实；内容长到要滚动找，就拆成目录，目录内 `README.md` 当索引。
- 每份文档在 `README.md`「文档」小节占一行：是什么、什么时候看。`docs/decisions/`、`docs/audit/`、`docs/todos/` 是流水，模块文档由 `docs/ARCHITECTURE.md` 的模块表索引，都不进 README。
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
