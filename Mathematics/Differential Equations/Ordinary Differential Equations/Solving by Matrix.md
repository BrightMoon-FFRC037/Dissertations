# 矩阵解法概述
* 一个高阶的ODE等价于多个一阶ODE构成的方程组
* 物理概念上，矩阵解法对应于系统的状态变量分析
* 而时域解法与变换域方法（系统函数方法）侧重于输入输出
> 我觉得矩阵解法的一个精彩之处在于，它将一个高阶ODE的特征根，与矩阵的特征值联系了起来。从此，特征根有了三个身份：高阶微分方程的特征根，一阶微分方程组系数矩阵的特征值，系统函数（Laplace变换）的极点

# 矩阵解法的思路
## 特征值与矩阵的同构关系

* $\lambda_i$ 为 $A$ 的特征值， $\vec{v_i}$ 为 $A$ 的特征向量
* 函数 $f(x)$ 同时作用于 $\lambda_i$ 与 $A$ 
* 得到 $f(\lambda_i),f(A)$
* $f(\lambda_i)$ 为 $f(A)$ 的特征值
* $\vec{v_i}$ 仍然为 $f(A)$ 的特征向量
## ODE

$$
\frac{d}{dt}\vec{y}(t)=A\vec{y}(t)+B\vec{e}(t)
$$

$$
\frac{d}{dt}\vec{y}(t)=A\vec{y}(t)
$$

## 形式解

$$
\vec{y}(t)= e^{At}\cdot \vec{y}(0)+e^{At}\cdot B*\vec{e}(t)
$$

$$
\vec{y}(t)= e^{At}\cdot \vec{y}(0)
$$


## 把特征值作为基底（对角化）
首先是把初始条件，按照 $A$ 的特征向量进行分解。

$$
\vec{y}(0)=\sum_i y_i(0)\vec{v_i}
$$

代入形式解

$$
\vec{y}(t)= e^{At}\cdot \vec{y}(0)=e^{At}\cdot \sum_i y_i(0)\vec{v_i}=\sum_i y_i(0)e^{At}\cdot\vec{v_i}
$$

根据

$$
e^{At}\vec{v_i}=e^{\lambda_i t} \vec{v_i}
$$

得到

$$
\vec{y}(t)= \sum_i y_i(0)e^{\lambda_i t}\cdot\vec{v_i}
$$



