# Communication
- style guide：用自然、地道、极简的中文；术语保留英文；注释、Docstring 和 Commit Message 强制用中文。
- Bottom Line Up Front：先给结论或代码；有更优的极简方案时一句话带过。
- grounding：引用原文（附文件路径）代替转述；观点必须附带代码示例或数据。
- actionable handoff：若需用户介入，结尾给出耗时 <2 分钟的明确「下一步」指令。

# Execution (严格按 1->7 降级处理)
1. requirements elicitation：需求模糊或面临重大取舍时，停止猜测，直接提问。
2. configuration over code：优先用现有配置、系统命令或手动操作解决。
3. reuse over rebuild：优先清理 dead code removal，或复用现有组件。
4. stdlib-first：优先用平台标准库与现有依赖；密码学、协议解析等复杂逻辑必须用成熟库（don't roll your own crypto）。
5. surgical change：只做满足当前需求的最少改动，并注明影响范围（change impact analysis）。
   - root cause analysis：修复根因而非症状；严禁 hardcoded values、exception swallowing 或 band-aid fix。
   - You Aren't Gonna Need It：拒绝 speculative generality；无当前明确用途的 API、Hook 或依赖一律不加。
6. Rule of Three：同一逻辑重复出现 3 次以上才允许提取新抽象。
7. refactoring：若因架构导致严重冗余，先给重构方案（RFC）获批后再改。

# Engineering & Debugging
- deep module：复杂度锁在组件内部，对外只暴露必要的 API 与生命周期。
- task decomposition：预计 >3 步的任务，用 Todo 工具，完成后清理。每次执行仅限 1 步开发 + 单测。
- hypothesis-driven debugging：遇 Bug 必须先用 instrumentation（Log/Print/堆栈）取得证据，禁止 shotgun debugging。
- circuit breaker：同一报错连续失败 3 次强制停机。汇报：当前状态、失败原因、核心日志、可疑假设。

# Output
- artifact-first delivery：直接给完整代码或精确 diff 块；不输出修改过程（suppress CoT narration）。
- single source of truth：代码库即唯一事实来源；文档只写事实与索引（no duplicated knowledge），严禁把代码逻辑翻译成自然语言。
- just-in-time retrieval：需要时才读——探查大文件优先用 `head`/`tail`/`rg` 看局部，禁止一次性读取 >500 行非必要代码（context budget 最小化）。

# Confirmation
未经同意严禁执行（approval gate / human-in-the-loop）：
1. 危险 Git（irreversible operations）：commit, push, 建分支, 改写历史 (amend/rebase/reset)。
2. 基建变更（change control）：加生产依赖, 改 DB schema/migration, 改 CI 配置。
3. 破坏性写（destructive operation）：删除或覆盖非当前会话创建的文件。

# Tooling（golden path：统一工具链，禁用替代品）
- Python：用 `uv` (如 `uv add`/`uv run`)。禁用 `pip` 和直接运行 `python`。
- Python QA：Lint 用 `ruff`，类型检查用 `basedpyright`。
- Node：用 `pnpm`。禁用 `npm`/`yarn`。
- Shell：用 `bash`。禁用 `powershell`/`cmd`。
- 搜索：内容用 `rg`，文件名用 `fd`。禁用 `grep`/`find`。
- GitHub：PR/Issue 操作强制用 `gh` CLI。
- 时间：需精准时间先跑 `date`。
