# 说明
数理统计这一部分的内容对于实际工作还是很有用的。下面根据实际问题的处理逻辑（与之相对的是知识点的建构逻辑）给出一些思路上的梳理，以及需要特别关注的问题。
## 思路
### 一个随机变量（被测物理量）
1. 估计分布（拟合）：绘制直方图，判断随机变量遵从的概率分布类型
2. 概率分布类型的检验（拟合优度检验）：采用假设检验
   1. 零假设是遵从某一种分布
   2. 构造检验统计量
      1. 目标是使之服从 $\chi^2$ 分布
      2. 于是对每一个区间内部的实验观测值，做标准化处理
      3. 然后平方求和
      4. 自由度是区间的分点个数
         1. 如果是对正态分布的检验，并且期望与方差采用的是样本估计值，那么自由度要再减去2
   3. 根据实验数据，计算出检验统计量的实际取值
   4. 根据检验水平，查表得出临界值
   5. 比较二者大小得出结论
## 概念辨析
1. 临界值
   1. 一般来说，作为检验工具的分布有下面几种
      1. 标准正态分布
      2. 各个自由度的t分布
      3. 各个自由度的F分布
      4. 各个自由度的 $\chi^2$ 分布
   2. 这些分布共同的特点是集中在0附近
      1. 也就是说，偏离中心的概率比较小
      2. 这个小概率对应检验水平
      3. 与此同时，靠近中心的概率比较大
      4. 这个大概率对应显著水平
      5. 通常显著水平和检验水平实现给定（这是自己提的要求，目标达到的精度）
      6. 通过概率对应找到的随机变量的特定取值就是临界值
      7. 一般来说，实验数据折合的数值，大于临界值（检验等式的时候），否定原假设，否则认为与原假设相容。
   3. 注意
      1. 是单侧（恒正）取值还是双侧（正负）取值
      2. 双侧取值注意对称性
      3. 注意数值表给出的上分位点还是下分位点