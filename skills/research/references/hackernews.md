# Hacker News

脚本 `scripts/hackernews-search.py` 在本 skill 目录下，Python 标准库，无需 token。

## 搜索

```bash
uv run python scripts/hackernews-search.py '{"query":"rust async","count":5}'
uv run python scripts/hackernews-search.py '{"query":"python","count":5,"type":"comment"}'
```

`query` 必填。`count` 取 1–30，默认 10。`type` 取 `story`（默认）、`comment`、`all`。

脚本走 `https://hn.algolia.com/api/v1/search`，单次 GET。要自己调时，参数是 `query`、`tags`（`story`/`comment`/`(story,comment)`）、`hitsPerPage`（1–1000）、`page`（从 0 起）。

响应 `hits[]` 含 `title`、`url`、`objectID`（拼 HN 链接用）、`points`、`num_comments`、`author`、`created_at`。顶层 `nbHits` 是总数。

## Feed

```bash
uv run python scripts/hackernews-search.py '{"mode":"top","count":10}'   # 首页热门
uv run python scripts/hackernews-search.py '{"mode":"new","count":10}'   # 最新
uv run python scripts/hackernews-search.py '{"mode":"best","count":10}'  # 最高分
```

`mode` 必填。返回 `items[]`，字段与搜索相同。

脚本不可用或路径解析不了，就用 Firebase 的 `topstories`、`newstories`、`beststories` 拿 ID 列表，再并发取 `item/<id>.json`。

## 输出

| # | 标题 | 分数 | 评论 | 日期 | HN 链接 |
|---|------|------|------|------|---------|
| 1 | <title> | <points> | <num_comments> | <YYYY-MM-DD> | [HN](<hn_url>) |

标题写「HN 上关于 <query> 的讨论」。表后附「共 <nbHits> 条结果」。
