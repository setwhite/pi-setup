# 项目文档通用规则

## 位置

文档放 `docs/`，一个子目录一类：`specs/`、`decisions/`、`research/`、`modules/`、`todos/`、`audit/`。

| 类 | 制式 | 例 |
|---|---|---|
| 单例 | `UPPER_SNAKE.md` | `docs/ARCHITECTURE.md`、`docs/GLOSSARY.md`、`docs/GLOSSARY-MAP.md` |
| 条目 | `NNNN-slug.md`，4 位补零，取目录最大号加一 | `specs/0001-checkout.md` |
| 模块 | `<module>.md` | `modules/checkout.md` |

- 一个条目一个文件。第一次使用就建目录。
- 任务与验收报告同号：`todos/0001-add-cart.md`、`audit/0001-2025-01-14.md`。
- 引用写 `DEC-NNNN`。
- 目录里的 `README.md` 当索引，一条一行，索引与文件双向对得上。

## 归属

一个事实只有一个载体。

| 事实 | 载体 |
|---|---|
| 行为、契约、默认值、错误、目录布局、类型签名 | 代码与测试 |
| 选型与取舍 | `docs/decisions/` |
| 模块职责、依赖方向、seam | `docs/ARCHITECTURE.md` |
| 模块用法 | `docs/modules/<module>.md` |
| 术语 | `docs/GLOSSARY.md` |
| 本轮的契约与验收 | `docs/specs/` |
| 任务与进度 | `docs/todos/` |
| 验收结论 | `docs/audit/` |
| 外部世界的现状 | `docs/research/` |

只写代码读不出来的：不变量、绕开某个坑的原因、必须保持的顺序、口头约定。

同一句话搜第二处。有就删一处，留指针。

代码与文档冲突，改文档。

## 进度

`rg -l '^- \[~\]' docs/todos/`

spec、决策、架构、模块文档不写状态。它们只描述现状。
