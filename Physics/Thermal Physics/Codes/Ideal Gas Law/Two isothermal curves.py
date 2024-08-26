import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

colormap = mpl.colormaps['coolwarm']
ax = plt.figure().add_subplot(projection='3d')
pmax = 1.2
pmin = 0.0005
### Isothermal One
N = 100 #离散取样数目
t0 = 0.1
p = np.linspace(0.00025,200,N)
t = t0*np.ones(N)
v = t/p
for i in range(len(p)-1):
    if i == int((len(p)-1)/2):
        ax.plot(v[i:i+2], p[i:i+2], t[i:i+2],label='Isothermal Curve One',color=colormap(t[i]))
    else:
        ax.plot(v[i:i+2], p[i:i+2], t[i:i+2],color=colormap(t[i]),linewidth=3)


### Isothermal Two
N = 100 #离散取样数目
t0 = 30000
p = np.linspace(75,200,N)
t = t0*np.ones(N)
v = t/p
for i in range(len(p)-1):
    if i == int((len(p)-1)/2):
        ax.plot(v[i:i+2], p[i:i+2], t[i:i+2],label='Isothermal Curve Two',color=colormap(t[i]))
    else:
        ax.plot(v[i:i+2], p[i:i+2], t[i:i+2],color=colormap(t[i]),linewidth=3)




###Surface
# Make data.
#二元函数的形式
N = 100 #参数离散取值的个数
p = np.linspace(0, 200, N)
v = np.linspace(0, 400, N)
p, v = np.meshgrid(p, v)#p,v各自是一个二维数组（坐标网格）
t = p*v

# Plot the surface.
ax.plot_surface(v, p, t, edgecolor='royalblue', lw=0.1, rstride=10, cstride=10,alpha=0.05)


ax.set_ylabel('Pressure: '+r'$p=\frac{P}{P_0}$')
ax.set_xlabel('Volume: '+r'$v=\frac{V}{V_0}$')
ax.set_zlabel('Temperature: '+r'$t=\frac{T}{T_0}$')


#ax.set(ylim=(0.01, 0.4), xlim=(0.01, 40), zlim=(-0.1, 1))

ax.legend()
plt.show()