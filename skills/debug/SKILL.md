---
name: debug
disable-model-invocation: true
description: 根因调试协议：复现、二分隔离、只读验证假设、最小修复与回归测试。
---

# 根因调试

1. Reproduce：先复现为最小命令或失败回归测试；未复现前不改业务代码。
2. Isolate / Bisect：查 `git log` 与 `git diff`，缩小输入，在 seam 处二分定位归属。
3. Hypothesize & Verify：提出明确根因假设，用只读观测证伪或证实；一次只验一个。
4. Root-Cause Fix：针对已证实根因做最小修复，回归测试转绿。
5. Prevent Recurrence：排查同类缺陷模式，跑受影响范围的 QA。

汇报：根因（`文件:行号` + 证据）、改动摘要、回归测试输出、是否需补 prefactor todo。
