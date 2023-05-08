import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 4 / (1 + x**2)

def composite_trapezoidal(a, b, h):
    n = int((b - a) / h)
    x = np.linspace(a, b, n+1)
    y = f(x)
    s = (y[0] + y[n] + 2 * np.sum(y[1:n])) * h / 2
    return s

def composite_simpson(a, b, h):
    n = int((b - a) / h)
    x = np.linspace(a, b, n+1)
    y = f(x)
    s = (y[0] + y[n] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2])) * h / 3
    return s

a, b = 0, 1

trap_errors = []
simp_errors = []

h_values = [0.5**i for i in range(1,24)]

for i in h_values:
    trap_error = abs(composite_trapezoidal(a, b, i) - np.pi)
    simp_error = abs(composite_simpson(a, b, i) - np.pi)
    trap_errors.append(trap_error)
    simp_errors.append(simp_error)

plt.plot(h_values, trap_errors, label="Composite Trapezoidal")
plt.plot(h_values, simp_errors, label="Composite Simpson")
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h')
plt.ylabel('Error')
plt.gca().invert_xaxis()
plt.legend()
plt.show()
