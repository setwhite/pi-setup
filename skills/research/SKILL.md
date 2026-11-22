---
name: research
disable-model-invocation: true
description: 收集一手外部事实、对比选型或核实第三方库行为，沉淀至 docs/research/。
---

# 技术调研

只在选型未定或结论依赖外部事实时运行，结果写入 `docs/research/`。

- Discovery First：问题模糊先搜 1 到 2 轮收敛成一句话，再按子代理隔离方式调研。
- Primary Sources：官方文档、源码、标准规范与实测 API 响应优先，每条结论附链接或 `路径:行号`。
- Community Experience：真实踩坑查 Reddit、`linux.do`（带域名）和 Hacker News（见 `references/hackernews.md`）；二手博客只作线索。

```md
## 结论

## 依据

## 未决
```

后续流程只引路径不抄正文；完成后按需提示运行 `/skill:plan`。
