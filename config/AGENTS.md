# Artifact（response、注释、Docstring、Commit、文档）
- 用自然、地道、极简的中文；术语保留英文。
- BLUF：先给结论或代码；代码给完整的或精确 diff，不复述修改过程；有更简单的方案就一句话点出。
- Grounding：引用原文并附文件路径，不转述；技术判断附代码或数据。
- Actionable handoff：需用户介入时，结尾给出 2 分钟内可完成的「下一步」指令。
- 代码库是唯一事实来源：文档只留代码里读不出的（决策、事实、索引）。

# 决策优先级（冲突时编号小者优先）
1. 需求澄清：需求不具体或有重大取舍时，停止猜测，直接提问。
2. 配置优先：先用现有配置、系统命令或手动操作解决。
3. 复用优先：先删除死代码（dead code），或复用现有组件。
4. 标准库优先：优先用标准库与现有依赖；密码学、协议解析等必须用成熟库（don't roll your own crypto）。
5. 最小改动（YAGNI）：只做满足当前需求的最少改动并注明影响范围；无当前用途的 API、Hook、依赖一律不加。
   - 修复根因：禁止 hardcoded values、吞异常（exception swallowing）、band-aid fix。
6. Rule of Three：同一逻辑重复 ≥3 次才允许抽象。
7. 重构：架构导致的严重冗余，先出 RFC，获批后再改。

# Engineering
- Deep module：复杂度封装在模块内部，对外只暴露必要的 API 与生命周期。
- Circuit breaker：同一报错连续失败 3 次即停止。汇报：当前状态、失败原因、核心日志、可疑假设。

# Confirmation（approval gate：未经用户同意，严禁执行）
1. 危险 Git：commit、push、checkout、改写历史（amend/rebase/reset）、丢弃未提交改动（restore/clean/stash drop）。
2. 基建变更：新增任何依赖（含 `--dev`）、改 DB schema/migration、改 CI。
3. 破坏性写：删除或覆盖 非当前会话创建的文件或目录。

# Tooling Rules
- Python：`uv`（`uv add`、`uv run`）。禁用 `pip` 与直接运行 `python`。
- Python QA：`uv run ruff check`（lint）、`uv run ruff format`（format）、`uv run basedpyright`（typecheck）、`uv run pytest`（test）。
- Node：`pnpm`。禁用 npm、yarn。
- TS QA：`biome check`（lint + format）、`tsc --noEmit`（typecheck）、`vitest run`（test）。
- Shell：`bash`。禁用 powershell、cmd。
- 搜索：内容用 `rg`；文件名用 `fd`。禁用 bash 的 grep / find。
- GitHub：PR、Issue 操作一律用 `gh`。
- 精确时间：先运行 `date`。
