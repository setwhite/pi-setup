---
name: html-card
disable-model-invocation: true
description: 生成 self-contained HTML 卡片。
---

# HTML 卡片

## Step — 生成 HTML 卡片

生成 HTML 卡片，写到当前工作目录，命名 `YYYY-MM-DD-标题.html`。

**Completion criterion**：文件已写入当前目录，除引用链接外无外部资源引用（zero external dependencies）。

## Reference — HTML 规范

- self-contained：字体用 system font stack，不加载 web font
- responsive：`<html lang="zh-CN">`，带 `<meta name="viewport">`
- interactive explainer（可选）：滑块调参、单步执行、点击联动等内联脚本控件；每次操作后把当前状态显示出来
- content-first design：无渐变、无 box-shadow 堆叠、无 backdrop-filter（no chartjunk）
- citation：引用标注可点击，脚注条目提供原始链接
