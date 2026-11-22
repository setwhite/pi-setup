---
name: docs-pr
disable-model-invocation: true
description: 生成高信噪比 PR 描述：Summary、Evidence、Merge Danger。
---

# PR 描述

短句直说，术语用 `docs/GLOSSARY.md` 规范词，不抄原始 diff。

```markdown
## Summary

<最小可视化视图：伪代码 / 调用树 / 组件树 / Mermaid>

## Evidence

- Before: <失败测试或输出> (path:line)
- After: <通过测试或输出> (path:line)

## Merge Danger

- Reversibility: Two-way door（可回滚） / One-way door（不可逆，附原因）
- Blast Radius: <一句话说明影响范围>
```
