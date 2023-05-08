import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quad
from scipy.special import legendre
import time

def f(x, k):
    return legendre(k)(2*x-1) * np.exp(x)

def integral(k, func):
    result, error = quad(func, 0, 1, args=(k,))
    return result

def approx(x, a):
    return sum(a[i] * legendre(i)(2*x-1) for i in range(len(a)))

start=time.time()
n = 10
coefficient = np.array([(2*i+1)*integral(i, f) for i in range(n+1)])

fig, ax1 = plt.subplots()
x = np.linspace(0, 1, 1000)
y = np.e**x
y_approx = approx(x, coefficient)
end=time.time()
print("run time:",end-start)
line1, = ax1.plot(x, y, label='e^x')
line2, = ax1.plot(x, y_approx, label='approximation')
ax2 = ax1.twinx()
line3, = ax2.plot(x, y_approx-y, label='error', color='r')
lines = [line1, line2, line3]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='best')
plt.show()
