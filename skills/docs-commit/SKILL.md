---
name: docs-commit
description: 当用户要求提交代码、写提交信息，或提到「提交」「commit」时使用。
---

# Commit 信息规范

遵循 [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)。

## 格式

```
<type>[scope][!]: <description>

[body]

[footer]
```

- `type` —— 必填，只能取：feat、fix、refactor、perf、test、docs、chore、build、ci、revert
- `scope` —— 模块/组件名，可选，没有不强加
- `description` —— imperative mood、≤ 30 字、不加句号
- `body` —— 空行后，说明变更动机与上下文
- `footer` —— 空行后，`BREAKING CHANGE:` 等元数据；每次提交必带署名 `Co-Authored-By: pi <noreply@pi.dev>`

BREAKING CHANGE 二选一：标题加 `!`（`feat(api)!: 移除 /v1/users 接口`），或 footer 写 `BREAKING CHANGE: <说明与迁移方式>`。

## 流程（atomic commits）

1. `git status --short` 盘点改动；按用户点名的文件逐个 `git add`，不用 `git add -A` / `git add .`，避免无关改动混入
2. `git diff --cached --stat` 看暂存区判断主力 type；混合变更用 `git add -p` 分次暂存，拆成多个 atomic commit
3. 按上面的格式提炼摘要

**Completion criterion**：提交信息按格式生成、含署名，且每个 commit 只含一类变更。

## 示例

`feat(parser): 支持 Markdown 表格解析` + body「重构解析入口，支持嵌套表格。」+ 署名。
