---
name: coding
disable-model-invocation: true
description: 代码风格、红/绿 TDD、lint/test。
---

# Coding

## Step 1 — 红/绿 TDD

## Step 2 — lint + test

改完运行项目的 lint + test；修不了就给出报错。

## 代码风格

### Python

- 函数体 ≤ 50 行、嵌套 ≤ 3 层、单文件 ≤ 300 行
- 位置参数 ≤ 3 个，超出改对象/数据类传参
- 魔法数字用命名常量（0、1、-1 等公认语义除外）
- 函数签名、类属性、数据类字段完整类型标注

### 通用

- 修改/新增代码保持现有代码风格
- 文档只做索引与事实陈述，信息唯一，不用文字复述代码逻辑
