# Laplace 和 Poisson 方程
这是稳定问题对应的方程，二者差别仅在于方程是否有非齐次项。数学上来看应该一起讨论。

半径方向不再是本征值问题。作为基底的本征函数都是从角度方向选取构造的。

## 球形边界
球形边界下，选取基底组：

$$
\{\cos(m\phi),\sin(m\phi)\},m=0,1,2,...
$$

$$
\{P^m_l(\cos \theta)\},l=m,m+1,m+2,...
$$

$$
w_{1lm}(\theta,\phi)=P^m_l(\cos \theta)\cos(m\phi)
$$

$$
w_{2lm}(\theta,\phi)=P^m_l(\cos \theta)\sin(m\phi)
$$

结合上半径方向的非本征值函数：

$$
w(\vec{r})=\sum_{lm}R_{1lm}(r)w_{1lm}(\theta,\phi)+\sum_{lm}R_{2lm}(r)w_{2lm}(\theta,\phi)
$$

$$
w(\vec{r})=\sum_{lm}R_{1lm}(r)P^m_l(\cos \theta)\cos(m\phi)+\sum_{lm}R_{2lm}(r)P^m_l(\cos \theta)\sin(m\phi)
$$

如果定解条件具有对称性（与某个变量无关）：
* 与 $\phi$ 无关： $m=0$


$$
w(\vec{r})=\sum_{l}R_{l}(r)P_l(\cos \theta)
$$

只有Legendre多项式作为本征函数

* 与 $\theta$ 无关： $l=0$
  
$$
w(\vec{r})=\sum_{m}R_{1m}(r)\cos(m\phi)+\sum_{m}R_{2m}(r)\sin(m\phi)
$$

只有三角函数作为本征函数
## 圆形边界

在圆形边界下，选取基底组

$$
\{\cos(m\theta),\sin(m\theta)\},m=0,1,2,...
$$

结合半径方向的非本征函数：

$$
w(\vec{r})=\sum_{m}R_{1m}(r)\cos(m\phi)+\sum_{m}R_{2m}(r)\sin(m\phi)
$$

## 补充
球形边界下，半径方向（非本征值问题）的齐次通解的基底是：

$$
{r^{l},r^{-l-1}}
$$

圆形边界下，半径方向的齐次通解的基底是：

$$
{1,\ln r,r^m,r^{-m}}
$$

通解基底前面的叠加系数的确定，取决于半径方向的剩余边界条件。如果方程还有非齐次项，还要考虑非齐次特解项。