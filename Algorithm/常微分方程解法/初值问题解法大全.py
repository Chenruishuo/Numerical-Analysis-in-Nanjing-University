import numpy as np
from matplotlib import pyplot as plt

def y(x):
    return 1/(x*np.tan(np.log(x)-np.pi/4))


h = 0.0001
x = np.arange(1, 2+h, h)
y0 = -1


def f(x, y):
    return -1/x**2 - y/x - y**2


def euler(x, y0, f):
    y = np.zeros(x.shape)
    y[0] = y0
    for i in range(len(x) - 1):
        y[i+1] = y[i] + h * f(x[i], y[i])
    return y


def improved_euler(x, y0, f):
    y = np.zeros(x.shape)
    y[0] = y0
    for i in range(len(x) - 1):
        k1 = f(x[i], y[i])
        k2 = f(x[i+1], y[i] + h * k1)
        y[i+1] = y[i] + h * (k1 + k2) / 2
    return y


def heun(x, y0, f):
    y = np.zeros(x.shape)
    y[0] = y0
    for i in range(len(x) - 1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + 2*h/3, y[i] + 2*h/3 * k1)
        y[i+1] = y[i] + h * (k1 + 3*k2) / 4
    return y


def midpoint(x, y0, f):
    y = np.zeros(x.shape)
    y[0] = y0
    for i in range(len(x) - 1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h/2, y[i] + h/2 * k1)
        y[i+1] = y[i] + h * k2
    return y


def runge_kutta(x, y0, f):
    y = np.zeros(x.shape)
    y[0] = y0
    for i in range(len(x) - 1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h/2, y[i] + h/2 * k1)
        k3 = f(x[i] + h/2, y[i] + h/2 * k2)
        k4 = f(x[i] + h, y[i] + h * k3)
        y[i+1] = y[i] + h * (k1 + 2*k2 + 2*k3 + k4) / 6
    return y

def adams(x, y0, dydx, runge_kutta):
    y = np.zeros(x.shape)
    y[:4] = runge_kutta(x[:4], y0, dydx)
    for i in range(3, len(x) - 1):
        y_pred = y[i] + h/24 * (55*dydx(x[i], y[i]) - 59*dydx(x[i-1], y[i-1]) + 37*dydx(x[i-2], y[i-2]) - 9*dydx(x[i-3], y[i-3]))
        y[i+1] = y[i] + h/24 * (9*dydx(x[i+1], y_pred) + 19*dydx(x[i], y[i]) - 5*dydx(x[i-1], y[i-1]) + dydx(x[i-2], y[i-2]))
    return y

y_precise=y(x)
error_euler = np.abs(y_precise-euler(x, y0, f))
error_improved_euler = np.abs(y_precise-improved_euler(x, y0, f))
error_heun = np.abs(y_precise-heun(x,y0, f))
error_midpoint = np.abs(y_precise-midpoint(x, y0, f))
error_runge_kutta = np.abs(y_precise-runge_kutta(x, y0, f))
error_adams = np.abs(y_precise-adams(x, y0, f, runge_kutta))

plt.figure(figsize=(12, 8))
plt.plot(x, error_euler, label='Euler')
plt.plot(x, error_improved_euler, label='Improved Euler')
plt.plot(x, error_heun, label='Heun')
plt.plot(x, error_midpoint, label='Midpoint')
plt.plot(x, error_runge_kutta, label='Runge-Kutta')
plt.plot(x, error_adams, label='Adams')
print(error_euler[-1],error_improved_euler[-1],error_heun[-1],
      error_midpoint[-1],error_runge_kutta[-1],error_adams[-1])
plt.legend(loc='best')
plt.ylabel('Error')
plt.grid(True)
plt.show()