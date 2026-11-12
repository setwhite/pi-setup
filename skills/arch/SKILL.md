---
name: arch
disable-model-invocation: true
description: 定模块边界、依赖方向与测试 seam，维护 ARCHITECTURE.md 与模块文档。
---

# 架构

只在结构会变时跑：新项目、新模块、依赖方向变化、出现新 seam。结构不变就回一句「不改」。

输入是 `docs/decisions/` 里本轮拍板的选型，加上现有代码。跨模块重构先出 RFC 给用户，批了再动结构。

## 定结构

- 按功能分目录，不按层。
- 模块边界按能独立读懂、独立替换的单位划。跨模块只走公开接口。
- 模块表写职责与允许的依赖方向。目录布局指向代码。
- 名字写职责。`utils`、`common` 这类词不算名字。
- 签名、异常、字段以代码为准。`docs/modules/` 只写用法与取舍。

## 定 seam

spec 的验收要写「在哪测」，所以 seam 先定。

- seam 是测试唯一能碰的边界。数量越少越好，取能满足本轮全部行为的最高那层，spec 的验收只许落在清单内。
- 把 seam 清单交给用户确认，再写进文档。
- 每份 spec 都要有模块承接。

## 写入

写 `docs/ARCHITECTURE.md` 与 `docs/modules/<module>.md`。位置与索引按 `../_shared/docs-rules.md`。

写完提示用户运行 `/skill:spec`。
