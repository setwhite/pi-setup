---
name: create-skills
disable-model-invocation: true
description: 创建或优化 agent skill。
---

# 创建 Skill

按以下流程引导用户完成 skill 的创建或优化，每步完成后等用户确认（checkpoint）；优化已有 skill 时跳过第一、二节，从第三节点到第六节，重点是第五节修剪（pruning）。

## 术语速查

- **model-invoked**：`description` 承担触发职责（trigger），agent 自动触发；代价是 description 常驻上下文（context load）。
- **user-invoked**：设 `disable-model-invocation: true`，只能人手触发的路径；description 仍必填（缺失则 skill 不加载），但不进系统提示词，零 context load。
- **branch**：skill 的触发场景/路径，一个场景一个 branch。
- **step / reference**：有序操作指令 / 查阅性定义、规则、示例。step 在前，reference 在后。
- **completion criterion**：判断某一步做完（done/not-done）的条件，要可检查并覆盖边界。
- **progressive disclosure**：只有部分 branch 需要的 reference 推到独立文件（放 `references/` 子目录，SKILL.md 用相对路径引用），全 branch 都需要的留在 SKILL.md。
- **leading word**：用模型预训练里的紧凑概念（「克制」「边界」）代替长句描述。

## 流程

### 一、判断载体

三条都满足才值得建 skill：模型默认做不到、有固定流程、会跨会话复用。不满足就用 AGENTS.md 里一行规则解决。

### 二、确定定位（invocation model）

1. 谁触发？agent 自动或其他 skill 调用 → model-invoked；只有人手输入 → user-invoked。
2. 有哪些触发场景？每个场景是一个 branch。

### 三、写 description（必填）

- model-invoked：第一句说清 skill 是什么；每个 branch 一个触发词（trigger word，同义词不算两个，如「提交」「commit」），句式 `当用户要求…、提到…时使用。`
- user-invoked：一句话概括 skill 做什么，不写触发词。

### 四、组织内容

1. 只写模型猜不到的信息（non-obvious）：口味偏好（禁 emoji、署名格式）、硬事实（API 参数、路径）、特定流程。
2. 有操作顺序的写成 step，查阅性的写成 reference；step 在上。
3. 每个 step 给出可检查的 completion criterion。
4. 只在部分 branch 需要的 reference 用 progressive disclosure 推出 SKILL.md。

### 五、修剪（pruning）

- **duplication**：同规则只在唯一位置定义；跨文件用相对路径引用（`见 ../other-skill/SKILL.md`）；与 AGENTS.md 等常驻规则重叠的部分直接删
- **清单与示例**：自检清单逐条复述正文规则时删（重复即 duplication）；同类示例只留一个
- **negation**：规则用正面表述（affirmative phrasing）；反模式节删掉，要强调的例外并进规则；口味类禁列表（禁 emoji、禁句号）保留精确否定
- **no-op**：模型默认会做的、已知的常识（类型表、口诀）都删
- **sediment**：删不再 relevant 的旧内容（stale content）
- **长度**：SKILL.md 超 200 行考虑 progressive disclosure

### 六、verification & validation

静态检查（verification）：

- description 非空，触发方式与定位相符（见第三、四节）
- 每个 step 的 completion criterion 能判断 done/not-done
- 无断裂指针：引用的文件与路径都存在

动态检查（validation；新开会话，避免模型知道自己在被测 - blind test）：

- model-invoked：用真实触发语试一遍，再用一句近似的、不该触发的话确认不误触发（trigger precision & recall）
- user-invoked：用 `/skill:name` 实跑一遍

**Completion criterion**：skill 能被 pi 正常加载（description 非空、frontmatter 合法、引用无断裂），且实跑时触发与执行符合定位。
