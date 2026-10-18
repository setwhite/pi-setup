---
name: docs-spec
disable-model-invocation: true
description: 把已有讨论综合成 spec，写入 docs/specs/。
---

# Spec

不访谈。当前对话与代码库里已有的东西足够写 spec；缺的去读代码，不问用户。

1. 探索仓库：相关模块怎么组织、有没有相关 ADR。全程用 `docs/GLOSSARY.md` 的规范词。
2. 定测试接缝：优先用已有接缝并取最高那层，需要新的就提最高点的方案——接缝越少越好，理想是一个。摊给用户确认。
3. 按 `references/spec-template.md` 写，落盘 `docs/specs/NNNN-slug.md`（编号取最大号加一，第一次用就建目录），补上 README 文档小节那一行。

见 [../_shared/docs-rules.md](../_shared/docs-rules.md)。
