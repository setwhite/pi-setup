---
name: coding
disable-model-invocation: true
description: 按 docs/todos/ 或轻量改动执行垂直切片 TDD 开发，收尾前跑 QA。
---

# 开发

## 1. 起步

- 有 `docs/todos/` 时：
  - 先处理 `[~]` 待验收 todo，读最新 `docs/audit/` 报告：通过则经用户确认改 `[x]` 并提示 `/skill:docs-commit`；退回开发只修未通过项；退回规划则停下提示 `/skill:plan`。
  - 领首个 `[ ]` 且前置全 `[x]` 的 todo，读绑定 spec 与 `docs/ARCHITECTURE.md` 中的测试边界（seam）；缺验收标准或未登记边界时先提问。
- Fast-Path：无 todo 的轻量改动直接进入测试与开发循环。

## 2. 测试纪律

- Seam-Only Black-Box：只在登记的公开边界测行为；深模块重构后用新边界测试替换旧浅层单测，不层层叠加。
- One Behavior Per Test：一条测试只验一个行为契约，期望值取字面量、手算或规格原文。
- Boundary Fakes & Mocks：只在系统边界（外部 API、时钟、随机、必要时的 DB/FS）经依赖注入提供替身；本地轻量替身优先于 mock，外部接口按具体操作拆成 SDK 风格。
- Characterization Test：重构无测试覆盖的旧代码前，先补锁住现有行为的测试，全绿后再动结构。
- Banned Tests：不 mock 内部协作者或测私有方法；不用同款算法重算期望值；不一次性批量预写全部测试焊死未验证接口。

## 3. 红绿循环

- Vertical Slice TDD：一次一个边界、一条失败测试、刚好跑通的最小实现，不提前写后续代码。
- Local Micro-Refactor：绿灯后可改命名或抽模块内私有函数，不改公开接口；跨模块重构单拆前置重构 todo。
- Unexpected Red：非刚写的测试突然变红且原因不明时，停下排查或转 `/skill:debug`。

## 4. 收尾

- Self-Review Diff：跑 QA 前先扫 `git diff --stat` 和核心改动，清掉无关修改与调试残留。
- QA & Docs：按影响范围跑 QA；模块用法或取舍有变时同步 `docs/modules/<module>.md`。
- Handoff：有 todo 改 `[~]` 并提示 `/skill:audit`；轻量改动直接汇报。
