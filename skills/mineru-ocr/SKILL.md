---
name: mineru-ocr
description: 文档转 Markdown。当用户要解析 PDF、Office 文档（docx/xlsx/pptx），或明确要求图片 OCR / 使用 MinerU 时使用。
---

# MinerU 解析

```bash
uv run --no-project --with requests python scripts/mineru_api.py "<输入路径或URL>" [-o 输出目录] [--pages 页码范围]
```

`scripts/mineru_api.py` 在本 skill 目录下，跑完返回 `full.md` 路径。

- Auth：优先读环境变量 `MINERU_API_TOKEN`；未设置时回退本目录 `token.txt`（在 https://mineru.net 申请，禁提交或打包）。
- Limits：单文件上限 200 MB、200 页，超出将失败。
- Network：海外直链（GitHub、AWS 等）易超时，先下载到本地再传路径。
