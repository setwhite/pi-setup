# 架构与设计规则

- Vertical Slice：按领域功能分目录，不按技术层水平切分；不用 utils、common、helpers、misc 命名模块。
- Deep Module：把复杂度封在内部，只暴露最小公开接口与生命周期；跨模块禁止直接引用内部文件（deep import）。
- Minimize Reader Load：砍掉只做转发的单调用方包装，尽量缩小可变状态作用域；新人应能在 30 秒内答清数据从哪来、谁能改它。
- Functional Core, Imperative Shell：核心逻辑写纯函数，IO、时钟与随机推到外层。
- Separate Before Serializing：并发或多执行体写同一目标前，先拆成各自独立的文件、key 或状态目录，读时再合并；只有单一写入者是真实不变量时，才用锁或原子操作串行化。
- Failure Modes：显式处理空值、超时、部分失败、幂等与并发竞争，不只写主路径。
- Subtract Before You Add：动功能或重构前，先删死代码、多余校验与薄包装，再在更简单的地基上加代码。
