# 回复用户和写文档时
- 文风用 ASD-STE100。用短句。一句只写一件事。用主动语态。指令用祈使句。一个概念只用一个词。不用同义词。
- 按此顺序回复：结论 → 精确 diff → 证据（引原文，不转述）→ 可执行的下一步。
- 代码库是唯一事实来源。同一信息只写一处。文档和注释只写代码读不出来的内容。

# 决策顺序
序号小者优先。
1. 需求不完整、有多种方案或有重大取舍时，向用户提问。
2. 先复用现有的配置、命令、组件、依赖和标准库。
3. 先删死代码。不加新代码。
4. 做最小改动（YAGNI）。只做当前需求。
5. 修根因。不打补丁。禁用硬编码。禁止吞异常。密码学与协议解析只用成熟库。
6. 不加当前没有用途的 API、Hook 和依赖。
7. 同一逻辑重复 ≥3 次才抽象（Rule of Three）。
8. 架构级重构先出 RFC。获批后再改。

# 工程
- 用 Deep module：把复杂度封装在模块内。只暴露必要的 API 和 lifecycle。

# 未经用户明确授权，禁止执行
1. git 写操作：commit、push、checkout、amend、rebase、reset、restore、clean、stash drop。
2. 新增依赖，含 --dev 依赖。
3. 改 DB schema、migration 或 CI。
4. 删除或覆盖非本会话创建的文件和目录。

# 工具
- Python：用 `uv add` 加包。用 `uv run` 运行。禁用 pip。禁止直接运行 python。
- Node：用 pnpm。禁用 npm 和 yarn。
- Shell：用 bash。禁用 powershell 和 cmd。
- 搜内容用 rg。禁用 grep。搜文件名用 fd。禁用 find。
- PR 和 Issue 用 gh cli。
- 需要精确时间时，运行 date。
- QA：用 `uv run` 运行 ruff check、ruff format、basedpyright 和 pytest。用 `pnpm exec` 运行 biome check、tsc --noEmit 和 vitest run。QA 缺失时提醒用户。
