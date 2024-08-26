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
p = np.linspace(0.0005,pmax,N)
t = t0*np.ones(N)
v = t/p
for i in range(len(p)-1):
    if i == int((len(p)-1)/2):
        ax.plot(v[i:i+2], p[i:i+2], t[i:i+2],label='Isothermal Curve One',color=colormap(t[i]))
    else:
        ax.plot(v[i:i+2], p[i:i+2], t[i:i+2],color=colormap(t[i]),linewidth=3)


### Isothermal Two
N = 100 #离散取样数目
t0 = 1
p = np.linspace(0.005,pmax,N)
t = t0*np.ones(N)
v = t/p
for i in range(len(p)-1):
    if i == int((len(p)-1)/2):
        ax.plot(v[i:i+2], p[i:i+2], t[i:i+2],label='Isothermal Curve Two',color=colormap(t[i]))
    else:
        ax.plot(v[i:i+2], p[i:i+2], t[i:i+2],color=colormap(t[i]),linewidth=3)




###Adiabatic Curve
f = 5 # degree of freedom
# Prepare arrays x, y, z
p = np.linspace(pmin,pmax,100)
t = p**(2/(f+2))
v = p**(-(f/(f+2)))

for i in range(len(p)-1):
    if i == int((len(p)-1)/2):
        ax.plot(v[i:i+2], p[i:i+2], t[i:i+2],label='Adiabatic curve',color=colormap(t[i]))
    else:
        ax.plot(v[i:i+2], p[i:i+2], t[i:i+2],color=colormap(t[i]),linewidth=3)



ax.set_ylabel('Pressure: '+r'$p=\frac{P}{P_0}$')
ax.set_xlabel('Volume: '+r'$v=\frac{V}{V_0}$')
ax.set_zlabel('Temperature: '+r'$t=\frac{T}{T_0}$')


#ax.set(ylim=(0.01, 0.4), xlim=(0.01, 40), zlim=(-0.1, 1))

ax.legend()
plt.show()