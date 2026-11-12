---
name: create-skills
disable-model-invocation: true
description: 创建或优化 agent skill。
---

# 创建 Skill

优化已有 skill 时跳过前两节，从 description 开始。

## 值不值得建

三条都满足才建：模型默认做不到、有固定流程、会跨会话复用。

## 定位

自动触发就靠 description。只有人工输入就设 `disable-model-invocation: true`。

## description

自动触发的先写一句概念，3–8 字，用预训练里的紧凑词（「决策记录」）。再写触发分支，一个分支一个触发词，同义词不算两个（「提交」「commit」）。句式用 `当用户要求…、提到…时使用。`

人工触发的写一句话概括做什么，不写触发词。

位置与正文清单不进 description。

## 组织

先 step，有序操作。后 reference，查阅性定义、规则、示例。只写模型猜不到的内容：口味、硬事实、特定流程。只在部分分支需要的 reference 放 `references/`。

## 修剪

- 同一条规则只写一处。与 AGENTS.md 重叠的删掉。
- 逐条复述正文的自检清单删掉。同类示例只留一个。
- 规则用正面表述。要强调的例外并进规则。
- 模型默认会做的、常识，删掉。
- 不再相关的内容删掉。
- 超过 200 行就拆 `references/`。

## 验证

- description 非空，触发方式与定位相符。
- 无断裂指针：引用的文件与路径都存在。
- 新开会话盲测。真实触发语试一遍，再用一句近似但不该触发的话确认不误触发。
