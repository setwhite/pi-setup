---
name: mineru-ocr
description: 文档转 Markdown。当用户要读 PDF、Office 文档（docx/xlsx/pptx），或明确要求对图片做 OCR，或提到「OCR」「MinerU」时使用。
---

# MinerU 解析

## 步骤

### 运行解析脚本

`scripts/mineru_api.py`（本 skill 目录下，下称 `<脚本路径>`）。

```bash
uv run --no-project --with requests python "<脚本路径>" "<输入>" [-o 输出目录] [--pages 页码范围]
```

完成条件：退出码 0，且回复里有 `full.md` 的路径。

## 参考

- 首次运行前把 MinerU API token 写入 `token.txt`（本 skill 目录下）。token 在 https://mineru.net 申请。
- 单文件 ≤ 200 MB、≤ 200 页，超出会解析失败。
- 国外 URL（github、aws 等）会请求超时；先下载到本地再传路径。
