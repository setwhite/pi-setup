# pi-setup

[pi](https://github.com/earendil-works/pi) 的安装与配置模板。仓库含全局设置、扩展包配置、AGENTS.md 与可选 skill。

顺序不能颠倒：先放好 `settings.json`，再装 pi。pi 首次启动时按 `settings.json` 的 `packages` 字段自动安装扩展包。

## 1. 前置条件

需要 Node.js 22.19+、Git、bash。版本用 `node -v`、`git --version`、`bash --version` 检查。

Windows 还要 Git Bash 或 WSL。pi 在原生 Windows 上用 Git Bash 跑 `bash` 工具与 `!` 命令。想改用原生 `powershell` 工具，见 pi 文档的 `docs/windows.md`。

pi 找 bash 的顺序：`settings.json` 的 `shellPath` → `%ProgramFiles%\Git\bin\bash.exe` → `%ProgramFiles(x86)%\Git\bin\bash.exe` → PATH 上的 `bash.exe`。已装 Git 却报找不到 bash 时，先 `where bash` 看排在第一个的路径，再把 `C:\Program Files\Git\bin` 提到 PATH 最前，或者直接写死：

```json
"shellPath": "C:\\Program Files\\Git\\bin\\bash.exe"
```

Windows 上顺手把 git 配好：

```bash
git config --global core.autocrlf input    # 仓库统一存 LF
git config --global core.quotepath false   # 中文文件名正常显示
git config --global core.symlinks true     # 认识符号链接
```

老仓库要逐个补 `git config core.symlinks true`。

批处理脚本要走 CRLF，否则 cmd 解析出错。写进全局 attributes：

```bash
mkdir -p ~/.config/git
cat >> ~/.config/git/attributes <<'EOF'
*.bat  text eol=crlf
*.cmd  text eol=crlf
*.ps1  text eol=crlf
EOF
```

要让 `ln -s` 建真符号链接，先开 Windows 开发者模式或以管理员运行。`winsymlinks` 必须是 `MSYS` 的第一项，放后面不生效：

```bash
echo 'export MSYS="winsymlinks:nativestrict${MSYS:+,$MSYS}"' >> ~/.bashrc
```

重开终端生效。

## 2. 安装

### 2.1 克隆仓库

```bash
git clone https://github.com/setwhite/pi-setup.git
cd pi-setup
```

后文命令都在仓库根目录执行。

### 2.2 放好全局设置

```bash
mkdir -p ~/.pi/agent
cp config/settings.json ~/.pi/agent/settings.json
```

要提示音就再复制声音文件，见 3.2。

### 2.3 安装 pi

macOS 与 Linux：

```bash
curl -fsSL https://pi.dev/install.sh | sh
```

Windows：

```powershell
powershell -c "irm https://pi.dev/install.ps1 | iex"
```

npm（需 Node.js 22.19+）：

```bash
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

脚本安装固定依赖版本，npm 安装不固定。

### 2.4 首次启动

```bash
pi
```

首次启动读设置，装 `packages` 里的扩展包，再引导登录。装失败的包打警告跳过，下次启动或 `/reload` 重试。要手动重装，`pi install` 后接 `packages` 里的字符串即可，例如 `pi install npm:pi-blackhole`。

登录就是进 pi 输 `/login` 选 provider。也可以先导出 `ANTHROPIC_API_KEY`、`OPENAI_API_KEY`、`GEMINI_API_KEY` 这类的环境变量，pi 会自己认。

自动装的扩展包：

| 扩展包 | 用途 |
|--------|------|
| [`pi-blackhole`](https://www.npmjs.com/package/pi-blackhole) | 压缩上下文。`/blackhole` 用算法生成摘要代替 `/compact`，不调 LLM。三个后台 worker 沉淀 observation 与 reflection，压缩后 `recall` 取回原文 |
| [`pi-context-view`](https://www.npmjs.com/package/pi-context-view) | `/context usage` 看上下文占用，`/context injections` 看系统提示与各扩展注入了什么 |
| [`pi-browser-use-lite`](https://www.npmjs.com/package/pi-browser-use-lite) | 经由配套浏览器扩展驱动你自己的 Chrome。用于网页测试与自动化 |
| [`pi-copy-button`](https://www.npmjs.com/package/pi-copy-button) | 全屏记录里代码块与引用块右侧加 copy 按钮 |
| [`pi-herdr-subagents-lite`](https://www.npmjs.com/package/pi-herdr-subagents-lite) | subagent 跑在 herdr pane 的独立 pi 进程里。`run` 启动，`send` 续跑，结果异步回传 |
| [`pi-jingle`](https://www.npmjs.com/package/pi-jingle) | 任务完成放提示音 |
| [`@narumitw/pi-btw`](https://www.npmjs.com/package/@narumitw/pi-btw) | `/btw` 临时侧问。默认不写入主会话 |
| [`@narumitw/pi-usage`](https://www.npmjs.com/package/@narumitw/pi-usage) | `/usage` 看账号用量与 DeepSeek 余额，`/fast` 切 Codex Fast |
| [`pi-web-search-lite`](https://www.npmjs.com/package/pi-web-search-lite) | `web_search` 与 `web_fetch`。GitHub 链接走 `gh`，Reddit 链接换成 redlib 域名 |
| [`pi-todo-lite`](https://www.npmjs.com/package/pi-todo-lite) | `todo` 任务表。显示在输入框上方 |
| [`@ssk_dev/rpiv-ask-user-question-lean`](https://www.npmjs.com/package/@ssk_dev/rpiv-ask-user-question-lean) | `ask_user_question` 提问工具。原版的 lean 版，初始化 token 少 83% |

不要的包删掉 `packages` 里那一行：不装音效删 `pi-jingle`，不装浏览器删 `pi-browser-use-lite` 与 `pi-copy-button`，不在 herdr 里跑删 `pi-herdr-subagents-lite`。

lean 版依赖原版包，原版代码随 lean 版自动装。机器上已有原版 `@juicesharp/rpiv-ask-user-question` 时先卸载，两个版本同时加载会重复注册工具：

```bash
pi remove npm:@juicesharp/rpiv-ask-user-question
```

装了独立的 `pi-observational-memory` 或 `pi-vcc` 也要先卸掉，与 `pi-blackhole` 冲突：

```bash
pi remove npm:pi-observational-memory
```

## 3. 配置

### 3.1 settings.json

模板全文如下。配置文件本身是严格 JSON，不能带注释，这里的注释只用来解释字段。

```jsonc
{
  // 给编辑器（VS Code 等）做校验与补全。
  "$schema": "https://pi.dev/schemas/settings.schema.json",

  // 主题。system 跟随终端配色。
  "theme": "dark",

  // 启动模型。安装后填实际值，不填就删掉这三个字段。
  "defaultProvider": "<your-provider>",
  "defaultModel": "<your-default-model>",
  "defaultThinkingLevel": "<your-thinking-level>",

  // 隐藏记录里的思考块，只留最终输出。
  "hideThinkingBlock": true,

  // 新项目的信任策略。always 不询问即信任；ask 逐次询问；never 一律不信任。只在 agent 目录的 settings.json 生效。
  "defaultProjectTrust": "always",

  // 要装的扩展包。pi 首次启动按此安装。手动重装见 2.4。
  "packages": [
    "npm:pi-jingle",
    "npm:@narumitw/pi-btw",
    "npm:@narumitw/pi-usage",
    "npm:pi-context-view",
    "npm:@ssk_dev/rpiv-ask-user-question-lean",
    "npm:pi-web-search-lite",
    "npm:pi-todo-lite",
    "npm:pi-herdr-subagents-lite",
    "npm:pi-copy-button",
    "npm:pi-browser-use-lite",
    "npm:pi-blackhole"
  ],

  // 用终端光标代替 pi 自绘光标。
  "showHardwareCursor": false,

  // Ctrl+P 能切换的模型。留空表示全部可用。格式 provider/model，加 :thinking 后缀可定该模型的思考等级。
  "enabledModels": [],

  // 输入框为空时连按两次 Esc 的动作。tree 打开会话树。
  "doubleEscapeAction": "tree",

  // /tree 的初始过滤。default 全部；no-tools 隐藏工具消息；其余 user-only、labeled-only、all。
  "treeFilterMode": "no-tools",

  // 任务完成时的音效。不要就删掉整个 sounds 块。
  "sounds": {
    "agent_end": "~/.pi/agent/sounds/hey_listen_navi.wav"
  },

  // Mermaid 渲染时机。off 不渲染；final 完成后渲染一次；streaming 边生成边渲染。
  "markdown": {
    "mermaid": "streaming"
  },

  // TUI 模式。fullscreen 全屏；regular 常规滚动。也能在 /settings 改。
  "tuiMode": "fullscreen",

  // 输入框水平内边距，取值 0-3。
  "editorPaddingX": 0,

  // 按模型设启动思考等级，键为 provider/modelId。也能在 /settings 改。
  "modelThinkingLevels": {},

  // 自动压缩。enabled 是总开关；reserveTokens 预留回复 token（16384）；keepRecentTokens 保留最近 token（20000）；modelOverrides 按模型覆盖。
  "compaction": {
    "enabled": true
  },

  // 补全下拉可见条数，取值 3-20。
  "autocompleteMaxVisible": 5,

  // 退出全屏打印什么。transcript 打完整记录；resume-hint 打恢复提示。
  "fullscreenExitOutput": "transcript",

  // 全屏滚动条。auto、always、hidden。
  "fullscreenScrollbar": "hidden",

  // 全屏下选中即复制。
  "fullscreenCopyOnSelect": false,

  // 全屏滚轮每格行数。auto 自适应，也可取 1-100。
  "fullscreenWheelScrollLines": "auto",

  // codemode 呈现方式。on 时其他工具照常声明给模型；only 时内置与扩展工具全部隐藏，模型只能经脚本调用。
  // inlineBudget 是声明预算，默认 3000。内置扩展 mcp、llama.cpp、codemode、tool-search 默认加载，用 -builtin:<name> 关掉。
  "codemode": {
    "mode": "only"
  },

  // 启动时启用的工具。+name 加，-name 减。默认 read、bash、edit、write；+codemode 打开 codemode 脚本。
  "defaultTools": [
    "+codemode"
  ],

  // 明显缓存未命中、保温成功、压缩用量、provider 恢复时给提示。
  "showCacheMissNotices": true,

  // 更新后显示精简 changelog，扩展包压成每包一行。
  "collapseChangelog": true,

  // true 隐藏启动头与资源列表；header 只隐藏模型范围行与资源列表。
  "quietStartup": false
}
```

字段没有合适的值就删掉，pi 用内置默认值。三个模型字段不填，首次启动会引导选择。

字段全表与取值见 pi 文档：<https://pi.dev/docs>。

### 3.2 音效（可选）

```bash
mkdir -p ~/.pi/agent/sounds
cp config/sounds/hey_listen_navi.wav ~/.pi/agent/sounds/
```

不要提示音就跳过这步，删掉 `settings.json` 里的 `sounds` 字段。

### 3.3 pi-blackhole

配置文件在 `~/.pi/agent/pi-blackhole/pi-blackhole-config.json`。pi-blackhole 首次加载时按默认值生成，不用手工建。

日常调节用 `/blackhole settings`：压缩模式、阈值、记忆开关都在面板里，保存即生效。worker 模型不在面板里，只能改配置文件。

```bash
mkdir -p ~/.pi/agent/pi-blackhole
cp config/pi-blackhole/pi-blackhole-config.json ~/.pi/agent/pi-blackhole/
```

模板里的 provider 与模型 id 都是占位符，换成你自己的。worker 用一个便宜的小模型就够。字段含义与默认值见 [`pi-blackhole`](https://www.npmjs.com/package/pi-blackhole)。

### 3.4 pi-web-search-lite

```bash
mkdir -p ~/.pi/agent/pi-web-search-lite
cp config/pi-web-search-lite/config.json ~/.pi/agent/pi-web-search-lite/
```

模板里的 API key 全换成占位符。字段含义见 [`pi-web-search-lite`](https://www.npmjs.com/package/pi-web-search-lite)。

API key 在 exa.ai、jina.ai、tavily.com、firecrawl.dev、brave.com/search/api、perplexity.ai 申请。也可以用环境变量，形如 `EXA_API_KEY`，环境变量优先。

GitHub 链接默认交给 `gh`，先 `gh auth login`。不想走 gh 就把 `handlers.github.enabled` 设为 `false`。

### 3.5 pi-herdr-subagents-lite

把 subagent 放到 herdr pane 里跑，每个 subagent 是独立 pi 进程。需要本机装好 herdr，且 pi 本身在 herdr pane 内运行，否则调用报 `not_in_herdr`。测试过 herdr 0.9.5 与 pi 1.4.0。

安装时不能加 `-l`。`-l` 只写项目级设置，子进程换个工作区就读不到这个包：

```bash
pi install npm:pi-herdr-subagents-lite
```

配置文件在 `~/.pi/agent/pi-herdr-subagents-lite/config.json`，不建就用默认值。

profile 放在 `~/.pi/agent/pi-herdr-subagents-lite/profiles/`，只读该目录下的 `*.md`。自带示例在 `examples/` 里，扩展每次加载都会重置 `examples/`，所以要把示例复制到上一层。新机器上 `examples/` 由扩展加载时生成，先启动一次 pi 或 `/reload`：

```bash
cd ~/.pi/agent/pi-herdr-subagents-lite/profiles && cp examples/worker.md worker.md
```

## 4. AGENTS.md 与 skill

### 4.1 AGENTS.md

```bash
cp config/AGENTS.md ~/.pi/agent/AGENTS.md
```

内容是中文编程规范：回复文风、文档文风、决策顺序、工程要求、授权边界、工具约定。细则看 `config/AGENTS.md`，本节不重复。不要就跳过。只给单个项目写指令时，把 `AGENTS.md` 放在项目根，pi 从工作目录向上逐级读。

### 4.2 skill

每个 skill 是一个目录，目录里必须有 `SKILL.md`，可以带 `scripts/`、`references/`。复制需要的目录到 `~/.pi/agent/skills/`：

```bash
mkdir -p ~/.pi/agent/skills
cp -r skills/plan ~/.pi/agent/skills/
cp -r skills/_shared ~/.pi/agent/skills/   # 多数 skill 会读 ../_shared/*.md
```

`_shared/` 没有 `SKILL.md`，不是 skill。里面放共用规则文件，`arch`、`audit`、`plan`、`docs-maintain` 都引用。漏复制就读不到。

`mineru-ocr` 还要 API token：在 mineru.net 申请，写进 `~/.pi/agent/skills/mineru-ocr/token.txt`。

| 分类 | skill | 触发 | 用途 |
|------|-------|------|------|
| 开发流程 | `plan` | 手动 | 问清需求，把选型与取舍写成决策记录 |
| 开发流程 | `research` | 手动 | 找外部事实、比较选型，写 `docs/research/` |
| 开发流程 | `spec` | 手动 | 写本轮 spec：契约与可证伪的验收标准 |
| 开发流程 | `todo` | 手动 | 把 spec 拆成单次会话能做完的任务 |
| 开发流程 | `arch` | 手动 | 维护 ARCHITECTURE.md 与模块边界 |
| 开发流程 | `coding` | 手动 | 领任务，红绿 TDD，收工前跑 QA。含难 Bug 的复现 |
| 开发流程 | `audit` | 手动 | 独立审计：只判 AC，质量问题只记录 |
| 文档写作 | `docs-maintain` | 手动 | 维护全部文档：格式、链接、重复、过时 |
| 文档写作 | `docs-readme` | 手动 | 写仓库根 README：安装、配置、索引 |
| 文档写作 | `docs-article` | 手动 | 写长文：先散收素材，再逐段成形 |
| 文档写作 | `docs-pr` | 手动 | PR 描述：Summary / Evidence / Merge Danger |
| 文档写作 | `docs-commit` | 模型 | 写 Conventional Commits 提交信息 |
| 文档写作 | `docs-glossary` | 模型 | 当场定术语，淘汰同义词 |
| 学习研究 | `systematic-learning` | 手动 | 体系化学习，输出 Markdown 知识卡片 |
| 学习研究 | `mineru-ocr` | 模型 | PDF、Office 文档、图片转 Markdown |
| 元技能 | `create-skills` | 手动 | 创建或优化 skill 的向导 |

触发方式：手动是 `SKILL.md` 写了 `disable-model-invocation: true`，只能显式调用；模型是对话中自动加载。

## 5. 校验、升级、卸载

装完先在系统 shell 里核对：

```bash
pi --version   # 有版本号
pi list        # 列出 packages 里的包
```

再进 pi 跑两条：

```
!printf 'Bash is working\n'   # 能输出说明 bash 工具通了
/reload                       # 重载配置，重试装失败的包
```

日常维护：

```bash
pi update --all          # 更新 pi 与全部扩展包
pi update                # 只更新 pi
pi update --extensions   # 只更新扩展包
pi update --models       # 刷新模型目录
pi remove <source>       # 卸载，同时清掉 settings.json 里的条目
```

`pi uninstall` 是 `pi remove` 的别名，`pi update --self` 是 `pi update` 的别名。

## 6. 装完之后还要自己做

下列事项脚本搞不定，装完逐条处理：

| 优先级 | 事项 | 位置 | 见 |
|--------|------|------|----|
| 必须 | 登录或填 API key，设默认模型 | `/login` 或环境变量；`~/.pi/agent/settings.json` | 2.4、3.1 |
| 必须 | 搜索 API key | `~/.pi/agent/pi-web-search-lite/config.json` | 3.4 |
| 必须 | MinerU API token（装了 `mineru-ocr` 才算） | `~/.pi/agent/skills/mineru-ocr/token.txt` | 4.2 |
| 推荐 | pi-blackhole 阈值与 worker 模型 | `~/.pi/agent/pi-blackhole/pi-blackhole-config.json` | 3.3 |
| 推荐 | 按模型设思考等级 | `~/.pi/agent/settings.json` 的 `modelThinkingLevels` 字段 | 3.1 |
| 可选 | `shellPath` | `~/.pi/agent/settings.json` | 1 |
| 可选 | AGENTS.md | `~/.pi/agent/AGENTS.md` | 4.1 |
| 可选 | 提示音 | `~/.pi/agent/settings.json` 的 `sounds` 字段 | 3.2 |
