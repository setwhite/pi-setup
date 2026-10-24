---
name: docs-maintain
disable-model-invocation: true
description: 核查并修复项目文档：格式、链接、重复、过时内容。
---

# 文档维护

读 `../_shared/docs-rules.md`。只改文档，不改代码。

## Step 1 — 盘点

1. `fd -e md . docs` 列全部文件；`docs/` 不存在就停，报告没有可维护的文档。
2. 按目录分类：specs、adr、decisions、research、modules、todos、audit，加上 `GLOSSARY.md`、`ARCHITECTURE.md`。
3. 记下每份的路径、编号、README 索引里有没有它。认不出的也列出来，不猜用途。

**Completion criterion**：每份文档都有类别；编号现状与索引缺口清楚。

## Step 2 — 格式

按「位置」核，能直接修的当场修。

- 放错目录或命名不符的，移到正确位置并改文件名。
- 编号不重复；缺号不补，不重排。
- 链接能打开：相对路径、`/skill:xxx`、`路径:行号`。
- 标题：一份一个 `#`，层级不跳。
- 索引与文件对得上；死链删掉。
- 只有标题没有正文的，列进 Step 4。

**Completion criterion**：机械问题已修，修不了的进了处置清单。

## Step 3 — 内容

先按「归属」表逐行核：每个载体有没有写不属于它的事实，同一事实有没有第二个副本。

再逐条对照代码，每条具体声明都要能打开：

- 路径、符号、命令、默认值：存在且相符。
- 术语：与 `docs/GLOSSARY.md` 一致。
- 状态：todos 复选框、阶段表区间、audit 报告三者对得上。
- 未决：已解决的已删。
- 缺失：有模块没文档，有决策没记录。

**Completion criterion**：每条 finding 写成 `文件:行号 — 观察 — 依据`，依据指到代码或 `../_shared/docs-rules.md`。

## Step 4 — 处置

- 机械问题：Step 2 已改。
- 确定错误：代码为准，直接改文档。
- 删除、合并、补写、改范围：列清单，等用户批。

**Completion criterion**：所有删除与合并都获批；没批的留在清单里。

## Step 5 — 收口

- 索引、阶段表、模块表跟上改动。
- 报告：改了什么、删了什么、没动的和原因。不落盘。

**Completion criterion**：文档与代码一致，索引无死链。
