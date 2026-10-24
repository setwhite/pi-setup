---
name: docs-maintain
disable-model-invocation: true
description: 维护项目全部文档的格式、链接、重复与过时内容，含仓库 README 与代码注释。
---

# 文档维护

读 `../_shared/docs-rules.md`。范围是项目里全部文档：`docs/**`、仓库根 `README.md` 等入口文件、代码注释。注释判据见 `../docs-docstring/SKILL.md`。

只改文档与注释。代码逻辑不对，记进报告，不动。

## Step 1 — 盘点

1. `fd -e md . docs` 列 `docs/`；缺失就跳过这一部分，不中止。
2. `fd -e md -d 1 .` 列仓库根 Markdown。`README.md`、`AGENTS.md` 是入口，不搬，只在原地核。
3. `rg -n 'TODO|FIXME|XXX|HACK'` 起步找注释；再核带 `--help` 与配置默认值的模块。
4. 分类：specs、adr、decisions、research、modules、todos、audit、`GLOSSARY.md`、`ARCHITECTURE.md`、根入口、注释所在模块。认不出的列出来，不猜用途。

**Completion criterion**：每份文档、每处待核注释都有类别；编号现状与索引缺口清楚。

## Step 2 — 格式

按「位置」核，能直接修的当场修。

- `docs/` 内放错目录或命名不符的，移到正确位置并改文件名。根 `README.md`、`AGENTS.md` 不搬。
- 编号不重复；缺号不补，不重排。
- 链接能打开：相对路径、`/skill:xxx`、`路径:行号`。
- 标题：一份一个 `#`，层级不跳。
- 索引与文件对得上；死链删掉。README「文档」小节每行指到存在的文件。
- 注释格式随该语言既有风格。
- 只有标题没有正文的，列进 Step 4。

**Completion criterion**：机械问题已修，修不了的进了处置清单。

## Step 3 — 内容

先按「归属」表逐行核：每个载体有没有写不属于它的事实，同一事实有没有第二个副本。

再逐条对照代码，每条具体声明都要能打开：

- 路径、符号、命令、默认值：存在且相符。
- 根 `README.md`：安装、用法、命令与代码和 `--help` 一致；不复制 `docs/` 的内容，重复的删一处，留指针。
- 术语：与 `docs/GLOSSARY.md` 一致。
- 状态：todos 复选框、阶段表区间、audit 报告三者对得上。
- 未决：已解决的已删。
- 缺失：有模块没文档、有决策没记录、有口头约定没落在代码旁。
- 注释：复述代码的、与实现不符的、TODO 型的，按 `../docs-docstring/SKILL.md` 判据核。文字与代码冲突时改文字。

**Completion criterion**：每条 finding 写成 `文件:行号 — 观察 — 依据`，依据指到代码或 `../_shared/docs-rules.md`。

## Step 4 — 处置

- 机械问题：Step 2 已改。
- 确定错误：代码为准，直接改文档与注释。
- 删除、合并、补写、改范围：列清单，等用户批。含整份文档、README 章节、注释块。
- 代码缺陷：写进报告，不动代码。

**Completion criterion**：所有删除与合并都获批；没批的留在清单里。

## Step 5 — 收口

- 索引、阶段表、模块表、README 跟上改动。
- 报告：改了什么、删了什么、没动的和原因，文档与注释分开列。不落盘。

**Completion criterion**：文档、注释与代码一致，索引无死链。
