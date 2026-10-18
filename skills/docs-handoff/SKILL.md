---
name: docs-handoff
disable-model-invocation: true
description: 把当前会话压缩成交接文档，写入 docs/handoff/。
argument-hint: "下一个会话要做什么？"
---

# Handoff

写一份交接文档，让全新会话能接着干。

- 落盘 `docs/handoff/YYYY-MM-DD-slug.md`，日期用 `date +%F` 取，slug 取下一个会话的主题。
- 写一节「下一步用哪些 skill」，点名下一个 agent 该调哪个。
- spec、ADR、commit、diff、issue 里已有的内容不复述，引用路径或链接。
- 密钥、密码、身份信息脱敏。
- 用户传了参数就按它调整重点。

见 [../_shared/docs-rules.md](../_shared/docs-rules.md)。
