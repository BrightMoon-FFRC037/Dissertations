# 波动方程

$$
\frac{\partial^2}{\partial^2t}u-c^2\nabla^2u=f(\vec{r},t)
$$

###### 各项变量分离形式的 级数解

$$
u(\vec{r},t)=\sum_n u_n(\vec{r},t)=\sum_n w_n(\vec{r})T_n(t)
$$

###### 空间维度
空间维度是一系列本征值问题(Helmholtz方程)

$$
\nabla^2w_n(\vec{r})+k_n^2w_n(\vec{r})=0
$$

$$
w_n(\vec{r})\text{ 的齐次边界条件}
$$

得到的本征函数作为基底，展开PDE定解条件中的非齐次项（方程的非齐次项与初始条件的非齐次项）

###### 时间维度
时间维度是一系列非本征值问题

$$
T''_n(t)+\omega_n^2T_n(t)=f_n(t)
$$

$$
T_n(0),T_n'(0)
$$

齐次通解的基底是：

$$
\{\cos({\omega_nt}),\sin({\omega_nt})\}
$$

利用本征函数作为基底，对PDE方程的非齐次项展开，匹配系数，得到一系列ODE方程的非齐次项。

利用本征函数作为基底，对PDE初始条件展开，匹配系数，得到一系列ODE初值。

###### 时空联系
本征值问题与非本征值问题通过本征值联系起来，下面的关系非常重要,也是与耗散方程的重要区别：

$$
\omega_n=k_nc
$$

# 耗散方程

$$
\frac{\partial}{\partial t}u-D\nabla^2u=f(\vec{r},t)
$$

###### 各项变量分离形式的 级数解

$$
u(\vec{r},t)=\sum_n u_n(\vec{r},t)=\sum_n w_n(\vec{r})T_n(t)
$$

###### 空间维度
空间维度是一系列本征值问题（和波动方程一样，都是Helmholtz方程的本征值问题）

$$
\nabla^2w_n(\vec{r})+k_n^2w_n(\vec{r})=0
$$

$$
w_n(\vec{r})\text{ 的齐次边界条件}
$$

得到的本征函数作为基底，展开PDE定解条件中的非齐次项（方程的非齐次项与初始条件的非齐次项）


###### 时间维度
时间维度是一系列非本征值问题

$$
T'_n(t)+\alpha_n T_n(t)=f_n(t)
$$

$$
T_n(0)
$$

齐次通解的基底是：

$$
\{e^{-\alpha_nt}\}
$$


利用本征函数作为基底，对PDE方程的非齐次项展开，匹配系数，得到一系列ODE方程的非齐次项。

利用本征函数作为基底，对PDE初始条件展开，匹配系数，得到一系列ODE初值。

###### 时空联系
本征值问题与非本征值问题通过本征值联系起来，下面的关系非常重要,也是与波动方程的重要区别：

$$
\alpha_n=Dk_n^2
$$


# Helmholtz方程的来源
Helmholtz方程的本征值问题，是波动方程和耗散方程为了寻找本征函数做基底，必然要面临的问题

$$
\nabla^2w_n+k_n^2w_n=0
$$

 $\{w_n\}$就是作为基底的本征函数组，当然，一般情况下是三元的本征函数，计数指标也是三个。
## 球形边界下的基底选取
在球形边界下，选取基底组

$$
\{\cos(m\phi),\sin(m\phi)\},m=0,1,2,...
$$

$$
\{P^m_l(\cos \theta)\},l=m,m+1,m+2,...
$$

$$
\{j_l(k_{li}r)\},i=1,2,3,...
$$

$$
w_{1lmi}(\vec{r})=j_l(k_{li}r)P^m_l(\cos \theta)\cos(m\phi)
$$

$$
w_{2lmi}(\vec{r})=j_l(k_{li}r)P^m_l(\cos \theta)\sin(m\phi)
$$

对应含时的原本的波动方程或是耗散方程的解则应该写为：

$$
u(\vec{r},t)=\sum_{lmi} T_{1lmi}(t)w_{1lmi}(\vec{r})+\sum_{lmi} T_{2lmi}(t)w_{1lmi}(\vec{r})
$$

$$
u(\vec{r},t)=\sum_{lmi}T_{1lmi}(t)j_l(k_{li}r)P^m_l(\cos \theta)\cos(m\phi)+\sum_{lmi}T_{2lmi}(t)j_l(k_{li}r)P^m_l(\cos \theta)\sin(m\phi)
$$

如果定解条件具有对称性（与某个变量无关）：
* 与 $\phi$ 无关： $m=0$

$$
u(\vec{r},t)=\sum_{li}T_{li}(t)j_l(k_{li}r)P_l(\cos \theta)
$$

>各项本征函数只有球Bessel和Legendre多项式


* 与 $\theta$ 无关： $l=0$

$$
u(\vec{r},t)=\sum_{mi}T_{1mi}(t)j_0(k_{i}r)\cos(m\phi)+\sum_{mi}T_{2mi}(t)j_0(k_{i}r)\sin(m\phi)
$$

>各项本征函数只有零阶球Bessel和三角函数

## 圆形边界下的基底选取
在圆形边界下，选取基底组

$$
\{\cos(m\theta),\sin(m\theta)\},m=0,1,2,...
$$


$$
\{J_m(k_{mi}r)\},i=1,2,3,...
$$

$$
w_{1mi}(\vec{r})=J_m(k_{mi}r)\cos(m\theta)
$$

$$
w_{2mi}(\vec{r})=J_m(k_{mi}r)\sin(m\theta)
$$


对应含时的原本的波动方程或是耗散方程的解则应该写为：

$$
u(\vec{r},t)=\sum_{mi} T_{1mi}(t)w_{1mi}(\vec{r})+\sum_{mi} T_{2mi}(t)w_{1mi}(\vec{r})
$$


$$
u(\vec{r},t)=\sum_{mi} T_{1mi}(t)J_m(k_{mi}r)\cos(m\theta)+\sum_{mi} T_{2mi}(t)J_m(k_{mi}r)\sin(m\theta)
$$


如果定解条件具有对称性（与某个变量无关）：
* 与 $\theta$ 无关： $m=0$

$$
u(\vec{r},t)=\sum_{i} T_{1i}(t)J_0(k_{i}r)
$$

>各项本征函数只有零阶Bessel函数

## 补充
通常意义下的“叠加系数”被含在我所说的 $T_n(t)$ 里面了。

对于波动方程，时间方面的ODE齐次通解的基底是三角函数。初始条件决定叠加系数。如果还有非齐次项，还有非齐次特解。

对于耗散方程，时间方面的ODE齐次通解的基底是指数函数。初始条件决定叠加系数。如果还有非齐次项，还有非齐次特解。

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

>只有Legendre多项式作为本征函数

* 与 $\theta$ 无关： $l=0$
  
$$
w(\vec{r})=\sum_{m}R_{1m}(r)\cos(m\phi)+\sum_{m}R_{2m}(r)\sin(m\phi)
$$

>只有三角函数作为本征函数
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
