---
name: arch
disable-model-invocation: true
description: 系统结构与测试 seam：维护 ARCHITECTURE.md 与模块文档。
---

# 架构

只在结构会变时跑：新项目、新增模块、依赖方向变化、出现新 seam。其余时候 `docs/ARCHITECTURE.md` 保持原样。

前提：`docs/specs/` 里有本轮要做的 spec。

## 原则

- package by feature：按功能组织，不按层。
- 签名、异常、字段以代码 docstring 为准；`docs/modules/` 只写用法与取舍。
- seam 越少越好，理想是一个：取能满足全部 spec 的最高那层。

## Step 1 — 读现状

读 `docs/ARCHITECTURE.md`、相关 spec 与 ADR。结构以代码为准，文档不一致就改文档。

**Completion criterion**：说得出现有模块边界、依赖方向，以及本次要动哪些。

## Step 2 — 定结构与 seam

- 定模块职责表、代码放置规则、`docs/modules/` 清单；模块表写职责与允许的依赖方向，目录布局指向代码。
- seam 清单摊给用户确认，写进 `docs/ARCHITECTURE.md`；spec 的「测试决定」只列本 spec 用哪几条。测试规则见 `../_shared/testing.md`。
- Coverage check：每份 spec 都有模块承接。

**Completion criterion**：用户批准，seam 清单已确认。

## Step 3 — 落盘

写 `docs/ARCHITECTURE.md` 与 `docs/modules/<module>.md`，落点与索引按 `../_shared/docs-rules.md`。

**Completion criterion**：文档落盘，下一步提示 `/skill:plan` 拆任务。
