---
name: docs-glossary
description: 领域术语管理。当用户讨论项目领域术语、概念定义或更新 GLOSSARY 时使用。
---

# GLOSSARY

Ubiquitous Language：项目领域词汇的唯一来源（SSOT），只放术语定义，不放实现细节、spec 或草稿。

- 当场校准：用词与术语表冲突、含糊或与代码不一致时当场指出并提议规范词，敲定立刻写入。
- Scenario & Code Check：讨论概念关系时举边界例子（如整单取消 vs 部分取消）说清边界，并对照代码核实口头定义与实现是否矛盾。
- Bounded Context：单业务域用 `docs/GLOSSARY.md`；多业务域用 `docs/GLOSSARY-MAP.md` 声明关系，各自放 `docs/<context>/GLOSSARY.md`。
- Opinionated：同一概念选最佳规范词，淘汰同义词记「别叫」；定义 1 到 2 句只说是什么，不收 timeout、error 等通用词。

```md
Order
客户提交的一次购买请求。
别叫：Purchase、transaction
```
