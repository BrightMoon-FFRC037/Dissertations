import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
#二元函数的形式
N = 100 #参数离散取值的个数
p = np.linspace(0, 10, N)
v = np.linspace(0, 10, N)
p, v = np.meshgrid(p, v)#p,v各自是一个二维数组（坐标网格）
t = p*v

# Plot the surface.
ax.plot_surface(p, v, t, edgecolor='royalblue', lw=0.1, rstride=10, cstride=10,alpha=0.05)

ax.contour(p, v, t, zdir='z',offset=-50,cmap='coolwarm')
ax.contour(p, v, t, zdir='x',offset=15,cmap='coolwarm')
ax.contour(p, v, t, zdir='y',offset=15,cmap='coolwarm')


ax.set_xlabel('Pressure: '+r'$p=\frac{P}{P_0}$')
ax.set_ylabel('Volume: '+r'$v=\frac{V}{V_0}$')
ax.set_zlabel('Temperature: '+r'$t=\frac{T}{T_0}$')

ax.set(xlim=(0, 15), ylim=(0, 15), zlim=(-50, 100))
plt.show()