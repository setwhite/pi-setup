---
name: create-skills
disable-model-invocation: true
description: 创建或优化 agent skill。
---

# 创建 Skill

按以下流程引导用户完成 skill 的创建或优化，每步完成后等用户确认。

## 概念速查

- **model-invoked**：`description` 承担触发职责，agent 自动触发；代价是 description 常驻上下文。
- **user-invoked**：设 `disable-model-invocation: true`，只能人手触发的路径；description 仍必填（缺失则 skill 不加载），但不进系统提示词，零 context load。
- **branch**：skill 的触发场景/路径，一个场景一个 branch。
- **step / reference**：有序操作指令 / 查阅性定义、规则、示例。step 在前，reference 在后。
- **completion criterion**：判断某一步做完的条件，要可检查并覆盖边界。
- **progressive disclosure**：只有部分 branch 需要的 reference 推到独立文件（放 `references/` 子目录，SKILL.md 用相对路径引用），全 branch 都需要的留在 SKILL.md。
- **leading word**：用模型预训练里的紧凑概念（「克制」「边界」）代替长句描述。
- **single source of truth**：每条规则只定义一次；重复出现即 Duplication。
- **Negation**：说「不要 X」会激活 X，改写为正面表述。
- **No-op**：去掉这条规则行为会变吗？不变就删——模型默认会做的、已知的常识都算。
- **Sediment**：过时内容堆积，每次修改顺手清理。

## 流程

优化已有 skill 时跳过第一、二节，从第三节点到第六节，重点是第五节修剪。

### 一、判断载体

三条都满足才值得建 skill：模型默认做不到、有固定流程、会跨会话复用。不满足就用 AGENTS.md 里一行规则解决。

### 二、确定定位

1. 谁触发？agent 自动或其他 skill 调用 → model-invoked；只有人手输入 → user-invoked。
2. 有哪些触发场景？每个场景是一个 branch。

### 三、写 description（必填）

缺失 description 的 skill 不会加载。

- model-invoked：第一句说清 skill 是什么；每个 branch 一个触发词（同义词不算两个，如「提交」「commit」），句式 `当用户要求…、提到…时使用。`
- user-invoked：一句话概括 skill 做什么，不写触发词。

### 四、组织内容

1. 只写模型猜不到的信息：口味偏好（禁 emoji、署名格式）、硬事实（API 参数、路径）、特定流程。通用最佳实践与模型已知的常识不写。
2. 有操作顺序的写成 step，查阅性的写成 reference；step 在上。
3. 每个 step 给出可检查的 completion criterion。
4. 只在部分 branch 需要的 reference 用 progressive disclosure 推出 SKILL.md。

### 五、修剪

- **Duplication**：同规则只在唯一位置定义；跨文件用相对路径引用（`见 ../other-skill/SKILL.md`）；与 AGENTS.md 等常驻规则重叠的部分直接删
- **清单与示例**：自检清单逐条复述正文规则时删；同类示例只留一个
- **Negation**：规则用正面表述；反模式节删掉，要强调的例外并进规则；口味类禁列表（禁 emoji、禁句号）保留精确否定
- **No-op**：模型默认会做的、已知的常识（类型表、口诀）都删
- **Sediment**：删不再 relevant 的旧内容
- **长度**：SKILL.md 超 200 行考虑 disclosure

### 六、验证

静态检查：

- 触发方式正确：model-invoked 的 description 含触发词，user-invoked 的为简短概括，两者均必填
- 触发词覆盖所有 branch
- step 的 completion criterion 能判断 done/not-done
- 无断裂指针：引用的文件与路径都存在

动态检查（新开会话，避免模型知道自己在被测）：

- model-invoked：用真实触发语试一遍，再用一句近似的、不该触发的话确认不误触发
- user-invoked：用 `/skill:name` 实跑一遍

**完成标准**：skill 能被 pi 正常加载（description 非空、frontmatter 合法、引用无断裂），且实跑时触发与执行符合定位。
