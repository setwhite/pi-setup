---
name: docs-maintain
disable-model-invocation: true
description: 巡检并维护项目文档、根 README 与代码注释。
---

# 文档与 README 维护

范围：`docs/**`、根目录 Markdown（`README.md`、`AGENTS.md` 原地检查）、代码注释；只改文档和注释，代码逻辑问题记进报告。

## 1. 机械巡检

```bash
uv run python scripts/check_docs.py .
```

## 2. 语义对账

- Drift Check：核实路径、符号、命令、`--help` 与配置默认值是否和代码一致。
- Cleanup：术语对齐 `docs/GLOSSARY.md`，删已解决未决项，删多余或过时注释；文档里手写的可程序化规则建议改成脚本或测试。

## 3. 根 README 准则

按需保留四节：
- Quickstart：照抄即跑的最小命令。
- Configuration：先最小可运行配置，再带逐项注释的完整配置（用途、何时改、联动影响），顺序不能反。
- Docs Index：只链长期文档（`ARCHITECTURE.md`、`GLOSSARY.md`、`docs/modules/`、`docs/adr/`），不链 `specs/`、`todos/`、`audit/`。
- Verify：逐条实跑 README 命令，确保输出与链接有效。

## 4. 修复与收尾

- 直接修：把放错目录的文件挪回原位、修断链、补标题层级。
- 先批准：删除、合并、重写章节或改范围前，先列清单等确认。
- 收尾：直接输出报告（不写文件），分「文档」「注释」「代码疑点」列已改、已删和保留原因。
