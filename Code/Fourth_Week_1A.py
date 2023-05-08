import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + x ** 2)

x = np.linspace(-5, 5, 11)
y = f(x)
n = len(x)
c = y.copy()
for j in range(1, n):
    c[j:n] = (c[j:n] - c[j - 1]) / (x[j:n] - x[j - 1])

def poly(xval):
    p = c[-1] * np.ones_like(xval)
    for j in range(n - 2, -1, -1):
        p = (xval - x[j]) * p + c[j]
    return p

xval = np.linspace(-5, 5, 1000)
plt.plot(xval, f(xval), label='True function')
plt.plot(xval, poly(xval), label='10th-order Newton polynomial')
plt.scatter(x, y, color="red", label='Interpolation Nodes')
plt.legend()
plt.show()