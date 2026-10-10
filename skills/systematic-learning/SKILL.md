---
name: systematic-learning
disable-model-invocation: true
description: 体系化学习：用 Feynman technique 构建知识体系（schema），输出 HTML 卡片。
---

# 体系化学习

用 Feynman technique 把孤立概念挂到知识树上（elaborative encoding）：讲清来源、定位、对比和边界，不做扁平定义。

## 输出结构（严格按此顺序）

### 1. 核心本质

Feynman 式讲解给外行听，回答三个问题：它是什么（一句话）；解决什么痛点（没有它时世界什么样）；为什么是现在才出现（技术前提与时代背景）。

### 2. 知识坐标系

broader terms（所属理论框架）；narrower terms（核心要素、细分流派）；related terms（易混淆对比，句式 `概念 A vs 概念 B —— 一句话区分`）。

### 3. 演进脉络

关键发展节点的时间线、代表人物及其贡献、前沿趋势与当前争论（open problems）。

### 4. 案例分析

1-2 个实例，经典场景加一个 counterexample（反直觉案例）；每个说清背景、应用方式、为何选它。

### 5. 边界与误区

failure modes（能力边界：何时有效、失效、有副作用）与 misconceptions（初学者最常见的误解与错误用法）。

## 工作流

### Step 1 — 并行搜索（multi-faceted retrieval）

概念本身（核心原理、通俗解释、tutorial）／知识定位（对比区别、发展史与提出者）／深入边界（局限误区、实战案例）三路并行。

**Completion criterion**：三路各自产出候选来源清单。

### Step 2 — 交叉验证（triangulation）

多源确认的才可信（corroboration）；单一来源标 `[单一信源]`（single-source）；来源矛盾则标注 conflicting evidence，列出双方依据与出处。

**Completion criterion**：每条关键结论都有信源，或已标注 `[单一信源]`／分歧。

### Step 3 — 生成 HTML 卡片

按五段结构输出，卡片顶部标注检索日期（YYYY-MM-DD；provenance），关键信息标注来源；格式遵循 `../html-card/SKILL.md`。

**Completion criterion**：卡片已生成，顶部有检索日期，五段齐备。
