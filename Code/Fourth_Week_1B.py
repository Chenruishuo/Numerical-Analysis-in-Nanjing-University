import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 1 / (1 + x ** 2)
n = 20
x_nodes = 5 * np.cos((2 * np.arange(n) + 1) * np.pi / 42)
def Lk(x, k, x_nodes):
    l = np.ones_like(x)
    for i in range(len(x_nodes)):
        if i == k:
            continue
        l *= (x - x_nodes[i]) / (x_nodes[k] - x_nodes[i])
    return l
def lagrange_interp(x, x_nodes, y_nodes):
    interp = 0
    for k in range(len(x_nodes)):
        interp += y_nodes[k] * Lk(x, k, x_nodes)
    return interp
x = np.linspace(-5, 5, 1000)
y_true = f(x)
y_interp = lagrange_interp(x, x_nodes, f(x_nodes))

plt.plot(x, y_true, label='True Function')
plt.plot(x, y_interp, label='Lagrange Interpolation')
plt.plot(x_nodes, f(x_nodes), 'ro', label='Interpolation Nodes')
plt.legend()
plt.show()