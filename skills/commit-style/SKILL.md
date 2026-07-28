---
name: commit-style
description: 生成符合 Conventional Commits 的提交信息。当用户要求提交代码、生成 commit message、发起 PR、或提到“提交”、“commit”、“push”时使用。
---

# Commit 信息规范

遵循 [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)。

## 格式

```
<type>[scope][!]: <description>

[body]

[footer]
```

- `type` —— 变更类型，必填
- `scope` —— 影响范围（模块/组件名），可选，没有不强加
- `!` —— 标记 BREAKING CHANGE，可选
- `description` —— 中文、动词开头、≤ 50 字、不加句号，必填
- `body` —— 空行后，说明变更动机与上下文，可选
- `footer` —— 空行后，`BREAKING CHANGE:` 等元数据，可选

BREAKING CHANGE 两种写法，二选一：
- 标题加 `!`：`feat(api)!: 移除 /v1/users 接口`
- Footer 说明：`BREAKING CHANGE: 移除 /v1/users，迁移至 /v2/users`

## Type

- `feat` —— 新功能
- `fix` —— Bug 修复
- `docs` —— 仅文档变更
- `style` —— 格式、空格等不影响逻辑的变更
- `refactor` —— 不改行为、不改 bug 的代码调整
- `perf` —— 性能优化
- `test` —— 测试补充或修改
- `build` —— 构建系统或外部依赖变更
- `ci` —— CI 配置变更
- `chore` —— 其他杂务

口诀：改行为 → `feat`/`fix`，改结构 → `refactor`，改性能 → `perf`，改描述 → `docs`，改验证 → `test`，改环境 → `build`/`ci`/`chore`。

## 生成流程

1. `git diff --stat` 回顾改动
2. 判断主力 type，混合时拆 commit
3. 提炼 ≤ 50 字中文摘要，动词开头
4. 有 breaking change 加 `!` 或 footer
5. 用户确认后 `git commit`

## 示例

```
feat(parser): 支持 Markdown 表格解析
fix: 修复用户名为空时 NPE
refactor(api): 提取公共认证中间件
perf(cache): 缓存热点查询减少 30% 延迟
feat(auth)!: JWT 令牌签名算法升级为 RS256
```

## 反模式

- 一条 commit 混多种 type
- 描述不具体（`fix bug`、`update code`）
- 描述加句号或“了”“的”结尾
- 强行编造 scope
- breaking change 不标注
