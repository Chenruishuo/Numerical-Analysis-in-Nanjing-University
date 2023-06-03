import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

def f(x):
    return 1 / (1 + x**2)

x = np.linspace(-5, 5, 11)
y = f(x)
interp_func = PchipInterpolator(x, y)
xx = np.linspace(-5, 5, 1000)
yy = f(xx)

plt.plot(xx, yy, label='Original Function') 
plt.plot(xx, interp_func(xx), label='Hermite Interpolation')
plt.scatter(x, y, c='r', label='Interpolation Points')
plt.legend()
plt.show()
