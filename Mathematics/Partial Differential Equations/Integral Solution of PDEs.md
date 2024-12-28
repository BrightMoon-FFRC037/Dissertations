# 概述
PDE的积分解比级数解，更具备直观的物理意义：
* 积分解的物理意义
  * 对于波动方程：行波解
  * 对于耗散方程：Green函数解（点源的扩散/传热，和Random Walk模型相统一）
* 级数解的物理意义
  * 驻波的叠加

积分变换法解PDE的流程和原理如下：
* 对时间（有起始点）做单边Laplace变换
  * PDE变成了关于空间的ODE
  * 做Laplace变换的对象包括
    * 形式上的解式：代入方程变成ODE
    * 含时的边界条件：变成ODE的边值条件
  * 初始条件不做变换，但是会变成ODE的非齐次项
  * 求解ODE的边值问题
  * 对解式逆Laplace变换
* 对空间（无界区域）做Fourier变换
  * PDE变成了关于时间的ODE
  * 做Fourier变换的对象包括
    * 形式上的解式：代入方程变成ODE
    * 含空间的初始条件：变成ODE的初始条件
  * 边界条件是无穷远处有界
  * 求解ODE初值问题
  * 对解式逆Fourier变换
  
积分变换的解的形式有以下特点：
* 形式上的二重积分，实质上是二重卷积
* 二元被积函数实质上就是二元Green函数
* 这二重卷积的产生原因如下：
  * 对于Laplace变换
    * 空间部分的卷积产生于求解非齐次的ODE过程中
      * 无论是从常数变易法角度看 
      * 还是从Green函数方法角度看
      * 这是关于空间的
    * 时间部分的卷积产生于逆变换的时候运用的卷积定理
      * 逆变换的底物（正变换的产物）是一个乘积形式
      * 逆变换的产物（正变换的底物）是一个卷积形式
      * 这是关于时间的
  * 对于Fourier变换
    * 时间部分的卷积产生于求解非齐次的ODE过程中
      * 无论是从常数变易法角度看 
      * 还是从Green函数方法角度看
      * 这是关于时间的
    * 空间部分的卷积产生于逆变换的时候运用的卷积定理
      * 逆变换的底物（正变换的产物）是一个乘积形式
      * 逆变换的产物（正变换的底物）是一个卷积形式
      * 这是关于空间的

# 逆变换
这是运用积分变换法的难点，下面梳理常见的复杂逆变换，以及产生的场景。
## Laplace变换对
### 无界 有源 耗散方程 变换对
无界边界，默认函数值取值有界

$$
G(p)=\frac{1}{\sqrt{p}}e^{-\alpha \sqrt{p}}
$$

$$
g(t)=\frac{1}{\sqrt{\pi t}}e^{-\frac{\alpha ^2}{4t}}
$$

$$
F(p)=\frac{1}{\sqrt{4\kappa p}}e^{- \sqrt{\frac{p}{\kappa}}|x-x'|}
$$

$$
f(t)=\frac{1}{\sqrt{4\pi \kappa t}}e^{-\frac{(x-x') ^2}{4\kappa t}}
$$


无界情况，最终被积函数是一个正态分布的概率密度函数。
### 半无界 无源 耗散方程 变换对
边界条件有界的部分是标量 $u_0$ 

error function:

$$
\text{erf}(x)=\frac{1}{\Gamma (\frac{1}{2})}\int_{-x}^xe^{-\xi^2}d\xi
$$

complementary error function:

$$
\text{erfc}(x)=1-\frac{1}{\Gamma (\frac{1}{2})}\int_{-x}^xe^{-\xi^2}d\xi
$$

误差函数和余误差函数和正态分布的分布函数关系密切，但是又有细微区别。

$$
G(p)=\frac{1}{p}e^{-\alpha\sqrt{p}}
$$

$$
g(t)=\text{erfc}\frac{\alpha}{2\sqrt{t}}
$$

$$
F(p)=\frac{u_0}{p}e^{-\sqrt{\frac{p}{\kappa}}x}
$$

$$
f(t)=u_0\text{erfc}\frac{x}{2\sqrt{\kappa t}}
$$


半无界情况，最终结果和正态分布的分布函数相关。
### 有界 无源 耗散方程 变换对
这个时候就没有一个简单的公式了

Laplace变换后是涉及双曲三角函数。

反演，是一个级数（极点无穷多，留数无穷多）。
### 无界 无源 波动方程 变换对

$$
G(p)=e^{-\alpha p}
$$

$$
g(t)=\delta({t-\alpha })
$$

$$
H(p)=\frac{1}{p}e^{-\alpha p}
$$

$$
h(t)=\eta({t-\alpha })
$$

$$
F(p)=\frac{1}{2a}(\phi(x')+\frac{\psi(x')}{p})e^{-\frac{p}{a}|x-x'|}
$$

$$
f(t)=\frac{1}{2a}(\phi(x')\delta(t-\frac{|x'-x|}{a})+{\psi(x')}\eta(t-\frac{|x'-x|}{a}))
$$

$$
f(t)=\frac{1}{2}\phi(x')\delta(at-|x'-x|)+\frac{1}{2a}{\psi(x')}\eta(t-\frac{|x'-x|}{a})
$$

## Fourier变换对
### 无界 有源 耗散方程 变换对

$$
g(x)=\frac{1}{\sqrt{2\pi \sigma^2}}e^{-\frac{x^2}{2\sigma^2}}
$$

$$
G(k)=\frac{1}{\sqrt{2\pi}}e^{-\frac{k^2\sigma^2}{2}}
$$

$$
f(x)=\frac{1}{\sqrt{2\kappa(t-\tau)}}e^{-\frac{x^2}{4\kappa(t-\tau)}}
$$

$$
F(k)=e^{-\kappa k^2(t-\tau)}
$$

### 无界 无源 波动方程 变换对

直接按照定义做就好了，最后也得到行波解。

注意，反演的时候，三角函数拆成复指数，整理成变量代换的形式即可。

另外可以借助无关变量求导与逆变换的换序，化简计算。