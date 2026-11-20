# 项目文档规则

## 目录与归属（SSOT）

文档放 `docs/`；同一事实只存一处；发现重复删冗余留指针；代码与文档冲突改文档。

- 代码与可执行检查：行为、签名、默认值、错误、目录布局、模块依赖约束。
- `docs/ARCHITECTURE.md`：模块职责、不变量与 seam 清单。
- `docs/modules/<module>.md`：模块用法与非显而易见的取舍。
- `docs/GLOSSARY.md`：领域术语。
- `docs/adr/`：不可逆选型与取舍（ADR）。
- `docs/specs/`：本轮契约与 AC。
- `docs/todos/`：当前切片 todo 与进度。
- `docs/audit/`：独立验收结论与质量线索。
- `docs/research/`：外部事实与调研结论。

## 约定

- 按需建目录与文件，不维护子目录 `README.md` 索引。
- todo 必须绑定对应 spec 路径。
- `ARCHITECTURE.md`、`modules/`、`adr/` 与 `specs/` 只写现状，不写进度。
- 查待审 todo：`rg -l '^- \[~\]' docs/todos/`。
