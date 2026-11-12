---
name: docs-readme
disable-model-invocation: true
description: 写或改仓库根 README：安装、配置、文档索引、开发。
---

# 根 README

节数不限。下面四节按需写，写了就要符合要求。

## 安装

照抄就能跑的那几条命令。

```bash
pnpm install
pnpm dev
```

## 配置

分两份，顺序不能反：

1. 最小配置：照抄就能运行。
2. 完整配置：逐项列出，每项带注释，教别人怎么用、什么时候改。

```toml
# 最小配置
[database]
url = "sqlite://./app.db"
```

```toml
# 完整配置
[server]
port = 8080                  # 前端 proxy 指向它；改了这个数，vite.config.ts 也要改

[auth]
jwt_secret = "${JWT_SECRET}"   # 必填，从环境变量读
access_ttl = "15m"           # 默认 15m；调长会削弱吊销能力
```

## 文档

索引只放四类：架构、术语、模块、决策。其余文档不进索引。

一个文件指文件，一个目录指目录。

```md
- [ARCHITECTURE](docs/ARCHITECTURE.md) — 模块边界与 seam，改结构前看
- [GLOSSARY](docs/GLOSSARY.md) — 术语唯一来源，命名前看
- [模块](docs/modules/) — 各模块的用法与取舍
- [决策](docs/decisions/) — 已决选型，改设计前看一遍
```

## 开发

```bash
pnpm test              # 单元测试
pnpm lint              # 静态检查
pnpm exec tsc --noEmit # 类型检查
```

## 校对

1. 逐条运行命令，输出与 README 一致。
2. 相对链接与 `路径:行号` 打得开。
