import numpy as np
import matplotlib.pyplot as plt

# 设置初始条件和步长
y0 = -1
a = 1
b = 2
h=0.1

def func(x, y):
    return -1 / x**2 - y / x - y**2

#Runge-Kutta-Fehlberg方法
def RKF(h, x, y, f,h_max,h_min,tol):
    k1 = h * f(x, y)
    k2 = h * f(x + h / 4, y + k1 / 4)
    k3 = h * f(x + 3 * h / 8, y + 3 * k1 / 32 + 9 * k2 / 32)
    k4 = h * f(x + 12 * h / 13, y + 1932 * k1 / 2197 - 7200 * k2 / 2197 + 7296 * k3 / 2197)
    k5 = h * f(x + h, y + 439 * k1 / 216 - 8 * k2 + 3680 * k3 / 513 - 845 * k4 / 4104)
    k6 = h * f(x + h / 2, y - 8 * k1 / 27 + 2 * k2 - 3544 * k3 / 2565 + 1859 * k4 / 4104 - 11 * k5 / 40)
    y_next = y + 25 * k1 / 216 + 1408 * k3 / 2565 + 2197 * k4 / 4104 - k5 / 5
    y_star = y + 16 * k1 / 135 + 6656 * k3 / 12825 + 28561 * k4 / 56430 - 9 * k5 / 50 + 2 * k6 / 55
    R = np.abs(y_next - y_star) / h
    delta = 0.84 * (tol / R)**0.25
    x_next = x + h
    if R > tol:
        if delta<=0.1:
            h = 0.1 * h
        elif delta>=4:
            h = 4 * h
        else:
            h = delta * h
        if h>=h_max:
            h=h_max
        elif h<h_min:
            print('Minimum h exceeded')
    return y_next, x_next, h

        

# 初始化解决方案数组并添加初始条件
X = [a]
Y = [y0]

# 使用Runge-Kutta-Fehlberg方法解决ODE
while X[-1] < b:
    y_next, x_next, h = RKF(h ,X[-1], Y[-1], func,h_max=0.1,h_min=0.001,tol=1e-4)
    X.append(x_next)
    Y.append(y_next)

# 绘图
plt.plot(X, Y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Runge-Kutta-Fehlberg')
plt.show()

