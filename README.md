# pi-setup：pi coding agent 安装与配置指南

> **目标读者**：AI coding agent，以及手动操作的用户。
>
> 本仓库是 [pi](https://github.com/earendil-works/pi) 的一套配置方案，含本体配置、扩展包与可选 skills。agent 读本文档，按步骤执行安装与配置。

---

## 1. 前置条件

确认环境已就绪：

| 依赖 | 检查命令 | 最低版本 |
|------|----------|----------|
| Node.js | `node -v` | ≥ 18 |
| npm | `npm -v` | ≥ 9 |
| Git | `git --version` | ≥ 2.30 |
| Bash | `bash --version` | 任意（Windows 需 Git Bash 或 WSL） |

**Windows**：pi 需要 Git Bash 或 WSL，不支持 PowerShell 与 CMD。pi 安装完成后，用户可直接向 pi 询问 Windows 环境配置。1.1 给出建议的 5 条 Git Bash 配置。

> **bash 查找顺序**：pi 按下列顺序查找 bash：
> 1. `~/.pi/agent/settings.json` 中 `shellPath` 指定的路径
> 2. `C:\Program Files\Git\bin\bash.exe`（Git Bash）
> 3. PATH 中的 `bash.exe`（可能是 Cygwin、MSYS2、WSL 等）
>
> **异常处理**：已装 Git，但 pi 报错找不到 bash，或找到了错误的 bash，按下列步骤处理：
> - 检查 `where bash` 的输出，确认排在第一位的 bash 路径。
> - Git Bash 不在 PATH 最前面时，编辑系统环境变量，把 `C:\Program Files\Git\bin` 移到最前面。
> - 或直接设置 `~/.pi/agent/settings.json` 的 `"shellPath"` 为 `"C:\\Program Files\\Git\\bin\\bash.exe"`。

### 1.1 Windows Git Bash 配置（可选）

Git Bash 在 Windows 上的默认行为与 Linux 不一致：换行符、文件名编码、符号链接。建议在安装 pi 前配置一次：

```bash
git config --global core.autocrlf input    # 仓库统一存 LF，防上 Linux 报 bad interpreter
git config --global core.quotepath false   # 中文文件名正常显示
git config --global core.symlinks true     # 认识符号链接
mkdir -p ~/.config/git && printf '*.bat text eol=crlf\n*.cmd text eol=crlf\n*.ps1 text eol=crlf\n' > ~/.config/git/attributes
echo 'export MSYS="winsymlinks:nativestrict${MSYS:+,$MSYS}"' >> ~/.bashrc   # 修 ln -s：MSYS 变量只认第一个选项
```

重开 Git Bash 后生效。老仓库需逐仓执行 `git config core.symlinks true`。

---

## 2. 配置 pi 本体

pi 的全局配置在 `~/.pi/agent/settings.json`。先复制本仓库的 `config/settings.json` 到该路径：

```bash
mkdir -p ~/.pi/agent
cp config/settings.json ~/.pi/agent/settings.json
```

### 2.1 配置项说明

下表列出 `config/settings.json` 各字段的含义。按需调整：

| 字段 | 默认值 | 何时调整 |
|------|--------|----------|
| `defaultProvider` / `defaultModel` / `defaultThinkingLevel` | 占位符（必填） | 默认模型。安装后填实际的 provider、模型与思考等级。不填就删掉这三个字段，让 pi 首次启动时引导选择 |
| `modelThinkingLevels` | 无 | 按模型固定启动思考等级。key 为 `provider/modelId`，value 取 `off`/`minimal`/`low`/`medium`/`high`/`xhigh`/`max`。在 `/settings` → Default thinking level per model 中设置，或手写进 `settings.json` |
| `enabledModels` | 空数组 | Ctrl+P 切换模型的候选列表。格式为 `provider/model`，可加 `:thinking` 后缀指定该模型的思考等级，如 `opencode-go/model:high`。填用户可用的模型 |
| `hideThinkingBlock` | `false` | 对话记录是否显示思考块。`true` 隐藏，只显示最终输出 |
| `cacheWarming` | `streaming` | 提示缓存保温。`off` 关闭、`streaming` 仅运行中保温、`idle` 空闲时也保温。仅在模型声明缓存有效期，且预估节省成本超过 $0.05 时生效。全局设置 |
| `compaction.enabled` | `true` | 自动压缩总开关。同一对象还可设 `reserveTokens`（预留回复 token，默认 16384）、`keepRecentTokens`（保留最近 token，默认 20000）、`modelOverrides`（按模型覆盖） |
| `sounds.agent_end` | `~/.pi/agent/sounds/hey_listen_navi.wav` | 音效文件路径。不需要音效就注释掉整个 `sounds` 块 |
| `markdown.mermaid` | `streaming` | Mermaid 图表渲染模式。`off` 不渲染、`final` 完成后一次渲染、`streaming` 边生成边渲染 |
| `tuiMode` | `fullscreen` | TUI 模式。`fullscreen` 全屏（pi 1.0 起为默认）、`regular` 常规滚动。在 `/settings` 中修改，立即生效 |
| `fullscreenScrollbar` | `hidden` | 全屏模式滚动条。取值 `auto`、`always`、`hidden` |
| `fullscreenCopyOnSelect` | `false` | 全屏模式下选中文本后是否自动复制。`false` 时用 Ctrl+X 复制选中内容 |
| `fullscreenWheelScrollLines` | `auto` | 全屏滚轮每格滚动的行数。`auto` 自适应（本地 macOS 终端一格一行），或取 1-100 |
| `fullscreenExitOutput` | `transcript` | 退出全屏时打印的内容。`transcript` 打印完整记录，`resume-hint` 打印恢复提示 |
| `autocompleteMaxVisible` | `5` | 自动补全下拉的可见条数，取 3-20 |
| `editorPaddingX` | `0` | 输入编辑器的水平内边距，取 0-3。数值越大，输入框左右留白越多 |
| `codemode.mode` | `on` | `codemode` 工具的呈现方式。`on` 时其他工具照常声明，描述中附加「可从脚本调用」的提示。`only` 时内置与扩展工具全部对模型隐藏，只在 `codemode` 描述中列出，模型一律经脚本调用。`codemode.inlineBudget` 控制声明预算，默认 3000。内置扩展（mcp、llama.cpp、codemode、tool-search）默认加载，用 `-builtin:<name>` 关闭 |
| `defaultTools` | `["+codemode"]` | 启动时启用的工具。`+name` / `-name` 在默认工具（`read`、`bash`、`edit`、`write`）上增减。`+codemode` 启用 codemode，agent 可写 JS 脚本并行调用工具，过滤大结果后再送入模型 |

### 2.2 音效文件（可选）

复制音效文件到 pi 的 sounds 目录：

```bash
mkdir -p ~/.pi/agent/sounds
cp config/sounds/hey_listen_navi.wav ~/.pi/agent/sounds/hey_listen_navi.wav
```

不需要音效就跳过此步骤，并注释掉 `~/.pi/agent/settings.json` 中的 `sounds` 块。

---

## 3. 安装 pi

执行任一命令安装 pi：

```bash
# 方式一：npm 全局安装
npm install -g --ignore-scripts @earendil-works/pi-coding-agent

# 方式二：curl 安装脚本
curl -fsSL https://pi.dev/install.sh | sh
```

安装完成后验证：

```bash
pi --version
```

命令应输出版本号。pi 首次启动时按 `settings.json` 的 `packages` 字段自动安装扩展包。

---

## 4. 安装扩展包

上一步的自动安装未触发时，手动安装：

```bash
pi install npm:pi-blackhole
pi install npm:pi-context-view
pi install npm:pi-chrome
pi install npm:pi-jingle
pi install npm:@narumitw/pi-btw
pi install npm:@narumitw/pi-usage
pi install npm:pi-web-search-lite
pi install npm:@ssk_dev/rpiv-ask-user-question-lean
pi install npm:@ssk_dev/rpiv-todo-lean
```

### 4.1 各扩展包的作用

| 扩展包 | 作用 |
|--------|------|
| [`pi-blackhole`](https://www.npmjs.com/package/pi-blackhole) | 合并压缩与观察记忆。`/blackhole` 用算法生成结构化摘要，替代 `/compact`，不调用 LLM。observer、reflector、dropper 三个后台 worker 把事实与决策沉淀为 observation 与 reflection。`recall` 工具在压缩后取回原文 |
| [`pi-context-view`](https://www.npmjs.com/package/pi-context-view) | `/context usage` 查看上下文占用分布，按工具、skill、消息等分类。`/context injections` 查看初始系统提示词、工具定义与各扩展注入的内容 |
| [`pi-chrome`](https://www.npmjs.com/package/pi-chrome) | Chrome 浏览器集成，用于网页测试与自动化 |
| [`pi-jingle`](https://www.npmjs.com/package/pi-jingle) | agent 完成工作时播放提示音 |
| [`@narumitw/pi-btw`](https://www.npmjs.com/package/@narumitw/pi-btw) | `/btw` 开启临时侧边对话。问答默认不写入主会话。只有显式带回的内容才加载到主编辑区，且不自动发送。支持全屏与左右分栏两种布局，分栏时实时展示主线程 |
| [`@narumitw/pi-usage`](https://www.npmjs.com/package/@narumitw/pi-usage) | `/usage` 查看当前账号用量与 DeepSeek API 余额。`/fast` 切换 Codex Fast 模式 |
| [`pi-web-search-lite`](https://www.npmjs.com/package/pi-web-search-lite) | 提供 `web_search` 与 `web_fetch` 工具。所有出站请求走同一代理。GitHub 链接交给 `gh` CLI 抓取，Reddit 链接换域名后抓取 |
| [`@ssk_dev/rpiv-ask-user-question-lean`](https://www.npmjs.com/package/@ssk_dev/rpiv-ask-user-question-lean) | 提供 `ask_user_question` 工具，向用户提问。原版 `@juicesharp/rpiv-ask-user-question` 的精简版，初始化 token 减少 83% |
| [`@ssk_dev/rpiv-todo-lean`](https://www.npmjs.com/package/@ssk_dev/rpiv-todo-lean) | 提供 `todo` 任务追踪工具。原版 `@juicesharp/rpiv-todo` 的精简版，初始化 token 减少 72% |

默认安装全部扩展包。下列场景需调整：

| 场景 | 操作 |
|------|------|
| 不需要音效 | 去掉 `pi-jingle` |
| 不需要浏览器集成 | 去掉 `pi-chrome` |
| 已装独立的 `pi-observational-memory` 或 `pi-vcc` | 先卸载，再装 `pi-blackhole`。三者冲突，见 5.1 |
| 已装原版 `@juicesharp/rpiv-ask-user-question` 或 `@juicesharp/rpiv-todo` | 先卸载，再装对应的 lean 版。两个版本同时加载会重复注册工具 |

lean 包依赖原版包。原版代码随 lean 包自动安装，`packages` 中只列 lean 版。已装原版时，先执行卸载命令：

```bash
pi uninstall npm:@juicesharp/rpiv-ask-user-question
pi uninstall npm:@juicesharp/rpiv-todo
```

---

## 5. 配置扩展包

部分扩展包有独立配置文件或外部依赖，需额外配置。

### 5.1 pi-blackhole

配置文件在 `~/.pi/agent/pi-blackhole/pi-blackhole-config.json`。扩展首次加载时按默认值自动生成，无需手工创建。压缩模式、阈值、记忆开关用 `/blackhole settings` 在 TUI 中调整，保存后立即生效。worker 模型（`model`、`observerModel`、`reflectorModel`、`dropperModel` 及各自的 fallback 数组）不在 overlay 中，只能手改配置文件。

要一次指定阈值与便宜的 worker 模型，复制仓库模板：

```bash
mkdir -p ~/.pi/agent/pi-blackhole
cp config/pi-blackhole/pi-blackhole-config.json ~/.pi/agent/pi-blackhole/pi-blackhole-config.json
```

模板各项：

| 键 | 作用 |
|----|------|
| `compactAfterTokens` | 固定压缩阈值，单位为 token。删除该键则用内置曲线，按模型上下文窗口自动缩放（0.90 @32k → 0.40 @1M） |
| `observerModel` / `reflectorModel` / `dropperModel` | 三个后台 worker 各自的模型与 `thinking` 等级。替换 `<your-*-provider>` 与 `<your-*-model>` 占位符 |
| `observerFallbackModels` / `reflectorFallbackModels` / `dropperFallbackModels` | 三个 worker 各自的 fallback 数组。元素字段与对应主模型相同，按顺序尝试。主模型报错、冷却或超时后，轮到下一个。不需要 fallback 就删掉 |
| `model` | worker 全部失败时的兜底模型。最后才轮到会话模型 |
| `sessionFallback` | `false` 时不回退会话模型。删掉该键或设为 `true` 则保留回退 |
| `workerAttemptTimeoutMs` | 每次 worker 尝试的硬超时，单位为毫秒。超时即切换下一个 fallback |
| `statusBar` | 状态栏的 token 计量（O/P/X）与 worker 进度 |

不需要的键直接删除。缺省时用扩展默认值。

`pi-blackhole` 与独立的 `pi-observational-memory`、`pi-vcc` 冲突，需先卸载：

```bash
pi uninstall npm:pi-observational-memory
```

### 5.2 pi-web-search-lite

复制配置文件到 `~/.pi/agent/pi-web-search-lite/config.json`：

```bash
mkdir -p ~/.pi/agent/pi-web-search-lite
cp config/pi-web-search-lite/config.json ~/.pi/agent/pi-web-search-lite/config.json
```

文件中 `apiKeys` 字段是占位符。`web_search` 支持多个搜索 provider：tavily、brave、exa、firecrawl、perplexity。填一个 key 即可使用，推荐 exa。`provider` 字段指定当前激活的后端。注册地址：https://exa.ai、https://jina.ai、https://tavily.com、https://firecrawl.dev、https://brave.com/search/api、https://perplexity.ai

其余字段按需调整。`proxy` 为空串时直连；填 `http://127.0.0.1:<端口>` 后，所有出站请求走本地代理。`fetch.extractors` 是正文提取的 fallback 链，按顺序尝试，直到成功（`html` 与 `jina` 都不需要 key）。GitHub 链接默认交给 `gh` CLI 抓取，使用前先执行 `gh auth login`。不需要时把 `handlers.github.enabled` 设为 `false`。

---

## 6. 安装 AGENTS.md

AGENTS.md 是 pi 启动时加载的全局项目指令。复制到全局位置：

```bash
cp config/AGENTS.md ~/.pi/agent/AGENTS.md
```

**内容概要**：中文编程规范，覆盖回复与文档文风、决策顺序、工程、授权边界、工具。节名与细则以 `config/AGENTS.md` 为准，本节只作速览。开发流程由第 7 节的 `plan` → `arch` → `coding` → `audit` 提供。

不需要中文规范就跳过此步骤，或在项目目录下另建 `.pi/AGENTS.md`。

---

## 7. 安装 Skills（可选）

Skills 是 pi 的可选能力。装入 `~/.pi/agent/skills/` 后，pi 即可发现。写作类 skill（`docs-article`）的文风规则来自第 6 节的 AGENTS.md。

> 下表只作速览。触发条件与流程细节以各 `skills/<name>/SKILL.md` 为准。

### 7.1 安装方法

每个 skill 是一个目录，含 `SKILL.md`，可选 `scripts/`、`references/` 等资源目录。复制需要的 skill 目录到 `~/.pi/agent/skills/`：

```bash
mkdir -p ~/.pi/agent/skills
cp -r skills/<skill-name> ~/.pi/agent/skills/
cp -r skills/_shared ~/.pi/agent/skills/    # arch、audit、coding、plan 与各 docs-* 用 ../_shared/*.md 相对引用，必须一起复制
```

`_shared/` 没有 `SKILL.md`，不是 skill，只是被上述 skill 引用的规则文件。

### 7.2 Skills 分类

`触发方式` 一列有两种取值。user-invoked：`SKILL.md` 写了 `disable-model-invocation: true`，只能由用户显式调用。model-invoked：模型按需求自行加载。

#### 开发流程

| Skill | 触发方式 | 用途 |
|-------|----------|------|
| `plan` | user-invoked | 规划一个阶段：调研、追问到共识，写 spec 与 `docs/todos/` 任务 |
| `arch` | user-invoked | 系统结构与测试 seam：维护 ARCHITECTURE.md 与模块文档 |
| `coding` | user-invoked | 开发流程：领取 `docs/todos/` 任务，TDD，跑 QA |
| `audit` | user-invoked | 独立审计：只判 AC，质量问题只记录 |
| `debug` | user-invoked | 难 Bug 的诊断循环：先造出能变红的回路，再谈假设 |

#### 文档写作

| Skill | 触发方式 | 用途 |
|-------|----------|------|
| `docs-maintain` | user-invoked | 维护全部文档的格式、链接、重复与过时内容，含 README 与代码注释 |
| `docs-article` | user-invoked | 长文写作：先散收碎片（explore），再逐段成形（exploit） |
| `docs-pr` | user-invoked | PR 描述：Summary / Evidence / Merge Danger 三段 |
| `docs-adr` | model-invoked | 记录技术决定与取舍 |
| `docs-commit` | model-invoked | 生成 Conventional Commits 格式的提交信息 |
| `docs-docstring` | model-invoked | 默认不写注释，注释只写代码说不出的 |
| `docs-glossary` | model-invoked | 术语当场定、淘汰同义词 |

#### 学习与研究

| Skill | 触发方式 | 用途 |
|-------|----------|------|
| `hackernews-search` | user-invoked | 搜索 HN 帖子、评论与热门 |
| `systematic-learning` | user-invoked | 体系化学习：Feynman technique 搭知识树，输出 Markdown 卡片 |

#### 元技能

| Skill | 触发方式 | 用途 |
|-------|----------|------|
| `create-skills` | user-invoked | 创建或优化 agent skill 的向导 |

### 7.3 选择策略

询问用户需要哪些 skills，再复制安装。

---

## 8. 登录认证

pi 支持多种 provider。认证在交互界面完成：

```bash
pi
# 进入 pi 后输入
/login
```

按提示选择 provider 并完成认证。

常见 provider 的准备工作：

- **Anthropic**：需要 `ANTHROPIC_API_KEY` 环境变量，或通过 `/login` 订阅登录
- **OpenAI**：需要 `OPENAI_API_KEY` 环境变量，或通过 `/login` 订阅登录
- **OpenCode Zen**：需要注册 [opencode.ai](https://opencode.ai) 并获取 API key
- **Google Gemini**：需要 `GEMINI_API_KEY` 环境变量
- 更多 provider 在 pi 中输入 `/login` 查看支持列表

也可在启动前设置环境变量：

```bash
export ANTHROPIC_API_KEY=sk-ant-...
pi
```

---

## 9. 安装后用户需自行配置

下列配置项无法在安装流程中自动完成。agent 安装结束后，逐条告知用户。做法见对应小节，本节只列出清单。

### 必须处理

| # | 配置项 | 位置 | 参见 |
|---|--------|------|------|
| 1 | 搜索 API Key | `~/.pi/agent/pi-web-search-lite/config.json` | 5.2 |
| 2 | Provider 认证、默认模型 | `/login` 或环境变量；`settings.json` | 8、2.1 |

### 推荐处理

| # | 配置项 | 位置 | 参见 |
|---|--------|------|------|
| 3 | pi-blackhole 压缩阈值、worker 模型 | `~/.pi/agent/pi-blackhole/pi-blackhole-config.json` | 5.1 |
| 4 | 每模型思考等级 | `settings.json` → `modelThinkingLevels` | 2.1 |

### 按需处理

| # | 配置项 | 位置 | 参见 |
|---|--------|------|------|
| 5 | `shellPath` | `settings.json` | 1 |
| 6 | AGENTS.md | `~/.pi/agent/AGENTS.md` | 6 |
| 7 | 音效 | `settings.json` → `sounds` | 2.2 |
| 8 | Git Bash Windows 配置 | `~/.gitconfig`、`~/.config/git/attributes`、`~/.bashrc` | 1.1 |
