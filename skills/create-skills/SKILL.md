---
name: create-skills
disable-model-invocation: true
description: 创建或优化 agent skill。
---

# 创建 Skill

每步完成后等用户确认。优化已有 skill 时跳过 Step 1–2，做 Step 3–6，重点是 Step 5。

## 术语速查

- **model-invoked**：靠 description 自动触发；代价是 description 常驻上下文（context load）。
- **user-invoked**：设 `disable-model-invocation: true`，只能人手触发；description 仍必填（缺失则不加载），但不进系统提示词，零常驻成本。
- **branch**：触发场景，一个场景一个 branch。
- **step / reference**：有序操作指令 / 查阅性定义、规则、示例；step 在前。
- **completion criterion**：判断某一步做完的条件，要可检查、覆盖边界。
- **progressive disclosure**：只在部分 branch 需要的 reference 放 `references/`（相对路径引用）；全 branch 都要的留 SKILL.md。

## 流程

### Step 1 — 判断载体

三条都满足才值得建 skill：模型默认做不到、有固定流程、会跨会话复用。不满足就用一行 AGENTS.md 规则解决。

### Step 2 — 确定定位（invocation model）

1. 谁触发？agent 自动或其他 skill 调用 → model-invoked；只有人手输入 → user-invoked。
2. 有哪些触发场景？

### Step 3 — 写 description（必填）

- model-invoked：一句概念（3–8 字，如「决策记录」，用预训练里的紧凑概念代替长句）+ 触发分支，一个 branch 一个触发词（同义词不算两个，如「提交」「commit」），句式 `当用户要求…、提到…时使用。` 落点与正文清单不进 description；没有独特方法的直接写触发条件。
- user-invoked：一句话概括 skill 做什么，不写触发词。

### Step 4 — 组织内容

1. 只写模型猜不到的：口味偏好（禁 emoji、署名格式）、硬事实（API 参数、路径）、特定流程。
2. 有操作顺序的写 step，查阅性的写 reference。
3. 每个 step 给出可检查的 completion criterion。

### Step 5 — 修剪（pruning）

- **duplication**：同规则只在唯一位置定义；跨文件引用写相对路径；与 AGENTS.md 等常驻规则重叠的直接删。
- **清单与示例**：逐条复述正文规则的自检清单删；同类示例只留一个。
- **negation**：规则用正面表述；反模式节删掉，要强调的例外并进规则；口味类禁列表（禁 emoji、禁句号）保留精确否定。
- **no-op**：模型默认会做的、已知的常识都删。
- **sediment**：删不再 relevant 的旧内容。
- **长度**：SKILL.md 超 200 行考虑 progressive disclosure。

### Step 6 — verification & validation

静态检查逐条过：

- description 非空，触发方式与定位相符
- 每个 step 的 completion criterion 能判断 done/not-done
- 无断裂指针：引用的文件与路径都存在

动态检查：新开会话盲测，模型不知道自己在被测。

- model-invoked：真实触发语试一遍，再用一句近似但不该触发的话确认不误触发
- user-invoked：用 `/skill:name` 实跑一遍

**Completion criterion**：静态检查全过，实跑时触发与执行符合定位。
