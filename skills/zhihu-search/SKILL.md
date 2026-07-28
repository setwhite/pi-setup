---
name: zhihu-search
disable-model-invocation: true
description: 搜索知乎站内内容。
---

# Zhihu Search Skill

## 概述
调用知乎开放平台 `GET /api/v1/content/zhihu_search` 检索站内内容，返回精简 JSON 结构。
完整 API 文档：https://developer.zhihu.com/docs

## 认证
环境变量 `ZHIHU_ACCESS_SECRET` 必填。可选配置：
- `ZHIHU_OPENAPI_BASE_URL`（默认：`https://developer.zhihu.com`）
- `ZHIHU_ZHIHU_SEARCH_URL`（完整 endpoint 覆盖，优先于 `ZHIHU_OPENAPI_BASE_URL` + 默认 path）

## 快速开始
```bash
python {baseDir}/scripts/zhihu-search.py '{"query":"如何理解 rave 文化","count":5}'
```

## 输入约定
传入 JSON 参数：
```json
{"query":"...", "count":10}
```
规则：
- `query` 必填，且不能为空字符串（自动 `strip`）。
- `count` 可选；脚本自动限制到 1-10。

## 输出约定

### 成功
返回 JSON：
- `code`, `message`
- `item_count`
- `items[]`，包含 `title`, `summary`, `url`, `author_name`, `vote_up_count`, `comment_count`, `edit_time`

### 失败
`error` 字段为动态错误描述：
```json
{"error":"query is required","exit_code":1}
{"error":"HTTP 403","body":"Forbidden","exit_code":1}
```
