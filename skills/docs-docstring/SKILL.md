---
name: docs-docstring
description: 注释讲 why，Docstring 给契约。当用户要求写或改注释、Docstring，或提到「注释」「docstring」时使用。
---

# 注释与 Docstring

## 注释

写 why 与约束：不变量、绕开某个坑的原因、必须保持的顺序、外部系统的怪癖。读者是三个月后要改这段代码的人。

## Docstring

写契约：参数、返回值、异常、边界条件。格式随仓库既有风格（Google、NumPy、JSDoc 或语言默认），没有先例就选该语言生态的主流。公开入口与非显然行为上写。

**Completion criterion**：每条注释都回答「为什么」，每个公开入口都写清了参数、返回值、异常。
