---
name: create-skills
disable-model-invocation: true
description: 创建或优化 agent skill：准入评估、触发设计、最小骨架与盲测验证。
---

# 创建与优化 Skill

优化已有 skill 直接从「Description」开始。

- Admission：三条全满足才新建——模型默认做不到、有固定重复流程、会跨会话复用。
- Trigger：自动触发靠 `description`；人工触发设 `disable-model-invocation: true`。
- Description：自动触发写「3 到 8 字概念锚点 + `当用户要求…、提到…时使用。`」（每场景一词）；人工触发一句话概括职责，不写「当…时使用」；路径、格式与正文清单不进 `description`。
- Plain Language：人也会维护，说人话，避免生造缩略黑话或电报体。
- Positive Over Negation：直接写要做的目标行为；只有无法正向表达的硬底线才用禁令，且紧跟正向做法。
- Completion Criteria：步骤型 skill 每步末尾写清可核验的完成条件，防止模型急着往下一步走而敷衍结束。
- Leading Words：高频复杂要求用现成工程术语指代（如 TDD、Tracer Bullet），避免到处重复解释。
- Guardrails & Skeletons：安全边界、验证标准、个人硬规则与最小输出骨架写死，其余留白。
- Deterministic Over Prompt：能用脚本检查的放进 `scripts/`，别靠正文口头提醒。
- SSOT & No-Op Pruning：`AGENTS.md`、`_shared/` 或仓库自带事实（`package.json`、`--help`）不重复搬运；超 200 行拆进 `references/`；删掉后模型表现不变差的句子整句删。

## 验证

1. 跑自动校验脚本：`uv run python scripts/validate_skills.py <skills根目录>`
2. 新会话盲测：1 条正例验触发，1 条近义反例验不误触发。
