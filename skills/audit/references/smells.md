# Smell 清单（Fowler, Refactoring ch.3）

仓库没写规范的地方靠它找线索。每条是「是什么 → 怎么办」：

- Mysterious Name：名字看不出它做什么、存什么 → 改名；想不出诚实的名字说明设计本身是浑的。
- Duplicated Code：同一段逻辑形状出现在多个 hunk 或文件里 → 抽出共同形状，两处都调它。
- Feature Envy：某方法摸别人的数据多过自己的 → 把方法挪到它羡慕的数据上。
- Data Clumps：同样几个字段或参数总是同行 → 捆成一个类型传。
- Primitive Obsession：用基本类型或字符串顶替领域概念 → 给这个概念一个自己的小类型。
- Repeated Switches：同一类型上的同一套 switch／if 级联反复出现 → 换成多态，或共用一个映射表。
- Shotgun Surgery：一处逻辑改动逼着你在很多文件里散着改 → 把一起变的东西收进同一个模块。
- Divergent Change：一个文件因为几件互不相干的事被改 → 拆开，让每个模块只为一个原因而变。
- Speculative Generality：为规格里没有的需求加的抽象、参数、钩子 → 删掉，收回到真有需要为止。
- Message Chains：`a.b().c().d()` 这种长导航，调用方不该依赖 → 在第一个对象上用一个方法盖住整条链。
- Middle Man：一个类或函数几乎只是转发 → 砍掉，直接调真目标。
- Refused Bequest：子类或实现类忽略、覆盖了继承来的大部分东西 → 弃掉继承，改用组合。
