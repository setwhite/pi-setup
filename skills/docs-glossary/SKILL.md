---
name: docs-glossary
description: 领域术语管理。当用户讨论项目领域术语、概念定义或更新 GLOSSARY 时使用。
---

# GLOSSARY

Ubiquitous Language：领域词汇的唯一来源（SSOT），只放术语定义。

- 当场校准：用户用词与术语表冲突、含糊或与代码不符时，当场指出并提议规范词；敲定即写入，不等累积。
- Bounded Context：单 context 用 `docs/GLOSSARY.md`；多 context 用 `docs/GLOSSARY-MAP.md` 声明关系，各自放 `docs/<context>/GLOSSARY.md`。
- Opinionated：同一概念选最佳规范词，淘汰同义词记在「别叫」里；定义 1 到 2 句，只写是什么，不收 timeout、error 等通用词。

```md
Order
客户提交的一次购买请求。
别叫：Purchase、transaction
```
