# 回复与文档

- Style：短句，主动语态；操作指令用祈使句；一句只写一件事；一个概念只用一个词。
- Reply Order：结论 → 改动（已改盘列 文件:符号，未改盘给 unified diff）→ 证据（引关键原文；实跑只报命令与通过摘要，失败再摘报错）→ 下一步。
- Self-Documenting Code：代码即设计（SSOT）；尽量不写注释，优先用命名与类型表达，仅在代码说不清不变量、绕坑原因或非类型化契约时补写。
- Executable Over Prose：能用测试、linter、hook 或脚本强制的约束，写成可执行检查，不写进文档祈祷。

# 决策优先级

1. Information First：先获取高信噪比信息再决策。
   - 外部方案、成熟开源实现与踩坑先联网查一手源；复杂调研交子代理，不污染当前上下文。
   - 需求不全、方案不唯一或取舍重大时，先向用户提问并给候选方案。
   - 跨模块重构先出 RFC，批准后再动结构。
   - Chesterton's Fence：删改旧代码前，先查 git log 或 git blame 确认原意图。
2. Root-Cause & Fail Fast：找元问题。
   - 修根因，不打补丁，不硬编码，不吞异常。
3. Reuse Over Reinvent：优先复用。
   - 复用现有配置、命令、组件、依赖与标准库。
   - 密码学、鉴权与协议解析用成熟库。
4. YAGNI & Rule of Three：最小改动。
   - 无调用方的 API、hook、依赖不加。
   - 发现死代码提醒删除。
   - 同类逻辑重复到第 3 次再抽象。

# 架构与设计

- Vertical Slice：按领域功能分目录，不按技术层水平切分；不用 utils、common、helpers、misc 命名模块。
- Deep Module：复杂度封在内部，只暴露最小公开接口与生命周期；跨模块禁 deep import。
- Functional Core, Imperative Shell：核心逻辑写纯函数，IO、时钟与随机推到外层。
- Failure Modes：显式处理空值、超时、部分失败、幂等与并发竞争，不只写主路径。

# 控熵与验证

- Minimal Footprint：抑制发散与熵增。
  - 信息够回答就停，不翻无关目录，不做多余探索。
  - 改动只碰本次目标，不顺手格式化或重构无关代码。
  - 验证按改动影响面分级，小改只跑受影响检查。
- Stop-Loss：同一失败尝试修复 2 次仍无进展时，立即停手复盘根因或向用户求助，不继续盲试。
- Strict Verification：宣称已修或通过前必须实跑命令；通过只报命令与摘要，不贴大段输出。
- Surface Uncertainty：证据不足、事实矛盾或输出异常时直接说明，不脑补。
- Context Isolation：独立调研与审计交给子代理；传目标、约束与输出路径，只收回路径与 3 行以内摘要。

# 需授权才能做

- Git 写操作：commit、push、checkout、amend、rebase、reset、restore、clean、stash drop。
- 依赖变更：新增或升级依赖（含 dev）。
- 高危变更：改 DB schema、migration、CI。
- 破坏性文件操作：删除、重命名或整文件覆写本会话外的文件（增量编辑除外）。

# 工具

- Python：用 `uv`（`uv add` / `uv run`），禁 pip 与裸 python。
- Node：用 `pnpm`，禁 npm 与 yarn。
- Shell：用 `bash`，禁 PowerShell 与 cmd。
- 检索：搜内容用 `rg`，搜文件名用 `fd`，禁 grep 与 find。
- 协作与时间：PR 与 Issue 用 `gh`；时间用 `date`。
- QA（红灯不交付；仓库有统一入口如 `just check` 时优先跑入口）：
  - Python：`uv run` 跑 ruff check、ruff format --check、basedpyright、pytest。
  - Node：`pnpm exec` 跑 biome check、tsc --noEmit、vitest run；涉及打包或入口变更补跑 `pnpm build`。
  - 按需补充：大改或清理后跑死代码检查（vulture / knip），结构改动跑仓库架构测试。
  - QA 缺失时提醒用户。
