import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

colormap = mpl.colormaps['coolwarm']

ax = plt.figure().add_subplot(projection='3d')
N = 100 #离散取样数目
t0 = 0.1
f = 5 # degree of freedom
# Prepare arrays x, y, z
p = np.linspace(0.001,0.1,N)
t = t0*np.ones(N)
v = t/p

for i in range(len(p)-1):
    if i == int((len(p)-1)/2):
        ax.plot(p[i:i+2], v[i:i+2], t[i:i+2],label='Isothermal curve',color=colormap(t[i]))
    else:
        ax.plot(p[i:i+2], v[i:i+2], t[i:i+2],color=colormap(t[i]),linewidth=3)

ax.set_xlabel('Pressure: '+r'$p=\frac{P}{P_0}$')
ax.set_ylabel('Volume: '+r'$v=\frac{V}{V_0}$')
ax.set_zlabel('Temperature: '+r'$t=\frac{T}{T_0}$')


ax.legend()
plt.show()