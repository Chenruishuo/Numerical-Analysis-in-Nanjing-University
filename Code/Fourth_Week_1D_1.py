import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def f(x):
    return 1 / (1 + x**2)

x = np.linspace(-5, 5, 11)
y = f(x)
cs = CubicSpline(x, y)

x_vals = np.linspace(-5, 5, 100)
plt.plot(x_vals, f(x_vals), label='Original function')
plt.plot(x_vals, cs(x_vals), label='Cubic spline') 
plt.scatter(x, y, c='r', label='Interpolation Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic spline interpolation')
plt.legend()
plt.show()
