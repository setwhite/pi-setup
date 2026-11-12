---
name: docs-glossary
description: 术语当场定、淘汰同义词。当用户讨论项目术语、命名，或提到「术语」「词汇表」「GLOSSARY」时使用。
---

# GLOSSARY.md

词汇的唯一来源。只放术语定义。

## 当场

- 用户的词与术语表冲突，当场指出：「术语表里 cancellation 指 X，你现在指 Y，哪个对？」
- 词含糊或一词多义，提议一个精确的规范词。
- 用户说某件事怎么运作，去代码里看是否同意。不一致就说出来。
- 一确定就写入，不等累积。

## 布局

单 context 用 `docs/GLOSSARY.md`。多 context 用 `docs/GLOSSARY-MAP.md` 列出各 context 的位置与关系，术语表放 `docs/<context>/GLOSSARY.md`。

```md
## 术语

**Order**:
客户提交的一次购买请求。
_别叫_: Purchase, transaction
```

- 有态度：同一概念有多个词时选最好的一个，其余列进 `_别叫_`。
- 定义一两句封顶。只说什么，不写怎么做。
- 只收这个 context 特有的概念。timeout、错误类型这类通用的不收。
- 天然成组就加小标题。
