---
name: hackernews-search
disable-model-invocation: true
description: 搜索 Hacker News 帖子与热门。
---

# Hacker News 搜索

## 概述

两种模式，直接调 API 无需注册：
- **搜索** —— `read` 调 Algolia API，单次 HTTP GET，零依赖
- **Feed** —— Python 脚本调 Firebase，拿首页热门/最新/最高分

搜索用 `read` 调 Algolia API 即可；Feed 模式用下面的 Python 脚本。

## 搜索：`read` 调 Algolia API

### URL 模板

`https://hn.algolia.com/api/v1/search?query=<关键词>&tags=<类型>&hitsPerPage=<条数>`

### 参数

- `query` —— 搜索关键词，空格分隔，必填
- `tags` —— `story`（默认）/ `comment` / `(story,comment)`（全部），可选
- `hitsPerPage` —— 1–30，默认 20，可选
- `page` —— 页码，0 起始，可选

### 示例

```
read "https://hn.algolia.com/api/v1/search?query=deepseek&tags=story&hitsPerPage=15"
read "https://hn.algolia.com/api/v1/search?query=rust+async&tags=comment&hitsPerPage=10"
read "https://hn.algolia.com/api/v1/search?query=linux+kernel&tags=(story,comment)&hitsPerPage=10"
```

翻页：追加 `&page=<页码>`。

### 响应解析

`read` 返回 JSON：
- `hits[]` —— 结果数组，含 `title`、`url`、`objectID`（拼成 HN 链接）、`points`、`num_comments`、`author`、`created_at`
- `nbHits` / `nbPages` / `page` —— 总命中数 / 总页数 / 当前页

## Feed：Python 脚本

脚本路径：`skill://hackernews-search/scripts/hackernews-search.py`。若路径无法解析，用 `read` 调 Firebase 端点回退。

### Feed 模式

```bash
python "<path>" '{"mode":"top","count":10}'   # 首页热门
python "<path>" '{"mode":"new","count":10}'    # 最新
python "<path>" '{"mode":"best","count":10}'   # 最高分
```

- `mode` —— `top` / `new` / `best`，必填
- `count` —— 1–30，默认 10，可选


## 失败回退

- 搜索网络错误 —— 重试一次，仍失败用 `web_search` 搜 `site:news.ycombinator.com <关键词>`
- Feed 脚本不可用 —— `read` 调 Firebase 端点拿 ID 列表 → 并行取详情 → 提取字段

## 展示格式

```
### 🔥 HN 上关于"<query>"的讨论

| # | 标题 | 分数 | 评论 | 日期 | HN 链接 |
|---|------|------|------|------|---------|
| 1 | <title> | <points> | <num_comments> | <date> | [HN](<hn_url>) |

共 <total> 条结果。
```
