---
name: html-card
description: 生成完全自包含的 HTML 卡片。
disable-model-invocation: true
---

## Step — 生成 HTML 卡片

生成 HTML 卡片，写到当前工作目录，命名 `YYYY-MM-DD-标题.html`。

**完成标准**：文件已写入当前目录。

## Reference — HTML 规范

- 完全自包含，不依赖任何 CDN 或外部资源
- 字体使用系统栈，不加载 web font
- 设计服务于阅读，不为炫技。无渐变、无 box-shadow 堆叠、无 backdrop-filter
- 响应式：移动端可读
- 引用标注可点击，脚注条目提供原始链接
