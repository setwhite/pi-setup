---
name: commit-style
description: 按 Conventional Commits 生成提交信息。当用户要求提交代码、写提交信息，或提到「提交」「commit」时使用。
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
- `description` —— 动词开头、≤ 30 字、不加句号
- `body` —— 空行后，说明变更动机与上下文
- `footer` —— 空行后，`BREAKING CHANGE:` 等元数据；每次提交必带署名：

```
Co-Authored-By: pi <noreply@pi.dev>
```

BREAKING CHANGE 二选一：标题加 `!`（`feat(api)!: 移除 /v1/users 接口`），或 footer 写 `BREAKING CHANGE: <说明与迁移方式>`。

## 流程

1. `git status --short` 盘点改动；要提交的文件按用户点名逐个 `git add`，禁止 `git add -A`、`git add .`
2. `git diff --cached --stat` 看暂存区，判断主力 type；混合多种变更就拆成多个 commit，用 `git add -p` 分次暂存
3. 提炼摘要；有 breaking change 加 `!` 或 footer
4. 用户确认后 `git commit`

**完成标准**：提交信息按格式生成、含署名，用户确认后再执行提交。

## 示例

```
feat(parser): 支持 Markdown 表格解析

重构解析入口，支持嵌套表格。

Co-Authored-By: pi <noreply@pi.dev>
```

单行示例：`fix: 修复用户名为空时 NPE`、`refactor(api): 提取公共认证中间件`、`perf(cache): 缓存热点查询`、`feat(auth)!: JWT 令牌签名算法升级为 RS256`
