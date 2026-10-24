---
name: docs-pr
disable-model-invocation: true
description: PR 描述：Summary / Evidence / Merge Danger 三段。
---

# PR 描述

不寒暄，散文尽量短，术语用 `docs/GLOSSARY.md` 的规范词。

```markdown
## Summary

<图、diff 草图或树>

## Evidence

- **Before:** <截图 / 输出 / 失败的测试>
  **After:** <截图 / 输出 / 通过的测试>

## Merge Danger

**Door:** <改得回来（two-way）还是改不回来（one-way）>

**Blast Radius:** <一个词说清影响范围>

<可选：合并后的影响>
```

## Summary 挑最小的视图

- 伪代码 —— 逻辑与算法
- 调用树 —— 运行时控制流
- 组件树 —— UI 结构，带重要的 state 与模块边界
- Mermaid —— 组件交互、数据流

代码与 diff 不抄进描述，要指就写 `路径:行号`。其余规则见 `../_shared/docs-rules.md`。
