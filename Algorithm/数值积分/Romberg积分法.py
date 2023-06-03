import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 4 / (1 + x**2)

def romberg(f, a, b, h, max_iterations=20, epsilon=1e-7):
    R = [[0] * (max_iterations + 1) for _ in range(max_iterations + 1)]
    R[0][0] = 0.5 * (b - a) * (f(a) + f(b))
    for i in range(1, max_iterations + 1):
        h = (b - a) / (2 ** i)
        sum = 0.0
        for k in range(1, 2 ** (i - 1) + 1):
            x = a + (k - 0.5) * 2 * h
            sum += f(x)
        R[i][0] = 0.5 * R[i - 1][0] + h * sum
        for j in range(1, i + 1):
            R[i][j] = (4 ** j * R[i][j - 1] - R[i - 1][j - 1]) / (4 ** j - 1)
            if j==i and np.abs(R[i][j]-R[i][j-1])<epsilon:
                return R[i][j]
    return R[max_iterations][max_iterations]

a, b = 0, 1

romberg_errors = np.array([])

h_values = np.array([0.5**i for i in range(1, 23)])

for i in h_values:
    romberg_error = np.abs(romberg(f, a, b, i) - np.pi)
    romberg_errors = np.append(romberg_errors, romberg_error)

plt.plot(h_values, romberg_errors, label="Romberg")
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h')
plt.ylabel('Error')
plt.gca().invert_xaxis()
plt.legend()
plt.show()
