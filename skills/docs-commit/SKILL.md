---
name: docs-commit
description: Conventional Commits 个人补充规则与原子提交。当用户要求提交代码或写 commit message 时使用。
---

# Commit 信息

遵循 Conventional Commits v1.0.0，叠加个人补充规则：

- Header：祈使句，英文不超过 50 字符，中文不超过 30 字，结尾不加句号；scope 取模块名（可选）。
- Body：写清楚改动动机与背景（why），不复述 diff。
- Footer：必带 `Co-Authored-By: pi <noreply@pi.dev>`。
- Atomic Commits：一个 commit 只做一类逻辑变更；混合改动用 `git status --short` 和 `git diff --cached --stat` 分批暂存。
