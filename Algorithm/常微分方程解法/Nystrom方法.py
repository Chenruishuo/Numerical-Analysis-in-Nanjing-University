#Nystrom方法
import numpy as np
import matplotlib.pyplot as plt

# 定义微分方程
def f(x, y):
    return -1/(x**2) - y/x - y**2

# 定义 Nyström 方法
def nystrom(f, x0, y0, h, N):
    x = np.linspace(x0, x0 + N*h, N+1)
    y = np.zeros(N+1)
    y[0] = y0

    # 使用 Runge-Kutta 方法来生成初始的两个点
    for i in range(1):
        k1 = h*f(x[i], y[i])
        k2 = h*f(x[i] + h/2, y[i] + k1/2)
        k3 = h*f(x[i] + h/2, y[i] + k2/2)
        k4 = h*f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
    
    for i in range(1, N):
        y[i+1] = y[i-1] + 2*h*f(x[i], y[i])
    
    return x, y

x0, y0, h, N = 1, -1, 0.01, 100 # 设定初始条件和步长
x, y = nystrom(f, x0, y0, h, N)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Nyström')
plt.show()

