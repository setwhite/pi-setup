---
name: audit
disable-model-invocation: true
description: 独立审计，逐条核对任务的验收标准与代码质量（ruff、basedpyright、pytest），只出意见，不改文件。
---

# 审计流程

用法：`/skill:audit <任务ID>`。未给任务 ID 则先询问。

## 前置条件

- **独立会话**：本会话若已执行过 coding 或写过仓库文件，停止，提示用户 `/new` 后重跑。
- **只读**：不修改 `docs/TODO.md` 与 git 已跟踪文件（虚拟环境与缓存目录除外）。

## Step 1 — 准备材料

1. 读取 `docs/TODO.md` 中该任务的交付物、验收标准、验收证据、前置。
2. 确认改动范围：以证据中的改动文件清单为准，再用 `git status --porcelain` 检查遗漏。已跟踪文件用 `git diff HEAD`，新文件用 `git ls-files -o --exclude-standard`。

**完成标准**：验收标准与改动范围明确。

## Step 2 — 核查

1. **AC 核对**：逐条亲自验证。TODO 中的证据只作线索，须本会话重跑。
2. **Quality gate**（均加 `--locked`，禁止改写 `uv.lock`）：
   - `uv run --locked ruff check`
   - `uv run --locked basedpyright`
   - `uv run --locked pytest`
3. **AGENTS 合规**：对照 `~/.pi/agent/AGENTS.md`，项目根 `AGENTS.md` 若存在也查。只查可机检条款：
   - 依赖或基建变更：`git diff HEAD -- pyproject.toml uv.lock`，有改动则列为 finding。
   - 吞异常、`# type: ignore`、硬编码路径或密钥：用 `rg` 定位。
   - 注释与 Docstring 是否为中文。

**完成标准**：每条 AC 有「达成 / 未达成 + 证据」；每个问题可定位到文件与行号。

## Step 3 — 输出

Finding 格式：`文件:行号 — 观察 — 依据（AGENTS 条款或 AC 编号）`。

- AC 允许「达成 / 未达成」判定。
- 禁止给 finding 标严重等级，禁止给实现方案。

```markdown
### AC 核对
| AC | 结论 | 证据 |
| --- | --- | --- |

### Findings
- `path/to/file.py:42` — 观察：… — 依据：AGENTS.md「Engineering」/ AC2

### 下一步
- 通过：由你勾选 `- [x] <任务ID>`，再运行 `/skill:coding` 领取下一个任务。
- 返工：回复「返工 <任务ID>」。
```

**完成标准**：结论可复现，未修改任何文件。
