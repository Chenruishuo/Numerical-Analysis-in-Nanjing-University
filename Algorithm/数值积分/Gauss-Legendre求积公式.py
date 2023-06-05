import numpy as np
# Gauss-Legendre求积公式
def Gauss_Legendre(f, a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    G = 0.5 * (b - a) * np.sum(w * f(0.5 * (b - a) * x + 0.5 * (b + a)))
    return G
# 测试
def f(x):
    return x**2
print(Gauss_Legendre(f, 0, 1, 100))



