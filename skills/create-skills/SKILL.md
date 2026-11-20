---
name: create-skills
disable-model-invocation: true
description: 创建或优化 agent skill：准入评估、触发设计、最小骨架与盲测验证。
---

# 创建与优化 Skill

优化已有 skill 直接从「Description」开始。

- Admission：三条同时满足才建——模型默认做不到、有固定重复流程、会跨会话复用。
- Trigger：自动触发靠 `description`；人工触发设 `disable-model-invocation: true`。
- Description：
  - 自动触发：3 到 8 字概念锚点 + `当用户要求…、提到…时使用。`（每分支一词，不堆同义词）。
  - 人工触发：一句话概括职责，不写「当…时使用」。
  - 路径、格式与正文清单不进 `description`。
- Guardrails & Skeletons：安全边界、验证标准、私域硬事实与最小输出骨架写死；其余留白。
- Deterministic Over Prompt：能用脚本检查的放进 `scripts/`，不写正文祈祷。
- SSOT & Pruning：`AGENTS.md` 或 `_shared/` 已写的条款不重复；超 200 行拆 `references/`；删模型常识与多余示例。

## 验证

1. 跑自动校验脚本：

```bash
uv run python scripts/validate_skills.py <skills根目录>
```

2. 新会话盲测：1 条正例验触发，1 条近义反例验不误触发。
