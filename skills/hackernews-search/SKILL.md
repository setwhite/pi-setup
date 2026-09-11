---
name: hackernews-search
disable-model-invocation: true
description: 搜索 Hacker News 帖子与热门。
---

# Hacker News 搜索

## 搜索：`web_fetch` 调 Algolia API

无需注册，单次 HTTP GET。URL 模板：

`https://hn.algolia.com/api/v1/search?query=<关键词>&tags=<类型>&hitsPerPage=<条数>`

- `query` —— 关键词，空格分隔，必填
- `tags` —— `story`（默认）/ `comment` / `(story,comment)`，可选
- `hitsPerPage` —— 1–30，默认 20，可选
- `page` —— 页码，0 起始，可选

```
web_fetch "https://hn.algolia.com/api/v1/search?query=deepseek&tags=story&hitsPerPage=15"
```

翻页追加 `&page=<页码>`。响应为 JSON：`hits[]` 每条含 `title`、`url`、`objectID`（拼 HN 链接用）、`points`、`num_comments`、`author`、`created_at`；另有 `nbHits` / `nbPages` / `page`。

## Feed：Python 脚本

脚本路径相对本 skill 目录：`scripts/hackernews-search.py`。

```bash
python "<path>" '{"mode":"top","count":10}'   # 首页热门
python "<path>" '{"mode":"new","count":10}'    # 最新
python "<path>" '{"mode":"best","count":10}'   # 最高分
```

`mode` 必填（top / new / best），`count` 可选（1–30，默认 10）。

## 失败回退

- 搜索网络错误：重试一次，仍失败改用 `web_search` 搜 `site:news.ycombinator.com <关键词>`
- Feed 脚本不可用或路径解析不了：`web_fetch` 调 Firebase 端点拿 ID 列表 → 并行取详情 → 提取字段

## 展示

| # | 标题 | 分数 | 评论 | 日期 | HN 链接 |
|---|------|------|------|------|---------|
| 1 | <title> | <points> | <num_comments> | <date> | [HN](<hn_url>) |

标题写「HN 上关于 <query> 的讨论」，表后附「共 <total> 条结果」。
