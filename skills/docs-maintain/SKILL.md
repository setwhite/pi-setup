---
name: docs-maintain
disable-model-invocation: true
description: 维护全部项目文档：格式、链接、重复与过时内容。含 README 与代码注释。
---

# 文档维护

范围是项目里全部文档：`docs/**`、仓库根 `README.md` 等入口文件、代码注释。规则按 `../_shared/docs-rules.md`。

只改文档与注释。代码逻辑不对就记进报告。

## 盘点

1. `fd -e md . docs` 列 `docs/`，没有就跳过这一部分。
2. `fd -e md -d 1 .` 列仓库根 Markdown。`README.md`、`AGENTS.md` 是入口，原地检查，不搬。
3. `rg -n 'TODO|FIXME|XXX|HACK'` 找注释。再查带 `--help` 与配置默认值的模块。

## 直接修

- 放错目录或命名不符的，移到正确位置。
- 链接能打开：相对路径、skill 名、`路径:行号`。
- 移动或合并后，去掉重复的一级标题，补齐跳过的层级。
- 索引和文件双向对得上：不漏文档，不指死文件。
- 注释格式随该语言的既有风格。

## 对代码

每条具体声明都要能打开：路径、符号、命令、默认值存在且相符。术语与 `docs/GLOSSARY.md` 一致。已解决的未决项删掉。

`README.md` 按 `/skill:docs-readme` 的判据检查，命令与代码、`--help` 一致。注释按 `/skill:coding` 的判据检查。

## 先批准

删除、合并、补写、改范围都列清单等用户批准，含整份文档、README 章节、注释块。

## 收口

报告写改了什么、删了什么、没动的和原因。文档与注释分开列。不写入文件。
