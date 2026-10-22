---
name: docs-adr
description: 当用户要记录技术决定、写下为什么这么设计，或提到「ADR」「决策记录」时使用。
---

# ADR

## 三条门槛（同时成立才建）

1. **Hard to reverse** —— 改主意的代价实打实
2. **Surprising without context** —— 后来的人看着代码会问「当初为什么这么写」
3. **A real trade-off** —— 有真实备选，你是为具体理由选的

## 写

`docs/adr/NNNN-slug.md`，编号取 `docs/adr/` 最大号加一，第一次用就建目录。

正文是一行标题加一到三句话：背景、决定了什么、为什么——价值就是记下这个决定与原因。

可选段落（多数用不上）：Considered Options（被否方案值得记住时）、Consequences（下游影响不明显时）。

不写状态。被取代时在新 ADR 里写「取代 ADR-NNNN」，旧的不动；反查用 `rg 'ADR-NNNN'`。有问题就改正文，不留历史版本。

值得记录：带 lock-in 的选型、context 间集成方式、边界与范围（明确的 no 和 yes 一样值钱）、故意偏离显而易见的做法、代码里看不见的约束。

见 [../_shared/docs-rules.md](../_shared/docs-rules.md)。
