import numpy as np
import matplotlib.pyplot as plt

def natural_cubic_spline(x, y):
    n = len(x)
    a = y.copy()
    b = np.zeros(n)
    d = np.zeros(n)
    h = np.diff(x)
    alpha = np.zeros(n-1)
    for i in range(1, n-1):
        alpha[i] = 3/h[i]*(a[i+1]-a[i])-3/h[i-1]*(a[i]-a[i-1])
    c = np.zeros(n)
    l = np.zeros(n)
    mu = np.zeros(n)
    z = np.zeros(n)
    l[0] = 1
    mu[0] = 0
    z[0] = 0
    for i in range(1, n-1):
        l[i] = 2*(x[i+1]-x[i-1])-h[i-1]*mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i]-h[i-1]*z[i-1])/l[i]
    l[n-1] = 1
    z[n-1] = 0
    for j in range(n-2, -1, -1):
        c[j] = z[j]-mu[j]*c[j+1]
        b[j] = (a[j+1]-a[j])/h[j]-h[j]*(c[j+1]+2*c[j])/3
        d[j] = (c[j+1]-c[j])/(3*h[j])
    return a, b, c, d

def eval_cubic_spline(x_eval, x, a, b, c, d):
    idx = np.digitize(x_eval, x) - 1
    idx = np.clip(idx, 0, len(x)-2)
    h = x_eval - x[idx]
    y_eval = a[idx] + b[idx]*h + c[idx]*h**2 + d[idx]*h**3
    return y_eval

R = lambda x: 1/(1+x**2)

x = np.linspace(-5, 5, 11)
y = R(x)

a, b, c, d = natural_cubic_spline(x, y)

x_eval = np.linspace(-5, 5, 501)
y_eval = eval_cubic_spline(x_eval, x, a, b, c, d)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_eval, R(x_eval), label='Original function')
ax.plot(x_eval, y_eval, label='Cubic Spline')
ax.scatter(x, y, c='r', label='Interpolation Nodes')
ax.legend(loc='upper left')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Cubic Spline Interpolation')
plt.show()
