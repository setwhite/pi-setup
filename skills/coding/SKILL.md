---
name: coding
disable-model-invocation: true
description: 按 docs/todos/ 或轻量改动执行垂直切片 TDD 开发，收工前跑 QA。
---

# 开发

## 1. 起步

- 有 `docs/todos/` 时：
  - 先结算 `[~]` 待审 todo，读最新 `docs/audit/` 报告：可交付则经用户批准改 `[x]` 并提示 `/skill:docs-commit`；回 coding 只修失败 AC；回 spec 停下提示 `/skill:plan`。
  - 领首个 `[ ]` 且前置全 `[x]` 的 todo，读绑定的 spec 与 `docs/ARCHITECTURE.md` seam；缺验收或未登记 seam 时先提问。
- Fast-Path：无 todo 的轻量改动直接进入测试与开发循环。

## 2. 测试纪律

- Seam-Only Black-Box：只在登记的 seam 上经公开接口测行为。
- One Behavior Per Test：一条测试验证一个行为契约，期望值取字面量、手算或规格原文。
- Characterization Test：重构无测试覆盖的旧代码前，先补锁死现有行为的测试，全绿后再动结构。
- Banned Tests：
  - Implementation-Coupled：mock 内部协作者、测私有方法、绕过 seam 查数据库或日志。
  - Tautological：用被测代码同款算法重算期望值。
  - Horizontal Slicing：批量预写全部测试再写实现，焊死想象接口。

## 3. 红绿循环

- Vertical Slice TDD：一次一个 seam、一条失败测试、刚好通过的最小实现，不预支后续测试。
- Local Micro-Refactor：绿灯后可改命名或抽模块内私有函数，不改 seam 与公开契约；跨模块重构单开 prefactor todo。
- Unexpected Red：非刚写的测试变红且原因不明时，停下排查或转 `/skill:debug`。

## 4. 收工

- Self-Review Diff：跑 QA 前先扫 `git diff --stat` 与核心改动，清掉无关变更与调试残留。
- QA：跑全套受影响检查（影响面说不准就跑全套）；模块用法或取舍有变时同步 `docs/modules/<module>.md`。
- Handoff：有 todo 时改 `[~]` 并提示 `/skill:audit`；轻量改动直接汇报结果。
