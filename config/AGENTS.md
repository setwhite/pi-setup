# 回复用户和写文档时
- 文风用 ASD-STE10
- 回复顺序：结论 → 精确 diff → 证据（引原文，不转述）→ 可执行的下一步。
- 事实来源：代码库是唯一事实来源。同一信息只写一处。文档与注释只写代码读不出来的内容；注释尽量不写。

# 决策顺序
序号小者优先。
1. 需求不完整、有多种方案、有重大取舍时，向用户提问。
2. 先复用现有配置、命令、组件、依赖、标准库。
3. 先删死代码，不新增代码。
4. 做最小改动（YAGNI）：只做当前需求。
5. 修根因，不打补丁。禁硬编码，禁吞异常。密码学与协议解析只用成熟库。
6. 无当前用途的 API、Hook、依赖不加。
7. 同一逻辑重复 ≥3 次才抽象（Rule of Three）
8. 架构级重构先出 RFC，获批再改。

# 工程
- Deep module：复杂度封装在模块内，只暴露必要的 API 与 lifecycle。
- Circuit breaker：连续失败 3 次即停，汇报状态、原因、关键日志、可疑假设。

# 未经用户明确授权，禁止执行
1. git 写操作：commit、push、checkout、amend、rebase、reset、restore、clean、stash drop。
2. 新增依赖，含 --dev 依赖。
3. 改 DB schema、migration 或 CI。
4. 删除或覆盖非本会话创建的文件与目录。

# 工具
- Python：`uv add` 加包，`uv run` 运行。禁 pip，禁直接 python。
- Node：pnpm。禁 npm、yarn。
- Shell：bash。禁 powershell、cmd。
- 搜内容用 rg，禁 grep。搜文件名用 fd，禁 find。
- PR、Issue 用 gh cli。
- 需精确时间跑 date。
- QA：`uv run` 跑 ruff check、ruff format、basedpyright、pytest；`pnpm exec` 跑 biome check、tsc --noEmit、vitest run。QA 缺失时提醒用户。
