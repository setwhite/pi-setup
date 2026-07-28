---
name: create-skills
disable-model-invocation: true
description: 创建或优化 agent skill。
---

# 创建 Skill

按以下流程引导用户完成 skill 的创建或优化，每步完成后等待用户确认再继续。

---

## 概念速查

以下术语在流程中会用到，内联定义，无需查外部参考。

**model-invoked**：有 `description` 字段，agent 能自动触发，其他 skill 也可调用。代价是 description 常驻上下文，消耗 token。

**user-invoked**：设 `disable-model-invocation: true`，无 description。只有人手输入名称才能触发，零 context load。代价是人得记住它存在。

**branch**：skill 的一种触发场景/路径。比如 `commit-style` 有「commit」「push」「提交」三个 branch。

**step**：有序的操作指令。**reference**：定义、规则、示例等查阅性内容。

**information hierarchy**：内容按紧急程度排序——step 最前，in-file reference 其次，disclosed reference（独立文件）最后。

**completion criterion**：告诉 agent 这一步「做完了」的条件。两个维度：可检查（能判断 done/not-done）和充分性（覆盖所有边界）。

**progressive disclosure**：把 reference 推到独立文件，只在需要时加载。拆分依据是 branch——只有部分 branch 需要的 material 适合推到后面，所有 branch 都需要的留下。

**leading word**：模型预训练中已有的紧凑概念（如「克制」「边界」），用它替代长段描述，让 agent 用更少的 token 锚定同一行为。

**single source of truth**：每个规则只在唯一位置定义。多处出现 = **Duplication**，改一处漏一处。

**Negation**：说「不要 X」反而激活 X。尽量正面表述目标行为。

**No-op**：规则说的是 agent 默认就会做的事，加了等于白加。测试：去掉这条规则，行为会变吗？

**Sediment**：过时内容堆积。每次改 skill 顺带清理不再相关的行。

---

## 流程

### 一、确定定位

问用户：
1. 谁触发？agent 自动或别的 skill 调用 → model-invoked。只有人手输入 → user-invoked。
2. 有哪些触发场景？列出来，每个场景是一个 branch。

### 二、写 description（仅 model-invoked）

- 第一句说清 skill 是什么
- 每个 branch 一个触发词，不重复。同义词不算两个 branch（「提交」「commit」是同一个）。
- 句式：`当用户要求…、提到…时使用。`

### 三、组织内容

1. 区分 step 和 reference。有操作顺序的写成 step，查阅性内容写成 reference。
2. step 在上，in-file reference 在下。每个 step 给出可检查的 completion criterion。
3. 只在部分 branch 需要的 reference → progressive disclosure 到独立文件。所有 branch 都需要的留在 SKILL.md。

### 四、修剪

逐项检查：
- **Duplication**：同一规则是否在 skill 内部或跨 skill 重复？（用「见 skill://xxx」替代）
- **Negation**：是否有「禁止…」「不要…」可以改写为正面表述？
- **No-op**：去掉这条，agent 行为会变吗？不变则删。
- **Sediment**：是否有不再 relevant 的旧内容？
- **长度**：SKILL.md 超过 200 行考虑 disclosure。

### 五、验证

以用户视角模拟一遍：
- 触发方式正确？（model-invoked 有 description，user-invoked 没有）
- 触发词能覆盖所有 branch？
- step 的 completion criterion agent 能判断 done/not-done？
- 内容没有依赖外部 reference 的断裂指针？
