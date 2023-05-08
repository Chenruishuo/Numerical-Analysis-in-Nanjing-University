import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(1+x**2)

x = np.linspace(-5, 5, 11)
y = f(x)
from scipy import interpolate
lin_interp = interpolate.interp1d(x, y)
xx = np.linspace(-5, 5, 101)
yy = lin_interp(xx)

plt.plot(xx, f(xx), label='Function')
plt.plot(xx, yy, label='Linear Interpolation')
plt.scatter(x, y, color="red", label='Interpolation Nodes')
plt.legend()
plt.show()