import numpy as np
import matplotlib.pyplot as plt

# 定义微分方程
def f(x, y):
    return -1/(x**2) - y/x - y**2

# 定义 hamming 方法
def hamming(f, x0, y0, h, N):
    x = np.linspace(x0, x0 + N*h, N+1)
    y = np.zeros(N+1)
    y[0] = y0

    # 使用 Runge-Kutta 方法来生成初始的四个点
    for i in range(3):
        k1 = h*f(x[i], y[i])
        k2 = h*f(x[i] + h/2, y[i] + k1/2)
        k3 = h*f(x[i] + h/2, y[i] + k2/2)
        k4 = h*f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
    
    for i in range(3, N):
        f_n = f(x[i], y[i])
        f_n_minus_1 = f(x[i-1], y[i-1])
        f_n_minus_2 = f(x[i-2], y[i-2])
        
        p_n_plus_1 = y[i-3] + 3/4*h*(2*f_n - f_n_minus_1 + 2*f_n_minus_2)
        c_n = y[i]
        
        q_n_plus_1 = p_n_plus_1 - 112/121*(y[i] - c_n)
        q_prime_n_plus_1 = f(x[i+1], q_n_plus_1)
        
        c_n_plus_1 = 1/8*(9*y[i] - y[i-2] + 3*h*(q_prime_n_plus_1 + 2*f_n - f_n_minus_1))
        
        y[i+1] = c_n_plus_1 + 9/121*(p_n_plus_1 - c_n_plus_1)
    
    return x, y

x0, y0, h, N = 1, -1, 0.01, 100 # 设定初始条件和步长
x, y = hamming(f, x0, y0, h, N)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Adjusted Hamming')
plt.show()
