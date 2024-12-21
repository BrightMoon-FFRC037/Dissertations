# 说明
统计里面的区间估计和假设检验有密切联系。这种关系就好比，正向推导与反证法的关系。下面给出一些参量和术语的对应关系。


|区间估计的统计量|假设检验的统计量|
|-|-|
|枢轴量<br>Pivotal Value|检验统计量<br>Test Statistics|
|置信水平<br> $1-\alpha$ |检验水平<br> $\alpha$ |
|临界值|临界值|
|置信区间|否定域|

这二者本质上解决的问题相同，描述的现象相同，但是处理问题的流程和思路又有区别，需要注意。

# 假设检验中的检验统计量
补充一下，关于等号的检验，都可以修正转化为对不等号的检验，相当于和临界值比较之前，进行了不等式放缩。

## 服从 $N(0,1)$ 分布的检验统计量
### 一个正态总体的期望值检验（已知方差）
已知 $\sigma^2,H_0:\mu=\mu_0$

$$
N=\frac{\bar X-\mu}{\sqrt{\frac{\sigma^2}{n}}}=\frac{\bar X-\mu_0}{\sqrt{\frac{\sigma^2}{n}}}\sim N(0,1)
$$

## 服从 $\chi^2$ 分布的检验统计量
### 分布函数检验（拟合优度检验）
已知分布是零假设，
可以有力地否定分布函数。


对 $\nu_i$ 进行标准化然后求平方和。

$$
V=\sum_{i=1}^{m+1}\frac{(\nu_i-np_i)^2}{np_i}\sim \chi^2(m)
$$

### 独立性检验
独立性是零假设，
可以有力地否定独立性。

$$
\sum_{i,j\in \{1,2\},i\neq j}\frac{(nP(A_iA_j)-nP(A_i)P(A_j))^2}{(nP(A_i)P(A_j))^2}\sim \chi^2(1)
$$

### 一个正态总体的方差检验

$H_0:\sigma^2=\sigma _0^2$

$$
W=\sum_{i=1}^n \frac{(X_i-\bar X)}{\sigma^2}
=\sum_{i=1}^n \frac{(X_i-\bar X)}{\sigma_0^2}\sim \chi^2(n-1)
$$

## 服从 $F$ 分布的检验统计量
### 线性回归问题中的相关性检验
线性无关是零假设，
可以有力地肯定线性相关性。

$$
F=\frac{U}{\frac{Q}{n-2}}\sim F(1,n-2)
$$

这里的 $U,Q$ 分别为回归平方和与残差平方和。

$$
U=\sum_t(\bar y-\hat y_t)^2=\hat b^2 l_{XX}
$$

$$
Q=\sum_t(y_t-\hat y_t)^2=l_{YY}-U
$$

这种检验等价于用相关系数 $R$ 进行检验。

### 两个正态总体的方差检验
####  $H_0:\sigma_1^2=\sigma_2^2$

$$
F=\frac{\frac{S_1^2}{\sigma_1^2}}{\frac{S_2^2}{\sigma_2^2}}=\frac{S_1^2}{S_2^2}\sim F(n_1-1,n_2-1)
$$



## 服从 $t$ 分布的检验统计量
### 一个正态总体的期望值检验
未知 $\sigma^2,H_0:\mu=\mu_0$

$$
T=\frac{\bar X-\mu}{\sqrt{\frac{S^2}{n}}}=\frac{\bar X-\mu_0}{\sqrt{\frac{S^2}{n}}}\sim T(n-1)
$$

### 成对数据的期望值检验
$H_0:\mu_z=0$
做差化成正态单总体（差值服从正态分布，各自未必服从）

$$
Z=X-Y
$$

转化为正态单总体的情况。

### 两个正态总体的期望值检验


#### 已知 $\sigma_1^2=\sigma_2^2,\ H_0:\mu_1=\mu_2$ 
对 $\bar X-\bar Y$ 标准化：


$$
T=\frac{\bar X-\bar Y-(\mu_1-\mu_2)}{\sqrt{\frac{S_1^2}{n}+\frac{S_2^2}{n}}}=\frac{\bar X-\bar Y}{\sqrt{\frac{S_1^2}{n}+\frac{S_2^2}{n}}}\sim t(2n-2)
$$

#### 已知 $\sigma_1^2\neq\sigma_2^2,\ H_0:\mu_1=\mu_2$ 

对 $\bar X-\bar Y$ 标准化：


$$
T=\frac{\bar X-\bar Y-(\mu_1-\mu_2)}{\sqrt{\frac{S_1^2}{n}+\frac{S_2^2}{n}}}=\frac{\bar X-\bar Y}{\sqrt{\frac{S_1^2}{n}+\frac{S_2^2}{n}}}\sim t(m)
$$

其中的 $m$ 根据 Behrens-Fisher 问题给出的近似值代入。

### 成功率（比率）的假设检验


