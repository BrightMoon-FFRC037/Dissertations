# 课本逻辑
* 函数在一点解析：函数在一点及其邻域内可导
* 解析区域：函数解析的点组成的区域
* 解析函数：在解析区域内，各点解析的函数
* Cauchy积分公式：解析函数在解析区域内成立
* 由Cauchy积分公式可知，解析函数不仅导数存在，任意高阶的导数都存在
* 由此解析函数，在解析点的，邻域型解析区域内，可以做Taylor展开
* 将参考点选在解析区域以外，解析函数在，环域型解析区域内，可以做Laurent展开

# 更顺畅的逻辑
* 函数在一点解析：函数在一点的邻域内，可以做幂级数展开（Taylor展开）
* 从而函数在该点导数存在，各个高阶导数也存在

# 概念辨析
## 解析函数、全纯函数、亚纯函数、整函数与解析区域
全纯函数与亚纯函数是课本没有的定义

* 解析函数（analytic function）等价于全纯函数（holomorphic function）：解析函数从可做幂级数展开定义，全纯函数从可导定义。在复变函数中，二者等价
* 亚纯函数（meromorphic function）是全纯函数的分式
* 全纯函数包含亚纯函数
  
确实可以只提解析函数

* 整函数是在全复平面解析的函数
* 换言之，解析函数可以存在不解析区域
* 不存在，不解析区域，的解析函数，是整函数
* Liouville定理说有界的整函数只能是常数
* 有界的整函数，等价于，在扩充的复平面（包含无穷远点）都解析的解析函数
* 换言之，在扩充的复平面上全部解析的函数，只有常数。常见的，$\sin z$ ， $e^z$ 在无穷远点都不解析...
  
## 解析与否、常点、奇点、极点
* 解析点等价于常点，不解析点等价于奇点
* 可去奇点在补充定义以前，属于奇点/不解析点，在补充定义以后，属于常点/解析点。如 $\frac{\sin z}{z}$ 在 $z=0$ 点。
* 不如把可去奇点一律归为解析点，在极限的意义下这是自然的
* 从极限的视角看
  * 解析点，极限存在且有限
    * 可去奇点，极限存在且有限，归为解析点
  * 奇点，上述以外的情况
    * 极点，极限存在但是无限，等于无穷远点 $\infty$
    * 本性奇点，极限不存在，不同趋近方式有不同值。

## Laurent展开与Taylor展开
* 展开区域不同
  * Taylor展开针对邻域
  * Laurent展开针对环域
* 但是邻域与环域在一定条件下是可以互换的
  * 将展开参考的分为有限点和无穷远点两类
  * 有限点的环域，也是无穷远点的环域
  * 环域外半径趋于无限，成为无穷远点的邻域
  * 环域内半径趋于零，有限点的邻域
* 展开参考点的极限不同
  * Taylor展开始终只包含幂级数的正则部分，在展开参考点，极限存在且有限
  * Laurent展开可以包含幂级数的主要部分，在展开参考点，极限存在且无限，或者不存在
  * 有限点的正则部分是正幂项，主要部分是负幂项
  * $\infty$ 的正则部分是负幂项，主要部分是正幂项
* 这意味着可能存在一个幂级数展开
  * 是有限点的Taylor展开，也是无穷远点的Laurent展开
  * 是有限点的Laurent展开，也是无穷远点的Taylor展开
  * 当然这对幂次和收敛于同时做出了苛刻要求
* 展开参考的不同（实用上）
  * Taylor以解析点为参考点
  * Laurent以不解析的奇点为参考点

## 留数与解析的关系
  * 留数应该定义成绕一点正向的围道积分除以 $2\pi i$
  * 留数定理应该叙述为：
    * 在有限点的留数等于Laurent展开 $z^{-1}$ 的系数，从属于主要部分
    * 在 $\infty$ 的留数等于Laurent展开 $-z^{-1}$ 的系数，从属于正则部分
  * 解析与否于留数非零与否
    * 不解析，留数也可以是零
    * 留数为零，不一定解析
    * 有限点解析，则，留数为零
    * 有限点留数非零，则，不解析
    * $\infty$ 解析，留数也可以非零
  * 从这一点回顾Cauchy积分公式对于无界情形：之所以要求 $\lim_{z\to \infty} f(z) = 0$ , 而非$\lim_{z\to \infty} z^2f(z) = 0$ ,是为了确保 $\infty$ 点，$\frac{f(z)}{z-a}$ 留数为零，不构成干扰。与解析与否无关。
  * 对于解析函数，只有有限个奇点，并且单值不含分支点，在扩充的复平面上，留数之和为零。分支点没有围道积分，从而没有留数。奇点无穷多，或许将不能求和
   
## 围道积分与边界积分
* 围道积分路径是单连通区域的边界，边界积分未必
* Cauchy定理指的是解析区域的边界积分是零，不能说明解析区域的围道积分是零
* 任意围道的围道积分是零，说明该区域存在原函数，该区域解析
* $\infty$ 的解析与否与留数非零与否无关，从而与围道积分非零与否无关