---
name: html-card
disable-model-invocation: true
description: 生成完全自包含的 HTML 卡片。
---

# HTML 卡片

## Step — 生成 HTML 卡片

生成 HTML 卡片，写到当前工作目录，命名 `YYYY-MM-DD-标题.html`。

**完成标准**：文件已写入当前目录，除引用链接外无任何外部资源引用。

## Reference — HTML 规范

- 完全自包含，不依赖任何 CDN 或外部资源
- 字体使用系统栈，不加载 web font
- `<html lang="zh-CN">`，带 `<meta name="viewport">`，移动端可读
- 可以加可交互解释器：滑块调参、单步执行、点击联动等内联脚本控件；每次操作后把当前状态显示出来
- 设计服务于阅读，不为炫技。无渐变、无 box-shadow 堆叠、无 backdrop-filter
- 引用标注可点击，脚注条目提供原始链接
