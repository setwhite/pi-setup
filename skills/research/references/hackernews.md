# Hacker News 检索

脚本 `scripts/hackernews-search.py` 在本 skill 目录下，使用 Python 标准库，无需 token。

```bash
uv run python scripts/hackernews-search.py '{"query":"rust async","count":5}'
uv run python scripts/hackernews-search.py '{"query":"python","count":5,"type":"comment"}'
uv run python scripts/hackernews-search.py '{"mode":"top","count":10}'
```

- 搜索参数：`query` 必填；`count` 取 1 到 30（默认 10）；`type` 取 `story`（默认）、`comment` 或 `all`。
- Feed 参数：`mode` 取 `top`、`new` 或 `best`。
- 底层与回退：搜索走 Algolia API（`https://hn.algolia.com/api/v1/search`）；脚本不可用时回退 Firebase API（`topstories`/`newstories`/`beststories` + `item/<id>.json`）。
- 展示：每条给出标题、分数、评论数、日期与 HN 链接，末尾附总结果数。
