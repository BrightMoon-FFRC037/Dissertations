# PDE的常见类型及其关联
波动方程描绘波动，包括机械波，电磁波，波函数。

耗散方程描绘不可逆过程，包括热传导，粒子扩散。

波动方程和耗散方程，不随时间变化的时候，形成稳定问题，也就是Laplace方程。就是波动方程、耗散方程删去了关于时间求偏导的项。

稳定问题引入激励源（受迫振动产生器，电荷，热源，粒子源），构成Poisson方程。就是Laplace方程多了非齐次项。

Helmholtz方程，是波动方程和耗散方程，分离掉时间变量后的**共同归宿**。物理上，描绘的是具有变量分离性质的解，的空间分布状况。Laplace方程也可以看作Helmholtz方程的特殊情况。
# PDE的解法
PDE 有若干解法，包括行波法、积分变换法、Green函数法，还有分离变量法（驻波法）。

行波法和驻波法（分离变量法），从波动角度看正好对应。之所以分离变量也叫驻波法是因为，其中的本征函数（空间部分）满足齐次边界条件，物理上形成驻波。

# PDE的级数解法
PDE的级数解法被称为“分离变量法（驻波法）”，但我认为称之为级数解法更准确。我在下面梳理一下这种解法的思路。
## 如何理解级数解的各项变量分离属性
我们猜PDE的解是级数解，级数的每一项具有变量分离的性质。其中，一个变量的分函数是“基底（本征函数）”，另一个变量的分函数是“系数（对应基底而言）”

$$
u(x,t)=\sum_n^\infty T_n(t)X_n(x)
$$

比如上面的式子， $X_n(x)$ 是基底， $T_n(t)$ 是系数。

**上面这种观点下的解具有局限性。由于基底是本征函数，从而这种观点下的解对应的定解问题，边界条件一定是齐次的。**

**对于非齐次的边界条件，还应该补上一个齐次化函数，这个函数是个有限和，各项依然变量分离，但是就无所谓什么基底了，因为这主要是非齐次的边界条件决定的。**

## 如何找到基底
### 找特征向量做基底
问题在于，怎么找到基底 $X_n(x)$ 。这要通过齐次方程和齐次边界条件，经过分量变量后，构造的本征值问题求解。换言之，我们找的基底，不是随便的基底，而是“特征向量”作为基底。

求解特征向量，是对于线性映射而言的，而线性映射是定义在线性空间上。

齐次的方程写成微分算子的形式，是一个线性的算子，因而是线性映射；齐次的边界条件，约束了一个线性空间。

它们对于加法和数乘（线性叠加运算）分别具有“保持运算”和“封闭性”。

相反的，非齐次方程对应的算子不是一个线性算子；非齐次边界条件约束出来的子集，也不构成线性空间。因为它们对于加法和数乘（线性叠加运算）分别不具有“保持运算”和“封闭性”。

### 这样的基底还是正交的

很巧的是，波动方程，耗散方程，稳定方程，它们对应的线性映射都是自伴的，从而可以正交相似对角化，找到彼此垂直的特征向量。


## 如何确定系数
对于正交的基底，可以通过内积（积分），求系数。

## 根据齐次与非齐次对定解问题分类
### 定解问题的三要素
* 方程齐次与否
* 初始条件（同一时间起点）齐次与否
  * 对于稳定问题，则是对于“剩余边界条件”齐次与否
* 边界条件（不同空间边界）齐次与否
  
### 边界条件的齐次化是首要的
将边界条件齐次化，分量变量构造本征值问题，求解本征函数。这是级数解法的第一步。

### 边界条件的齐次化是有代价的
边界条件的齐次化，可能使得原本齐次的方程，变得不齐次，也可能使得原本齐次的初始条件变得不齐次。但这都是次要的。找到“基底”最重要，确定“系数”是体力活。

边界条件齐次化，且不引发方程的非齐次化，成为同时齐次化，这是大好事。

边界条件齐次化，且不引发初始条件非齐次化，这也是一件好事。

### 如何将边界条件齐次化
我们应该假设齐次化函数（承担非齐次边界条件）具有有限和的形式，其中每一项，均为变量分离形式。这样的假设有助于求解。就好像我们假设PDE具有各项变量分离的级数解一样。

这样的假设下，应优先尝试同时齐次化方法。

*非齐次边界条件的齐次化是复习要解决的第一个问题*

### 其它非齐次项如何处理
其它的非齐次项包括：
* 方程的非齐次项
* 初始条件的非齐次项
* 或剩余边界条件的非齐次项

对于这三种非齐次项的的处理的内在逻辑是一致的。都是先按照“基底”展开，然后匹配“系数”。

具体而言，是把解 $u(x,t)$ 和非齐次项 $f(x,t)$ 同时按照基底 $X_n(x)$ 展开。

*任意函数按照本征函数的展开概念简单，操作复杂，是复习的第二个要点。这一点是个大问题，涉及到Legendre, Bessel 等函数的性质及其运用。这是最难的一点。*

$$
u(x,t)=\sum_n^\infty T_n(t)X_n(x)
$$

$$
f(x,t)=\sum_n^\infty S_n(t)X_n(x)
$$

无论PDE方程，还是初始条件，还是剩余边界条件实质上都是方程（关于 $u$ 和 $f$ 的方程）。根据这个方程（带入 $f$ 和 $u$ 的级数表达式），逐项匹配系数即可。

初始条件和剩余边界条件都是代数方程，匹配系数也只是求解代数方程，不难。得到：

$$
T_n(0),\ T'_n(0)
$$

由于PDE是微分方程，匹配系数实际上是在解ODE。结合上上面由初始条件匹配好的系数，实际上是在求ODE的初值问题。也不能说难，但也未必好求。

*求解常微分方程的初值问题，尤其是带非齐次项的常数变易法，是复习的第三点*

## 一般流程
* 边界条件齐次化
  * 尽量同时齐次化，不要给方程引入非齐次项
  * 但也不要怕给方程引入非齐次项
  * 如果边界条件已经齐次，只有方程非齐次，且形式简单，可以考虑求非齐次方程的特解，方法同求齐次化函数一样，转化为非齐次ODE的边值问题。这样做，下面就不用对方程的非齐次项展开了。
* 分离变量求解本征值问题
* 用本征函数形式上展开代求的解
* 用本征函数展开所有其它非齐次项
* 分别将展开式（级数表达式）带入PDE和初始条件或者剩余边界条件，逐项匹配系数
  * 匹配系数是求代数方程或者ODE初值问题的过程

*边界条件的两种齐次化方法，方程的两种齐次化方法。这四种方法的选取组合，决策问题应该是复习的第五个要点*

# 本征值问题的多样性
## 变换坐标系
为了分离变量，要保证边界条件的“边界”是变量分离的形式。这就要求选取相应的坐标系。我怀疑不规则形状，可以通过保角变换化成规则形状。
## 本征值问题形式的决定因素
方程的形式，边界条件的形状影响着本征值问题的形式。

*什么样的方程与什么样的边界形状，对应什么样的本征值问题和本征函数，这是复习的第四个要点*

有的本征值问题很好求，比如简谐方程，Euler方程，因为它们都可以化成常系数的ODE。他们的解是三角函数或指数函数和幂函数这样的初等函数。

有的本征值问题很难求，比如Legendre 方程，Bessel 方程等等。他们的解是特殊函数。
## 本征值的统一物理图景
这个物理图景应该是驻波，只不过是不同方向上的驻波。横向纵向，径向角度方向......这是不含时的，表示能量和波动幅度的空间分布。
# 特殊函数
# 特殊函数的由来
PDE分离变量的ODE方程的解，或是ODE和齐次边界构成的本征值问题的本征函数。
## Legendre 多项式
这是与 $\phi$ **无关**的Helmholtz方程在球坐标系 $(r,\theta,\phi)$ 下分离变量后， $\theta$ (与 $z$ 轴夹角)部分构成的本征值问题的本征函数。

本征值问题中的齐次边界条件，对于筛选、约束Legendre方程的解，使之截断成为多项式，有重要意义。
## 连带 Legendre 函数
这是与 $\phi$ **有关**的Helmholtz方程在球坐标系 $(r,\theta,\phi)$ 下分离变量后， $\theta$ (与 $z$ 轴夹角)部分构成的本征值问题的本征函数。

本征值问题中的齐次边界条件，对于筛选、约束Legendre方程的解，使之截断成为多项式，有重要意义。
## Bessel 函数
Bessel方程来自Helmholtz方程在柱坐标系下分离变量，半径方向部分。
这是Bessel方程的一个解。注意，并没有添加本征值问题的齐次边界条件约束。

事实上，Bessel函数参与到PDE问题中，不一定是以本征函数的身份出现。

但是，在本征值问题中，作为本征函数出现的Bessel函数和作为本征函数出现的三角函数具有类似性。而二者都不同于永远作为本征函数出现的Legendre多项式和连带Legendre函数。

>$$
\sin(m x) \sim J_m(k_{mi}x)
>$$
## Neumann 函数
这是Bessel方程与Bessel函数线性无关的另一个解。同样，并没有添加本征值问题的齐次边界条件约束。

事实上，Neumann函数参与到PDE问题中，不一定是以本征函数的身份出现。
## 两种 Hankel 函数
这是Bessel函数和Neumann函数，经过正交变换，得到的另一对柱函数。不一定涉及本征值问题，不再赘述。
>上面的四种柱函数，可以和三角函数做一个类比

>$$
\sin(\omega x) \sim J_\nu(x)
>$$

>$$
\cos(\omega x) \sim N_\nu(x)
>$$

>$$
e^{i\omega x} \sim H^{(1)}_\nu(x)
>$$

>$$
e^{-i\omega x} \sim H^{(2)}_\nu(x)
>$$

## 球Bessel函数
这是Helmholtz方程在球坐标系下分离变量，径向方向ODE的解。

由于和Bessel函数相关，（从Bessel函数修正得到）故得此名。

根据四种柱函数的关系，可以定义球Neumann函数，两种球Hankel等等。

同样的，它们也不一定作为本征函数出现。


# 特殊函数的表示方法
## 特殊函数的符号记法
* Legendre 多项式
  
$$
P_l(x)
$$

称为 $l$ 次Legendre多项式，这里 $l$ 是参数， $x$ 才是变量。

* 连带Legendre 函数
  
$$
P_l^m(x)
$$


称为 $m$ 阶， $l$ 次连带Legendre函数，这里 $m,\ l$ 是参数， $x$ 才是变量。

* Bessel 函数
  
$$
J_\nu(x)
$$


称为 $\nu$ 阶， Bessel函数，这里 $\nu$ 是参数， $x$ 才是变量。

* Neumann 函数
  
$$
N_\nu(x)
$$


称为 $\nu$ 阶， Neumann函数，这里 $\nu$ 是参数， $x$ 才是变量。


>关于特殊函数的讨论，其实方法和基本初等函数是一致的。这一点可以和三角函数做一个类比。

>$$
\sin(\omega x +\phi)
>$$

>这里面， $\omega,\ \phi$ 都是参数，只有 $x$ 是变量。我们讨论的是一类三角函数，并不是一个三角函数。关于三角函数，我们也不确切的知道所有点的取值，而只知道它的关键点取值。我们研究它的对称性，研究不同 $\omega,\ \phi$ 函数之间的关联（诱导公式等等）。要想更粗暴的理解三角函数，可以把它做Taylor展开，用级数表达式理解。三角函数也可以看作由经典的 $y''=\omega ^2 y$ 这样一个微分方程的解而引出。

## Laurent 展开表示法
* Legendre 多项式在 $x=0$ 处展开
* Legendre 多项式在 $x=1$ 处展开
## 微分表示法
* Legendre 多项式的微分表示
## 生成函数
在生成函数 $f(x,t)$ 关于 $t$ 的Laurent展开中，各项系数是特殊函数。
* Legendre 多项式的生成函数
* Bessel 函数的生成函数
# 特殊函数的对称性
## 奇偶性
* Legendre 多项式的奇偶性与次数的奇偶性相一致
* 整数阶 Bessel函数的奇偶性与阶数的奇偶性一致
# 特殊函数的特殊点取值
* 任意次Legendre多项式在 $x=1$ 处取值为 $1$ 
* $l$ 次Legendre多项式在 $x=-1$ 处取值为 $(-1)^l$
* 奇数次Legendre多项式是奇函数，在 $x=0$ 处取值为 $0$
* 0阶Bessel函数在 $x=0$ 处取值为 $1$
* 其它阶数的Bessel函数在 $x=0$ 处取值为 $0$
# 同类型不同参数的特殊函数的关联
## 相邻参数的递推关系
### 柱函数
#### Legendre多项式
相邻三次，构成了一个非线性的二阶递推关系。

这个递推关系是根据生成函数两侧求导（右侧逐项求导）然后比对系数得到的。
#### Bessel函数
通过求导，构建的相邻两阶柱函数的递推关系。
>实际上这是柱函数的定义，也是Bessel方程解的充要条件

>这个关系，也可以通过相似变换来认识。（正）求导算符的相似算符，可以使Bessel函数降一阶。负求导算符的相似算符，可以使Bessel函数升一阶。相似关系的过渡变换不同，正求导算符用正幂函数过渡，负求导算符用负幂函数过渡。

如果不涉及导数，柱函数函数相邻三阶，构成一个非线性的二阶递推关系。

## 相反参数的关系
* Bessel函数关于阶数的奇偶性（整数）与阶数自身的奇偶性一致
* Legendre函数关于阶数（而非次数）的相反对应者，线性相关。符号上的奇偶性与阶数自身的奇偶性一致，绝对值部分比较复杂。
# 和特殊函数的内积运算
## Legendre 函数
### 幂函数 与 Legendre 多项式的内积

$$
\int_{-1}^{+1}x^kP_l(x)dx
$$

* $k$ 与 $l$ 奇偶性相反，则内积为零。
  这说明偶数次幂函数，在奇数次Legendre多项式下投影为零，反之亦然。
  * 直接根据积分限和被积函数的对称性就可以得到！
* $k$ 小于 $l$ 则内积为零。
  这说明幂函数，在比自己次数高的Legendre多项式下，投影为零。
  * 使用Legendre多项式的微分表达式，便于分部积分
  * 每分部积分一次，向 $x^k$ “转移”了一个“负求导” $-\frac{d}{dx}$ 。
  * 总共分部积分 $l$ 次。
  * $k$ 小于 $l$ 扛不住这么多次求导。
  * 换言之，用Legendre多项式展开幂函数的时候，用不到比自己幂次高的Legendre多项式
* 只有 $k$ 大于 $l$ 且 二者奇偶性相同时，内积才非零。这时，通常考虑下面的式子。
  

$$
\int_{-1}^{+1}x^{l+2n}P_l(x)dx=2^{l+1}\frac{(l+2n)!(l+n)!}{n!(2l+2n+1)!}
$$

* 这个式子不难得出：
  * 把转移到 $x^k=x^{l+2n}$ 上面的求导算子，导进去。
  * 用 $(-1)^l$ 来颠倒调整微分表达式中 $(x^2-1)^l$ 顺序。
  * 换元化成 $B(p,q)$ 形式。
    * 注意有个系数 $2$ 先在积分限折半时被除掉，又在 $dt$ 处恢复，总的结果是没有产生。
    * 此外注意 $dt$ 相比于 $dx$ 会吃掉一个 $x$ 进到 $d()$ 里面。这就是产生双阶乘（半整数 $\Gamma$ 函数的原因）。
  * 进而利用 $\Gamma$ 写成阶乘形式。
    * 注意 $B$ 换 $\Gamma$ “鸡在河上飞”
    * 半整数 $\Gamma$ 比的处理流程
      * 半整数步进一的截断阶乘，通分，化成步进二的**奇数**截断双阶乘，提出 $2$ 的幂次
      * 用阶乘除阶乘，构造截断阶乘。用偶数双阶乘除偶数双阶乘，构造偶数截断双阶乘。
      * 用上面两个截断阶乘，构造级数截断双阶乘。
      * 这么做完全是因为，偶数双阶乘可以化为单阶乘，但是奇数双阶乘不可以。
### 多项式 与 Legendre 多项式的内积
多项式可以看作幂函数的线性组合，根据内积的双线性性质，可以轻松得到。

作为特例，一个最有用的特例（得到模平方），考虑 Legendre 多项式与其自身的内积。


$$
\int_{-1}^{+1}P_l(x)P_l(x)dx=\frac{2}{2l+1}
$$


那么，把后一个视作基底，前一个视作多项式。只有最高次幂有贡献。

结合Legendre多项式在 $x=0$ 点处的幂级数表达式，可以知道最高次幂的系数，从而得解。

### 幂函数与Legendre多项式的乘积 与 Legendre 多项式的内积


$$
\int_{-1}^{+1}x^mP_k(x)P_l(x)dx
$$


原则上，这类问题已经解决，但是有更简便，更实用的方法。

关于Legendre函数的二阶递推，是非线性的，变系数的。
存在于系数中的 $x$ 看起来丑陋，却有它的用处。既可以用它“产生”一个 $x$ 也可以用它“吃掉”一个 $x$ 。

在这里，我们利用二阶递推关系，“吃掉”幂级数中的 $x$ 将问题化为Legendre多项式与其自身的内积（相对于多项式与Legendre多项式的内积，更为简洁）。

### 复合 $(1\pm x)$ 的函数与Legendre多项式的内积


$$
\int_{-1}^{+1}(1+x)^kP_l(x)dx
$$


$$
\int_{-1}^{+1}\ln(1-x)P_l(x)dx
$$


$$
\int_{-1}^{+1}(1-x)^{\alpha}P_l(x)dx
$$


这些问题不只是上面结论的迁移，而是方法的迁移。

上面的讨论能够奏效，关键在于计算非零项内积的步骤。这个方法是重要的。

首先是把Legendre用微分表达式写出来，然后多次分部积分，转移求导算子。最后化成 $B$ 函数，表达成阶乘的形式。

之所以这类问题可以这么做，是因为他们求导后，自己的形式稳定，而且和Legendre微分表达式的 $(x^2-1)$ 可以合并整理进入 $B$ 函数。

微小的区别在于整理成 $B$ 函数时候的换元方法，不再是 $t=x^2$ 。
通常是 $2t=1+x$ 。因为 $\pm x\in(-1,1),1\pm x\in(0,2),t\in(0,1)$ 定义域复合，并且形式也符合。

### 幂函数 在 Legendre 多项式基底组下的展开
* 广义Fourier 展开法：这是一个向量，在正交基底组下面展开的标准方法
  * 根据内积公式和模方公式，求广义Fourier系数。
  * 注意，根据 $k,l$ 的大小关系与奇偶性，做一定事先快速筛选，化简计算。
* 幂级数与Legendre多项式的互相展开法（三角形过渡矩阵，迭代求逆）
  * 考虑Hilbert空间的两组基底 ${\{x^l\}}$ 与 ${\{P_l(x)\}}$ 
  * 二者之间的过渡矩阵应该是三角形的（根据前面的讨论）。
  * 过渡矩阵的一种形式我们已经完全知晓，也就是各次Legendre多项式在各次幂函数下的系数。
  * 这样的矩阵求逆可以用，有规律迭代的方法完成。
  * 具体来讲，根据 $P_l(x)$ 的幂级数展开式，用 $P_l(x)$ 和 低次幂级数，表示最高次幂级数 $x^l$ 
  * 如此迭代，幂级数的次数越来越低，直到全部替换为Legendre多项式。

### 多项式 在 Legendre 多项式基底组下的展开
多项式看作幂函数的线性组合，原则上与方法上，结果易得。
### 连带 Legendre 函数与其自身的内积

$$
\int P_l^m(x)P_k^m(x)dx
$$

与处理 Legendre 多项式与幂函数的内积思路一致，都要通过分部积分，转移求导符号。

这里需要适用连带 Legendre 函数的微分表达式，启动分部积分的流程。

$$
P_l^m(x)=(-1)^m(1-x^2)^{\frac{m}{2}}\frac{d^m}{dx^m}P_l(x)
$$

也就是说，连带Legendre函数的微分表达式，涉及到对Legendre多项式的微分。

作为对比，或者继承，可以回顾一下Legendre多项式自身的微分表达式。

$$
P_l(x)=\frac{(-1)^l}{2^ll!}\frac{d^l}{dx^l}(1-x^2)^l
$$

可见， $1-x^2$ 一直是和Legendre函数密切相关的组分。这从初始换元公式就可以知道， $x=\cos(\theta),1-x^2=\sin(\theta)$ 

前面我们通过分部积分，把微分符号从 $(1-x^2)$ 转移到了幂函数上面。

这里我们通过分部积分，把微分符号从一个Legendre多项式，完全转移到了另一个Legendre多项式 $P_l(x)$ 

进而将问题转变为了Legendre多项式与多项式的内积，进而找最高次幂的系数就好了。

注意， $P_l^m(x)$ 的最高次幂也是 $l$ 


## Bessel 函数
### 幂函数 与 Bessel 函数的内积运算
**Bessel函数只有在齐次边界条件下，才作为本征函数而出现，才会讨论所谓内积**。 而作为本征函数出现的Bessel函数和一般的Bessel函数是有显著区别的。


$$
J_{\nu}(x)
$$


$$
J_{m}(k_{mi}r)=J_m(\mu_{mi}\frac{r}{a})=J_m(\mu_{mi}x)
$$


当然了，如果不从内积的角度看，仍然可以定义积分。
下面先考虑和一般的Bessel函数的积分，再看和作为本征函数的Bessel函数的积分。

$$
\int x^\mu J_{\nu}(x)dx
$$

处理方法和Legendre多项式相同的地方是多次分部积分。
不同的地方是，利用涉及导数的递推关系，分部积分。而不是用微分表达式分部积分。

处理问题也不一样。幂函数和Legendre多项式的内积是定积分，这里是不定积分。
前者因为是本征函数，作差项恰好总是被消掉。这里讨论一般的积分，消不掉。即便作为本征函数，也未必总是能被消掉。

这需要我们思考一个更根本的问题，化简的方向是什么？
化简的方向是为了拿掉积分号。而对于不定积分，只有下列形式，可以拿掉积分号。

$$
\int f'(x)dx=f(x)+C
$$


也就是说，我们目标是把被积函数化成某个已知函数的导数形式。
这就要利用柱函数的两个核心递推式。


$$
\frac{d}{dx}x^{\nu}J_{\nu}=x^{\nu}J_{\nu -1}
$$


$$
-\frac{d}{dx}x^{-\nu}J_{\nu}=x^{-\nu}J_{\nu +1}
$$


对于这个问题


$$
\int x^\mu J_{\nu}(x)dx
$$


只要 $\mu,n$满足下列关系中的一种，任务便宣告完成。


$$
\mu-\nu=1\text{ or }\mu +\nu=1
$$


如果满足任何一种，那就要通过分部积分，使得被积函数的幂次与Bessel函数的阶次之间的关系，向着这样的条件趋近。
#### 分部积分路径一
利用这个递推式（右侧向左侧使用），分部积分


$$
\frac{d}{dx}x^{\nu}J_{\nu}=x^{\nu}J_{\nu -1}
$$


每分部积分一次，关注被函数幂次变化如下：


$$
x^{\mu}J_{\nu}\to x^{\mu-1}J_{\nu+1}
$$


这是一种“双向奔赴”（改变相对位移，质心不变），朝着减法条件趋近，也就是说该路径适用条件是


$$
\mu-\nu=2n+1
$$


#### 分部积分路径二
利用这个递推式（右侧向左侧使用），分部积分


$$
-\frac{d}{dx}x^{-\nu}J_{\nu}=x^{-\nu}J_{\nu +1}
$$


每分部积分一次，关注被函数幂次变化如下：


$$
x^{\mu}J_{\nu}\to x^{\mu-1}J_{\nu-1}
$$


这是一种“保持距离的追赶”（改变质心，相对位移不变），朝着加法条件趋近，也就是说该路径适用条件是


$$
\mu+\nu=2n+1
$$


#### 路径选择
那么在着手处理之前，就应该首先判断是否可积、是否需要分部积分调整幂次与阶数、如何选取分部积分的路径。

* 可积的条件，相差或者相和，为正奇数。
* 相差正奇数，要让二者“双向奔赴”，用第一递推条件分部积分。
* 相和正奇数，要让二者“同向左移”，用第二递推条件分部积分。
#### 最终结果化简
根据Bessel函数的二阶递推关系，结果总可以用 $J_0$ ， $J_1$ 表示。

如果是作为本征函数的内积运算，一方面是定积分，另一方面涉及到零点，可以进一步简化形式。

### Bessel 函数与其自身的内积运算
对于Bessel函数，内积运算是比较狭隘的，作为函数取本征函数，不定积分取成特殊定积分的推论而存在。因此，一般先讨论不定积分，然后内积运算不言自明。

这类问题是通过Bessel方程出发得到的结论，而不是Bessel函数的某一种表达式。

通过类似 Wronski 行列式的构造方法，用错位相乘取积分的办法得到。ODE中的二阶项，积分后转化为导数做差。零阶项，就是所求。

作为本征函数的Bessel函数的模平方就是这样得到的。
### 级数表达式下 积分与求和换序
这是一种比较暴力的方法，但很多时候很奏效。
一般适用于定积分，包括无穷积分。然后利用Bessel函数的级数表达式，逐项积分再求和。

求和的方法有很多种：
* 利用逆Taylor展开
* 化 $B$ 函数，往往对应无穷积分
* 化 $\Gamma$ 函数，往往对应 $0\sim t$ 的积分
### 积分表达式下 积分与积分换序
Bessel函数好用的积分表达式是用复变函数作为被积函数的（复指数函数方便积分）。

这个积分表达式是通过Bessel函数的生成函数做变量代换，将幂级数形式转换为Fourier级数形式，再对应到Fourier系数公式（积分式），从而得到。

>所谓生成函数，一般是一个二元函数，对于另外一个变量做展开，我们关注的特殊函数成为了“系数”。

>作为Taylor展开的系数，对应于原函数的导数；

>作为Laurent展开的系数，对应于原函数的围道积分；

>作为Fourier展开的系数，对应于原函数在一个周期上的积分（内积）；

交换了积分顺序之后，内层的积分往往简单，外层的积分往往需要运用留数定理，或是其它办法解决。