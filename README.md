# pi-setup：pi coding agent 安装与配置指南

> **目标读者**：AI coding agent（以及想手动操作的人类）。
>
> 本仓库是 [pi](https://github.com/earendil-works/pi) 的一套配置方案，包含本体配置、扩展包和可选 skills。agent 阅读本文档后，逐步骤执行安装与配置。

---

## 1. 前置条件

确认以下环境已就绪：

| 依赖 | 检查命令 | 最低版本 |
|------|----------|----------|
| Node.js | `node -v` | ≥ 18 |
| npm | `npm -v` | ≥ 9 |
| Git | `git --version` | ≥ 2.30 |
| Bash | `bash --version` | 任意（Windows 需 Git Bash 或 WSL） |

**Windows**：pi 需要 Git Bash 或 WSL，不支持 PowerShell 和 CMD。安装完成后可直接向 pi 询问 Windows 环境配置。

> **bash 查找顺序与异常处理**：pi 按以下顺序查找 bash：
> 1. `~/.pi/agent/settings.json` 中 `shellPath` 指定的路径
> 2. `C:\Program Files\Git\bin\bash.exe`（Git Bash）
> 3. PATH 中的 `bash.exe`（可能是 Cygwin、MSYS2、WSL 等）
>
> 如果用户安装了 Git 但 pi 报错找不到 bash，或找到了错误的 bash：
> - 检查 `where bash` 的输出，确认排在第一位的 bash 路径
> - 如果 Git Bash 不在 PATH 最前面，编辑系统环境变量，把 `C:\Program Files\Git\bin` 移到最前面
> - 或者直接在 `~/.pi/agent/settings.json` 中设置 `"shellPath": "C:\\Program Files\\Git\\bin\\bash.exe"` 强制指定

---

## 2. 配置 pi 本体

pi 的全局配置位于 `~/.pi/agent/settings.json`。先将本仓库的 `config/settings.json` 复制到该路径：

```bash
mkdir -p ~/.pi/agent
cp config/settings.json ~/.pi/agent/settings.json
```

### 2.1 配置项说明

`config/settings.json` 中各字段含义，按需调整：

| 字段 | 默认值 | 何时调整 |
|------|--------|----------|
| `defaultProvider` / `defaultModel` / `defaultThinkingLevel` | 占位符（必填） | 默认模型配置。安装后必须填写实际 provider / 模型 / 思考等级，否则删除这三个字段，让 pi 首次启动引导选择 |
| `modelThinkingLevels` | 无 | 按模型固定启动思考等级，key 为 `provider/modelId`，value 为 `off`/`minimal`/`low`/`medium`/`high`/`xhigh`/`max`。在 `/settings` → Default thinking level per model 中设置，或手写进 `settings.json` |
| `enabledModels` | 空数组 | Ctrl+P 切换模型的候选列表，格式 `provider/model`（可加 `:thinking` 后缀指定该模型的思考等级，如 `opencode-go/model:high`），按用户可用模型填写 |
| `observational-memory.compactAfterTokensMode` | `calibrated` | memory 压缩阈值模式：`ratio` 按当前模型 contextWindow × `compactAfterTokensRatio` 触发压缩；`calibrated` 则使用固定 token 数（`compactAfterTokens`） |
| `observational-memory.compactAfterTokens` | `81000` | `calibrated` 模式下的固定压缩阈值（token 数），按模型 contextWindow 自行估算 |
| `observational-memory.compactAfterTokensRatio` | 无 | `ratio` 模式下的压缩触发比例；改用 `ratio` 模式时填写（如 `0.5`） |
| `observational-memory.model` | 无 | 指定 memory 专用模型（observer/reflector/dropper），用便宜模型降低 token 消耗（如 opencode-go 的 `deepseek-v4-flash`、openai 的 `gpt-4o-mini`）；不填则复用当前会话模型 |
| `sounds.agent_end` | `~/.pi/agent/sounds/hey_listen_navi.wav` | 音效文件路径；如果不需要音效，注释掉整个 `sounds` 块 |
| `markdown.mermaid` | `streaming` | Mermaid 图表渲染模式：`off` 不渲染、`final` 完成后一次性渲染、`streaming` 边生成边渲染 |
| `tuiMode` | `regular` | TUI 模式：`regular` 常规，或实验性 `fullscreen`；`/settings` 中修改立即生效 |
| `editorPaddingX` | `0` | 输入编辑器水平内边距（0-3），数值越大输入框左右留白越多 |

### 2.2 音效文件（可选）

将音效文件复制到 pi 的 sounds 目录：

```bash
mkdir -p ~/.pi/agent/sounds
cp config/sounds/hey_listen_navi.wav ~/.pi/agent/sounds/hey_listen_navi.wav
```

如果不需要音效，跳过此步骤并在 `~/.pi/agent/settings.json` 中注释掉 `sounds` 块。

---

## 3. 安装 pi

执行以下任一命令安装 pi：

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

应输出版本号。pi 首次启动时会根据 `settings.json` 中的 `packages` 字段自动安装扩展包。

---

## 4. 安装扩展包

如果上一步自动安装未触发，手动安装：

```bash
pi install npm:@ff-labs/pi-fff
pi install npm:pi-observational-memory
pi install npm:pi-context-usage
pi install npm:pi-chrome
pi install npm:pi-jingle
pi install npm:@narumitw/pi-btw
pi install npm:@juicesharp/rpiv-web-tools
pi install npm:@juicesharp/rpiv-ask-user-question
pi install npm:pi-rtk-optimizer
pi install npm:pi-workspace-history
```

### 4.1 各扩展包的作用

| 扩展包 | 作用 |
|--------|------|
| [`@ff-labs/pi-fff`](https://www.npmjs.com/package/@ff-labs/pi-fff) | 替换内置 find/grep，按 frecency 排序、git-aware |
| [`pi-observational-memory`](https://www.npmjs.com/package/pi-observational-memory) | 将长对话历史压缩为 observation/reflection 条目，原文用 `recall(<id>)` 取回 |
| [`pi-context-usage`](https://www.npmjs.com/package/pi-context-usage) | 在页脚显示上下文使用量 |
| [`pi-chrome`](https://www.npmjs.com/package/pi-chrome) | Chrome 浏览器集成，用于网页测试和自动化 |
| [`pi-jingle`](https://www.npmjs.com/package/pi-jingle) | agent 完成工作时播放提示音 |
| [`@narumitw/pi-btw`](https://www.npmjs.com/package/@narumitw/pi-btw) | agent 等待期间显示动画 |
| [`@juicesharp/rpiv-web-tools`](https://www.npmjs.com/package/@juicesharp/rpiv-web-tools) | 提供 `web_search` 和 `web_fetch` 工具 |
| [`@juicesharp/rpiv-ask-user-question`](https://www.npmjs.com/package/@juicesharp/rpiv-ask-user-question) | 提供 `ask_user_question` 工具，向用户提问 |
| [`pi-rtk-optimizer`](https://www.npmjs.com/package/pi-rtk-optimizer) | 压缩工具输出，减少 token 消耗 |
| [`pi-workspace-history`](https://www.npmjs.com/package/pi-workspace-history) | 工作区级 undo/redo（`/undo`、`/redo`、`/tree` 时间机器），恢复聊天历史节点对应的真实文件状态 |

默认全装。仅两种场景需要去掉对应扩展：

| 场景 | 操作 |
|------|------|
| 不需要音效 | 去掉 `pi-jingle` |
| 不需要浏览器集成 | 去掉 `pi-chrome` |

---

## 5. 配置扩展

部分扩展有独立的配置文件，需要复制到位。

### 5.1 pi-rtk-optimizer

```bash
mkdir -p ~/.pi/agent/extensions/pi-rtk-optimizer
cp config/extensions/pi-rtk-optimizer/config.json ~/.pi/agent/extensions/pi-rtk-optimizer/config.json
```

`pi-rtk-optimizer` 依赖 `rtk` 二进制，无法通过 npm 安装。需从 GitHub Releases 下载：

- 下载地址：[rtk releases](https://github.com/rtk-ai/rtk/releases)（找最新版本，下载 Windows 版 `rtk.exe`）
- 放置路径：`~/.local/bin/rtk.exe`（即 `%USERPROFILE%\.local\bin\rtk.exe`）
- 确保 `~/.local/bin` 在系统 PATH 中（`where rtk` 能找到即为成功）

### 5.2 pi-fff

安装 `@ff-labs/pi-fff` 后，设置环境变量 `PI_FFF_MODE=override`，FFF 完全替换内置 find/grep。

### 5.3 rpiv-web-tools

配置文件复制到 `~/.config/rpiv-web-tools/config.json`：

```bash
mkdir -p ~/.config/rpiv-web-tools
cp config/rpiv-web-tools/config.json ~/.config/rpiv-web-tools/config.json
```

此文件中的 `apiKeys` 字段为占位符。`web_search` 支持多个搜索 provider（exa、jina、tavily、firecrawl 等），至少填一个 key 即可使用，推荐 exa；`provider` 字段指定当前激活的搜索后端。注册地址：https://exa.ai、https://jina.ai、https://tavily.com、https://firecrawl.dev

---

## 6. 安装 AGENTS.md

AGENTS.md 是 pi 启动时加载的全局项目指令。复制到全局位置：

```bash
cp config/AGENTS.md ~/.pi/agent/AGENTS.md
```

**内容概要**：中文编程规范——包含环境约定（bash、uv、pnpm、ruff、basedpyright）、语言与文风约束（中文注释、禁止套话）、工程原则、工作流程（需求不明先读代码再问用户），以及未经确认不 commit / 改依赖 / 破坏性操作的硬约束。TDD、lint + test、模块结构与代码风格由第 7 节的 `coding` skill 提供。

不需要中文规范的项目可跳过此步骤，或在项目目录下另行创建 `.pi/AGENTS.md`。

---

## 7. 安装 Skills（按需选择）

Skills 是 pi 的按需能力包，放在 `~/.pi/agent/skills/` 下即可被 pi 发现。写作类 skill（`article-writing`、`systematic-learning`）的文风规则由第 6 节 AGENTS.md 的「语言约束」提供。

### 7.1 安装方法

每个 skill 是一个目录，包含 `SKILL.md`（以及可选的 `scripts/`）。将需要的 skill 目录复制到 `~/.pi/agent/skills/`：

```bash
mkdir -p ~/.pi/agent/skills
cp -r skills/<skill-name> ~/.pi/agent/skills/
```

### 7.2 Skills 分类

#### 编程通用

| Skill | 触发方式 | 用途 |
|-------|----------|------|
| `plan` | user-invoked | 联网调研、追问至共识，产出 `PLAN.md`、`ARCHITECTURE.md`、`TODO.md` |
| `coding` | user-invoked | 领任务、红/绿 TDD、lint + test、模块与代码风格 |
| `audit` | user-invoked | 新会话独立审计：机器门槛、验收标准与仓库规范两轴核查 |
| `commit-style` | model-invoked | 生成 Conventional Commits 格式的提交信息 |
| `create-skills` | user-invoked | 创建或优化 agent skill 的向导 |

#### 学习与研究

| Skill | 触发方式 | 用途 |
|-------|----------|------|
| `systematic-learning` | user-invoked | 费曼式体系化学习，输出 HTML 知识卡片 |
| `hackernews-search` | user-invoked | 搜索 HN 帖子与热门 |

#### 内容创作

| Skill | 触发方式 | 用途 |
|-------|----------|------|
| `article-writing` | user-invoked | 结构化技术文章写作 |
| `html-card` | user-invoked | 生成自包含 HTML 卡片（被其他 skill 引用） |

### 7.3 选择策略

询问用户需要哪些 skills，按需复制安装。

---

## 8. 登录认证

pi 支持多种 provider，认证在交互界面完成：

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

安装流程无法自动完成的配置项，agent 安装结束后逐条告知用户。具体做法见对应小节，本节只做清单。

### 必须处理

| # | 配置项 | 位置 | 参见 |
|---|--------|------|------|
| 1 | 搜索 API Key | `~/.config/rpiv-web-tools/config.json` | 5.3 |
| 2 | Provider 认证、默认模型 | `/login` 或环境变量；`settings.json` | 8、2.1 |
| 3 | memory 专用模型 | `settings.json` → `observational-memory.model` | 2.1 |

### 推荐处理

| # | 配置项 | 位置 | 参见 |
|---|--------|------|------|
| 4 | `PI_FFF_MODE=override` | 环境变量 | 5.2 |
| 5 | `rtk.exe` | `~/.local/bin/rtk.exe` + PATH | 5.1 |
| 6 | 每模型思考等级 | `settings.json` → `modelThinkingLevels` | 2.1 |

### 按需处理

| # | 配置项 | 位置 | 参见 |
|---|--------|------|------|
| 7 | `shellPath` | `settings.json` | 1 |
| 8 | AGENTS.md | `~/.pi/agent/AGENTS.md` | 6 |
| 9 | 音效 | `settings.json` → `sounds` | 2.2 |
