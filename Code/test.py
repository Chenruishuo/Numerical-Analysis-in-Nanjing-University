import numpy as np
def composite_simpson(f0, a, b, h):
    n = int((b - a) / h)
    x = np.linspace(a, b, n+1)
    y = f0(x)
    s = (y[0] + y[n] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2])) * h / 3
    return s
def f1(x):
    return composite_simpson(lambda y: f(x, y), 0, 1, 0.01)
def f(x, y):
    return x*y
n=100
x = np.linspace(0, 1, 101)
print(x)
y = f1(x)
print(y)



