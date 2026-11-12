---
name: todo
disable-model-invocation: true
description: 把 spec 拆成单次会话能做完的任务，写进 docs/todos/。
---

# 拆任务

输入是 spec 的验收与 `docs/ARCHITECTURE.md` 的 seam 清单。写进 `docs/todos/NNNN-slug.md`。

## 切片

- 每条任务是 tracer bullet：垂直切片，穿过要碰的每一层，做完能单独验证，单次会话能做完。
- 一次只拆一个阶段。
- 拆之前先看有没有 prefactor：先把改动变简单，再做简单的改动。上一轮 `/skill:audit` 的质量线索可以拆成 prefactor 任务。

## 格式

```md
- [ ] 未开始
- 验收：AC1、AC3

## 交付物

这一任务做完，用户能做什么。

## 前置

0003
```

- 状态三选一：`- [ ] 未开始`、`- [~] 待审`、`- [x] 已验收`。改状态不改文件名。
- 验收只写 AC 编号，不抄正文。
- 前置写被阻塞的任务号。只领前置全为 `[x]` 的任务，没有就写「无」。

拆完请用户确认。确认后提示用户运行 `/skill:coding`。
