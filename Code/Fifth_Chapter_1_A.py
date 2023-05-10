import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 4 / (1 + x**2)


def composite_trapezoidal(f, a, b, h):
    n = int((b - a) / (2 * h)) * 2
    x = np.linspace(a, b, n+1)
    y = f(x)
    s = (y[0] + y[n] + 2 * np.sum(y[1:n])) * h / 2
    return s


def composite_simpson(f, a, b, h):
    n = int((b - a) / h)
    x = np.linspace(a, b, n+1)
    y = f(x)
    s = (y[0] + y[n] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2])) * h / 3
    return s


a, b = 0, 1

trap_errors = np.array([])
simp_errors = np.array([])

h_values = np.array([0.5**i for i in range(1, 23)])

for i in h_values:
    trap_error = np.abs(composite_trapezoidal(f, a, b, i) - np.pi)
    simp_error = np.abs(composite_simpson(f, a, b, i) - np.pi)
    trap_errors = np.append(trap_errors, trap_error)
    simp_errors = np.append(simp_errors, simp_error)

mask1 = np.where(h_values > 1e-6)
coefficients1 = np.polyfit(
    np.log10(h_values[mask1]), np.log10(trap_errors[mask1]), 1)
# 输出拟合的函数式
print(
    f"对于复合梯形公式拟合的函数式为 log10(y) = {coefficients1[0]}log10(x) + {coefficients1[1]}")

mask2 = np.where(h_values >= 10**(-2.1))
coefficients2 = np.polyfit(
    np.log10(h_values[mask2]), np.log10(simp_errors[mask2]), 1)
# 输出拟合的函数式
print(
    f"对于复合梯形公式拟合的函数式为 log10(y) = {coefficients2[0]}log10(x) + {coefficients2[1]}")

poly_fit1 = np.poly1d(coefficients1)
poly_fit2 = np.poly1d(coefficients2)
plt.plot(h_values[mask1], np.power(10, poly_fit1(
    np.log10(h_values[mask1]))), label='fit for Composite Trapezoidal')
plt.plot(h_values[mask2], np.power(10, poly_fit2(
    np.log10(h_values[mask2]))), label='fit for Simpson')
plt.plot(h_values, trap_errors, label="Composite Trapezoidal")
plt.plot(h_values, simp_errors, label="Composite Simpson")
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h')
plt.ylabel('Error')
plt.gca().invert_xaxis()
plt.legend()
plt.show()
