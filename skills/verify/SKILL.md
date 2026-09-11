---
name: verify
disable-model-invocation: true
description: 验证变更：跑检查、整理证据、等人审结论。
---

# Verify

## Step 1 — 机器验证

- 跑项目 lint + test，保留原始输出
- 有 PR 就查 CI 状态（`gh pr checks`）

**完成标准**：每项检查有明确结果——通过，或列出失败项与原始输出。

## Step 2 — 整理人审

按下方清单交给用户，等结论：

- 变更范围：`git diff --stat` 或文件清单
- 检查结果：lint / test / CI 的结论与关键输出
- 验收清单：PLAN.md 的 TODO 验收标准逐条标注「通过 / 未通过 / 未验证」；没有 PLAN.md 就按用户要求列
- 独立评审：新会话加载 judge skill 拿到的结论；没跑就写「未评审」
- 待决问题与风险

**完成标准**：用户明确「通过」或「打回」；打回则记录原因。
