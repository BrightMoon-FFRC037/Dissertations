import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

colormap = mpl.colormaps['coolwarm']

ax = plt.figure().add_subplot(projection='3d')

f = 5 # degree of freedom
# Prepare arrays x, y, z
p = np.linspace(0,5,1000)
t = p**(2/(f+2))
v = p**(-(f/(f+2)))

for i in range(len(p)-1):
    if i == int((len(p)-1)/2):
        ax.plot(p[i:i+2], v[i:i+2], t[i:i+2],label='Adiabatic curve',color=colormap(t[i]))
    else:
        ax.plot(p[i:i+2], v[i:i+2], t[i:i+2],color=colormap(t[i]),linewidth=8)

ax.set_xlabel('Pressure: '+r'$p=\frac{P}{P_0}$')
ax.set_ylabel('Volume: '+r'$v=\frac{V}{V_0}$')
ax.set_zlabel('Temperature: '+r'$t=\frac{T}{T_0}$')


ax.legend()

plt.show()