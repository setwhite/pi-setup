# 项目文档规则

## 目录与归属（SSOT）

项目文档放 `docs/`；同一事实只存一处，重复的删掉留路径；代码与文档冲突改文档。

- 代码与可执行检查：行为、签名、默认值、错误、目录布局、依赖约束。
- `docs/ARCHITECTURE.md`：模块职责、核心不变量与测试边界（seam）清单。
- `docs/modules/<module>.md`：模块用法与非显而易见的取舍。
- `docs/GLOSSARY.md`：领域术语表。
- `docs/adr/`：难回退的选型与取舍记录（ADR）。
- `docs/specs/`：本轮规格与验收标准（AC）。
- `docs/todos/`：当前任务拆解（todo）与进度。
- `docs/audit/`：独立验收结论与质量建议。
- `docs/research/`：外部事实与调研结论。

## 约定

- 按需建文件，不维护子目录 `README.md` 索引；todo 必须写明对应 spec 路径。
- `ARCHITECTURE.md`、`modules/`、`adr/`、`specs/` 只写现状，不写进度。
- 查待验收 todo：`rg -l '^- \[~\]' docs/todos/`。
