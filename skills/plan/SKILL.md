---
name: plan
disable-model-invocation: true
description: 当需求还没问到没有歧义，或要把选型与取舍落成决策记录时使用。
---

# 需求与决策

问清不做项、验收标准、外部依赖。一次问完，每条给候选答案。其余从代码与对话里取。

术语当场定，写进 `docs/GLOSSARY.md`，格式见 `/skill:docs-glossary`。

## 决策

三个条件同时成立才建：难回退、后来的人会问「当初为什么这么写」、有真实备选。

写 `docs/decisions/NNNN-slug.md`。编号取目录最大号加一。第一次使用就建目录。正文三段：

```md
## 决定

## 为什么

## 代价
```

不写状态。被取代时新开一条，写「取代 DEC-NNNN」。旧的不动。反查用 `rg 'DEC-NNNN'`。

不够门槛的写进 spec 的「未决」。

## 交给谁

按 `../_shared/docs-rules.md` 定位置与编号。决策写完提示用户运行 `/skill:arch`。
