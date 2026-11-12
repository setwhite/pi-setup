---
name: mineru-ocr
description: 文档转 Markdown。当用户要读 PDF、Office 文档（docx/xlsx/pptx），或明确要求对图片做 OCR，或提到「OCR」「MinerU」时使用。
---

# MinerU 解析

```bash
uv run --no-project --with requests python scripts/mineru_api.py "<输入>" [-o 输出目录] [--pages 页码范围]
```

`scripts/mineru_api.py` 在本 skill 目录下。跑完给出 `full.md` 的路径。

- 首次运行前把 MinerU API token 写入本 skill 目录的 `token.txt`。token 在 https://mineru.net 申请。
- 单文件 ≤ 200 MB、≤ 200 页。超出会解析失败。
- 国外 URL（github、aws 等）会请求超时。先下载到本地，再传路径。
