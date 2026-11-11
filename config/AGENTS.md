# 回复与文档
- 短句，主动语态。指令用祈使句。一句只写一件事。一个概念只用一个词。
- 回复顺序：结论 → 改动（unified diff）→ 证据（引原文）→ 下一步。
- 文档与注释只补代码说不出的。代码即设计，D.R.Y.。

# 决策优先级
1. 获取信息：联网找成熟方案与踩坑；需求不全、方案不唯一、取舍重大时先提问；跨模块重构先出 RFC
2. 找元问题：不打补丁，不硬编码，不吞异常。
3. 优先复用：现有配置、命令、组件、依赖、标准库；密码学与协议解析用成熟库。
4. 最小改动（YAGNI）：无调用方的 API、Hook、依赖不加；死代码提醒删；重复到第 3 次才抽象。

# 架构
- 按功能分层，不按技术分层。
- Deep module：复杂度封在内部，只对外暴露必要 API 与 lifecycle。

# 控制范围
- 信息足够就回答，不做多余验证
- 不要翻看被问对象无关的目录

# 需授权才能做
- git 写操作：commit、push、checkout、amend、rebase、reset、restore、clean、stash drop。
- 新增依赖，含 dev。
- 改 DB schema、migration、CI。
- 删除或覆盖本会话外创建的文件。

# 工具
- Python 用 uv（`uv add` / `uv run`），禁 pip 与直接运行 python。
- Node 用 pnpm，禁 npm 与 yarn。
- Shell 用 bash，禁 powershell 与 cmd。
- 搜内容用 rg，搜文件名用 fd，禁 grep 与 find。
- PR 与 Issue 用 gh。
- 时间用 date。
- QA
  - `uv run` 跑 ruff check、ruff format、basedpyright、pytest。
  - `pnpm exec` 跑 biome check、tsc --noEmit、vitest run。
  - QA 缺失时提醒用户。
