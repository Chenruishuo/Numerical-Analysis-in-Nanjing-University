import numpy as np
import matplotlib.pyplot as plt

R = lambda x: 1/(1+x**2)

x = np.linspace(-5, 5, 11)
y = R(x)

R_deriv = lambda x: -2*x/(1+x**2)**2
y_deriv = R_deriv(x)

h = np.diff(x)
a = y[:-1]
b = y_deriv[:-1]
c = (-3*h*y[:-1] - 2*h*y_deriv[:-1] + 3*h*y[1:] - h*y_deriv[1:])/(h**2)
d = (2*h*y[:-1] + h*y_deriv[:-1] - 2*h*y[1:] + h*y_deriv[1:])/(h**3)

x_eval = np.linspace(-5, 5, 501)
y_eval = np.zeros_like(x_eval)
for i in range(len(x)-1):
    idx = np.logical_and(x_eval >= x[i], x_eval <= x[i+1])
    h_i = x_eval[idx] - x[i]
    y_eval[idx] = a[i] + b[i]*h_i + c[i]*h_i**2 + d[i]*h_i**3

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_eval, R(x_eval), label='Original function')
ax.plot(x_eval, y_eval, label='Hermite Interpolation')
ax.scatter(x, y, c='r',label='Interpolation Nodes')
ax.legend(loc='upper left')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Hermite Interpolation')
plt.show()
