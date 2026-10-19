---
name: arch
disable-model-invocation: true
description: 系统结构与测试接缝：维护 ARCHITECTURE.md 与模块 README。
---

# 架构

只在结构会变时跑：新项目、新增模块、依赖方向变化、出现新接缝。其余时候 `docs/ARCHITECTURE.md` 保持原样，别重写。

前提：`docs/specs/` 里有本轮要做的 spec。

## 原则

- package by feature：按功能组织，不按层。
- 签名、异常、字段以代码 docstring 为准；模块 README 只写用法与取舍。
- 接缝越少越好，理想是一个：取能满足全部 spec 的最高那层。

## Step 1 — 读现状

读 `docs/ARCHITECTURE.md`、相关 spec 与 ADR。结构以代码为准，文档不一致就改文档。

完成标准：说得出现有模块边界、依赖方向，以及本次要动哪些。

## Step 2 — 定结构与接缝

- 模块表、依赖方向、代码放置规则、模块 README 位置。
- 接缝清单摊给用户确认，结论写进 spec 的「测试决定」；测试规则见 `../_shared/testing.md`。
- Coverage check：每份 spec 都有模块承接。

完成标准：用户批准，接缝清单已确认。

## Step 3 — 落盘

`docs/ARCHITECTURE.md` 与各模块 README。落点与 README 索引按 `../_shared/docs-rules.md`。

完成标准：文档落盘，下一步提示 `/skill:slice`。
