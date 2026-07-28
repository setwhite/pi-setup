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

**Windows 用户请注意**：pi 在 Windows 上需要 Git Bash 或 WSL 环境，不要使用 PowerShell 或 CMD。pi 安装完成后，可直接问 pi 如何配置 Windows 环境。

> **agent 注意——Windows bash 检测异常处理**：pi 按以下顺序查找 bash：
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

`config/settings.json` 中各字段含义：

**agent 注意**：以下字段可能需要根据用户情况调整：

| 字段 | 默认值 | 何时调整 |
|------|--------|----------|
| `workspaceHistory.storageDir` | `.pi-history` | 工作区历史存储目录。默认为工作路径下的相对目录 `.pi-history`，可改为绝对路径 |
| `observational-memory.model` | 无 | 如果用户使用的 provider 支持 reasoning，填写实际的 provider 和 model |
| `sounds.agent_end` | `~/.pi/agent/sounds/hey_listen_navi.wav` | 音效文件路径；如果不需要音效，注释掉整个 `sounds` 块 |

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
pi install npm:pi-workspace-history
pi install npm:pi-context-usage
pi install npm:pi-chrome
pi install npm:pi-jingle
pi install npm:@tifan/pi-preferred-thinking
pi install npm:@narumitw/pi-btw
pi install npm:@juicesharp/rpiv-web-tools
pi install npm:@juicesharp/rpiv-ask-user-question
pi install npm:pi-rtk-optimizer
```

### 4.1 各扩展包的作用

| 扩展包 | 作用 |
|--------|------|
| `@ff-labs/pi-fff` | 替换 pi 内置工具为优化版本 |
| `pi-observational-memory` | 自动压缩长对话历史，保留关键信息 |
| `pi-workspace-history` | 记录各项目的会话历史，支持 `/resume` 恢复 |
| `pi-context-usage` | 在页脚显示上下文使用量 |
| `pi-chrome` | Chrome 浏览器集成，用于网页测试和自动化 |
| `pi-jingle` | agent 完成工作时播放提示音 |
| `@tifan/pi-preferred-thinking` | 为不同模型预设思考等级 |
| `@narumitw/pi-btw` | agent 等待期间显示动画 |
| `@juicesharp/rpiv-web-tools` | 提供 `web_search` 和 `web_fetch` 工具 |
| `@juicesharp/rpiv-ask-user-question` | 提供 `ask_user_question` 工具，向用户提问 |
| `pi-rtk-optimizer` | 压缩工具输出，减少 token 消耗 |

**agent 注意**：默认全装。仅以下两种情况需要去掉对应扩展：

| 场景 | 操作 |
|------|------|
| 不需要音效 | 去掉 `pi-jingle` |
| 不需要浏览器集成 | 去掉 `pi-chrome` |

---

## 5. 配置扩展

部分扩展有独立的配置文件，需要复制到位。

### 5.1 pi-preferred-thinking

为不同模型设置默认思考等级：

```bash
mkdir -p ~/.pi/agent/extensions
cp config/extensions/pi-preferred-thinking.json ~/.pi/agent/extensions/pi-preferred-thinking.json
```

**agent 注意**：此配置文件中的模型列表基于 opencode-go provider。如果用户使用其他 provider（如 Anthropic、OpenAI），需要据此调整模型 ID。格式为 `provider/model` 映射到 thinking level（`off`/`low`/`medium`/`high`/`max`）。

### 5.2 pi-rtk-optimizer

上下文/Token 优化器：

```bash
mkdir -p ~/.pi/agent/extensions/pi-rtk-optimizer
cp config/extensions/pi-rtk-optimizer/config.json ~/.pi/agent/extensions/pi-rtk-optimizer/config.json
```

**agent 注意**：`pi-rtk-optimizer` 依赖 `rtk` 二进制，无法通过 npm 安装。需从 GitHub Releases 下载：

- 下载地址：[rtk releases](https://github.com/rtk-ai/rtk/releases)（找最新版本，下载 Windows 版 `rtk.exe`）
- 放置路径：`~/.local/bin/rtk.exe`（即 `%USERPROFILE%\.local\bin\rtk.exe`）
- 确保 `~/.local/bin` 在系统 PATH 中（`where rtk` 能找到即为成功）

### 5.3 pi-fff

**agent 注意**：安装 `@ff-labs/pi-fff` 后，告知用户设置环境变量 `PI_FFF_MODE=override`，并说明这是推荐做法。

### 5.4 rpiv-web-tools

Web 搜索工具配置。复制到 `~/.config/rpiv-web-tools/config.json`：

```bash
mkdir -p ~/.config/rpiv-web-tools
cp config/rpiv-web-tools/config.json ~/.config/rpiv-web-tools/config.json
```

**agent 注意**：此文件中的 `apiKeys` 字段为占位符。用户需要将 Exa 的 API key 填入。注册地址：https://exa.ai

---

## 6. 安装 AGENTS.md

AGENTS.md 是 pi 启动时加载的全局项目指令。复制到全局位置：

```bash
cp config/AGENTS.md ~/.pi/agent/AGENTS.md
```

**内容概要**：中文编程规范——包含环境约束（bash、uv）、中文注释要求、类型标注、函数长度/文件长度/嵌套深度/参数数量/圈复杂度等代码格式限制，以及死代码清理原则。

**agent 注意**：如果用户的项目不需要中文规范，可以跳过此步骤，或在项目目录下另行创建 `.pi/AGENTS.md`。

---

## 7. 安装 Skills（按需选择）

Skills 是 pi 的按需能力包，放在 `~/.pi/agent/skills/` 下即可被 pi 发现。

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
| `commit-style` | model-invoked | 生成 Conventional Commits 格式的提交信息 |
| `create-skills` | user-invoked | 创建或优化 agent skill 的向导 |
| `grilling` | user-invoked | 对方案/决策进行追问式审查 |

#### 学习与研究

| Skill | 触发方式 | 用途 |
|-------|----------|------|
| `systematic-learning` | user-invoked | 费曼式体系化学习，输出 HTML 知识卡片 |
| `prior-research` | user-invoked | 术语映射与方案调研 |
| `hackernews-search` | user-invoked | 搜索 HN 帖子与热门 |

#### 内容创作

| Skill | 触发方式 | 用途 |
|-------|----------|------|
| `article-writing` | user-invoked | 结构化技术文章写作 |
| `prose-style` | user-invoked | 技术写作风格参考（被其他 skill 引用） |
| `html-card` | user-invoked | 生成自包含 HTML 卡片（被其他 skill 引用） |

#### 中文社区

| Skill | 触发方式 | 用途 |
|-------|----------|------|
| `zhihu-search` | user-invoked | 搜索知乎站内内容（需 `ZHIHU_ACCESS_SECRET` 环境变量） |

### 7.3 选择策略

**agent 注意**：询问用户需要哪些 skills，按需复制安装。

---

## 8. 登录认证

pi 支持多种 provider。让用户在 pi 交互界面中登录：

```bash
pi
# 进入 pi 后输入
/login
```

然后根据提示选择 provider 并完成认证。

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
