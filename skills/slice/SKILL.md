---
name: slice
disable-model-invocation: true
description: 把当前阶段拆成原子任务，写入 docs/todos/。
---

# 拆任务

一次只拆一个阶段。后续阶段各占一行，进入该阶段时再拆，别预支。

前提：本轮 spec 与 `docs/ARCHITECTURE.md` 就绪，接缝已确认。

## Step 1 — 定范围

读 spec 与接缝清单，确认这一阶段交付什么、不含什么。

完成标准：阶段边界与 MVP 范围明确。

## Step 2 — 拆原子任务

- 每个任务是 tracer bullet：垂直切片，穿过要碰的每一层，做完能单独验证，单次会话能做完。
- 拆之前先看有没有 prefactor：先把改动变简单，再做简单的改动。
- 「验收」写成能跑的检查（命令，或输入与期望输出），不写散文。
- 后续阶段在阶段表各占一行：阶段名、任务区间、目标，不拆任务。

格式见 `references/todo-format.md`（阶段表不存在就建），落点按 `../_shared/docs-rules.md`。

完成标准：用户批准，每个任务单会话能做完；提示从 `/skill:coding` 领第一个任务。
