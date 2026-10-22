# 项目文档通用规则

写项目文档的 skill 先读这一份。

## 位置

- 文档进 `docs/`：`specs/`、`adr/`、`research/` 各一个子目录，术语表 `docs/GLOSSARY.md`，架构 `docs/ARCHITECTURE.md`，任务 `docs/todos/`。
- 任务一份一个 `docs/todos/T<NN>.md`，格式见 `/skill:slice`；阶段表在 `docs/todos/README.md`。
- 每份文档在 `README.md`「文档」小节占一行：是什么、什么时候看。`docs/audit/`、`docs/todos/` 是状态机的一环，不进索引。
- 仓库根的 `README.md`、`AGENTS.md` 是入口，不算文档，不搬。有内容才建目录。

## 只写环境查不到的

不变量、绕开某个坑的原因、必须保持的顺序、口头约定。目录布局、`--help` 输出、类型签名本身就是事实来源。

## 剪枝

- 单一来源：一个含义只在一处定义，别处引路径。
- 只留对当下有用的行；删掉不影响行为就删整句，不修字。

## 进度

进度只有一个来源：`docs/todos/` 任务文件的复选框。spec、ADR、架构、模块文档不写状态与进度，只描述现状，随代码改。
