# GLOSSARY 格式

单 context 用 `docs/GLOSSARY.md`；多 context 用 `docs/GLOSSARY-MAP.md` 列出各 context 的位置与关系，术语表放 `docs/<context>/GLOSSARY.md`。

```md
# {Context 名}
{一两句说明这个 context 是什么、为什么存在}

## Language

**Order**:
客户提交的一次购买请求。
_Avoid_: Purchase, transaction
```

- 有态度：同一概念有多个词时选最好的一个，其余列进 `_Avoid_`。
- 定义一两句封顶，只说什么，不写怎么做。
- 只收这个 context 特有的概念；timeout、错误类型这类通用的不收。
- 天然成组就加小标题。
