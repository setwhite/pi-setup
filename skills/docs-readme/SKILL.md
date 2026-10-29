---
name: docs-readme
disable-model-invocation: true
description: 写或改仓库根 README：安装、配置、文档索引、开发。
---

# 根 README

README 不限于几节。下面四节必须有，且按各节要求写；其余内容自由发挥。

写之前读 `../_shared/docs-rules.md`：项目事实归谁、什么时候留指针，都在那里。

## 安装

```bash
pnpm install
pnpm dev
```

## 配置

两份，顺序不能反：

1. 最小配置：照抄就能跑。
2. 完整配置：逐项列出，每项带注释，教别人怎么用、什么时候改。

```toml
# 最小配置
[database]
url = "sqlite://./app.db"

[server]
port = 8080
```

```toml
# 完整配置
[server]
port = 8080                      # 前端 proxy 指向它；改了这个数，vite.config.ts 也要改

[database]
url = "sqlite://./app.db"        # 生产换 postgres://；换完跑 uv run alembic upgrade head
pool_size = 5                    # 默认 5；调大先算数据库连接上限

[auth]
jwt_secret = "${JWT_SECRET}"     # 必填，从环境变量读
access_ttl = "15m"               # 默认 15m；调长会削弱吊销能力
```

## 文档

索引只放四类：架构文档、术语、模块文档、ADR。其他文档不进索引。

一个文件指文件，一个目录指目录。

```md
- [ARCHITECTURE](docs/ARCHITECTURE.md) — 模块边界与 seam，改结构前看
- [GLOSSARY](docs/GLOSSARY.md) — 术语唯一来源，命名前看
- [模块](docs/modules/) — 各模块的用法与取舍
- [ADR](docs/adr/) — 已决选型，改设计前扫一遍
```

## 开发

```bash
pnpm test              # 单元测试
pnpm lint              # 静态检查
pnpm exec tsc --noEmit # 类型检查
```

## Step 1 — 盘点

读现有 README、`docs/` 目录与构建配置文件，抽出 README 里出现的每条命令。

**Completion criterion**：四节各缺什么已列清；每条现有命令都能指到出处文件。

## Step 2 — 重写

四节按各节要求写；其余内容自由发挥。

**Completion criterion**：四节齐备且符合各节要求；配置含最小与完整两份；完整配置每项有注释。

## Step 3 — 校对

1. 命令逐条真跑，输出与 README 一致。
2. 相对链接、`路径:行号` 打得开。

**Completion criterion**：命令全部跑通，链接无死链。
