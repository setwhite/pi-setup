---
name: docs-commit
description: 当用户要求提交代码、写提交信息，或提到「提交」「commit」时使用。
---

# Commit 信息

遵循 [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)。

## 格式

```
<type>[scope][!]: <description>

[body]

[footer]
```

- `type` 必填，取 feat、fix、refactor、perf、test、docs、chore、build、ci、revert 之一。
- `scope` 是模块名，可选。
- `description` 用祈使句，30 字以内，不加句号。
- `body` 空行后写变更动机与上下文。
- `footer` 空行后写元数据，每次提交带署名 `Co-Authored-By: pi <noreply@pi.dev>`。

破坏性变更二选一：标题加 `!`（`feat(api)!: 移除 /v1/users 接口`），或 footer 写 `BREAKING CHANGE: <说明与迁移方式>`。

## 拆分

一个 commit 一类变更。混合改动就分次暂存，拆成多个 commit。

```bash
git status --short        # 盘点改动
git diff --cached --stat  # 看暂存区，判断主力 type
```

## 示例

```
feat(parser): 支持 Markdown 表格解析

重构解析入口，支持嵌套表格。

Co-Authored-By: pi <noreply@pi.dev>
```
