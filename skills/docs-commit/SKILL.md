---
name: docs-commit
description: Conventional Commits 私域规则与原子提交。当用户要求提交代码或写 commit message 时使用。
---

# Commit 信息

遵循 Conventional Commits v1.0.0，叠加私域规则：

- Header：祈使句，英文不超过 50 字符，中文不超过 30 字，结尾无句号；scope 取模块名（可选）。
- Body：写变更动机与上下文（why），不复述 diff。
- Footer：必带 `Co-Authored-By: pi <noreply@pi.dev>`。
- Atomic Commits：一个 commit 一类逻辑变更；混合改动用 `git status --short` 与 `git diff --cached --stat` 分批暂存。
