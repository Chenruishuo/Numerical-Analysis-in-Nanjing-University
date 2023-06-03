import numpy as np
import matplotlib.pyplot as plt
import time

def f(t):
        return t**3 / (1 - t)**5 * 1/(np.exp(t / (1 - t))-1) if t!=0 and t!=1 else 0


def composite_trapezoidal(f, a, b, h):
    n = int((b - a) / (2 * h)) * 2
    x = np.linspace(a, b, n+1)
    y = list(map(f, x))
    s = (y[0] + y[n] + 2 * np.sum(y[1:n])) * h / 2
    return s


def composite_simp_errorson(f, a, b, h):
    n = int((b - a) / h)
    x = np.linspace(a, b, n+1)
    y = list(map(f,x))
    s = (y[0] + y[n] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2])) * h / 3
    return s


def romberg_integration(f, a, b, h, max_iterations=14, epsilon=1e-13):
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
    return R[max_iterations][max_iterations]


def adaptive_integration(f, a, b, h, epsilon=1e-6, max_depth=50):
    x0 = a
    x2 = b
    x1 = (a + b) / 2.0
    S0 = composite_simp_errorson(f, a, b, (b-a)/2)
    S1 = composite_simp_errorson(f, x0, x1, (x1-x0)/2)
    S2 = composite_simp_errorson(f, x1, x2, (x2-x1)/2)
    error = abs(S0 - S1 - S2)
    if error < epsilon or max_depth == 0:
        return S1 + S2
    else:
        left_integral = adaptive_integration(
            f, x0, x1, epsilon / 2, h / 2, max_depth - 1)
        right_integral = adaptive_integration(
            f, x1, x2, epsilon / 2, h / 2, max_depth - 1)
        return left_integral + right_integral


def composite_gauss_twopoint(f, a, b, h):
    x = np.array([-np.sqrt(1/3), np.sqrt(1/3)])
    w = np.array([1, 1])
    n = (b - a) / h
    intervals = np.linspace(a, b, n+1)
    integral = 0
    for i in range(n):
        x_new = (x + 1) * intervals[i] / 2 + (1 - x) * intervals[i+1] / 2
        integral += h/2 * np.sum(w * f(x_new))
    return integral

a, b = 0, 1
h_values = np.array([0.5**i for i in range(1, 15)])

trap_errors = np.array([])
trap_times=np.array([])
for i in h_values:
    _st = time.time()
    trap = np.abs(composite_trapezoidal(f, a, b, i))
    _ed=time.time()
    trap_errors = np.append(trap_errors, np.abs(trap-np.power(np.pi,4)/15))
    trap_times=np.append(trap_times,_ed-_st)
print(f"复合梯形公式最小误差：{np.min(trap_errors)}，最大误差：{np.max(trap_errors)}，最多用时（ms）：{1000*max(trap_times)}")

simp_errors = np.array([])
simp_times=np.array([])
for i in h_values:
    _st = time.time()
    simp = np.abs(composite_simp_errorson(f, a, b, i))
    _ed = time.time()
    simp_errors = np.append(simp_errors, np.abs(simp-np.power(np.pi,4)/15))
    simp_times=np.append(simp_times,_ed-_st)
print(f"复合Simpson公式最小误差：{np.min(simp_errors)}，最大误差：{np.max(simp_errors)}，最多用时（ms）：{1000*max(simp_times)}")

romberg_errors = np.array([])
romberg_times=np.array([])
for i in h_values:
    _st = time.time()
    romberg = np.abs(romberg_integration(f, a, b, i))
    _ed = time.time()
    romberg_errors = np.append(romberg_errors, np.abs(romberg-np.power(np.pi,4)/15))
    romberg_times=np.append(romberg_times,_ed-_st)
print(f"Romberg最小误差：{np.min(romberg_errors)}，最大误差：{np.max(romberg_errors)}，最多用时（ms）：{1000*max(romberg_times)}")

adaptive_errors = np.array([])
adaptive_times=np.array([])
for i in h_values:
    _st = time.time()
    adaptive = np.abs(adaptive_integration(f, a, b, i))
    _ed = time.time()
    adaptive_errors = np.append(adaptive_errors, np.abs(adaptive-np.power(np.pi,4)/15))
    adaptive_times=np.append(adaptive_times,_ed-_st)
print(f"自适应最小误差：{np.min(adaptive_errors)}，最大误差：{np.max(adaptive_errors)}，最多用时（ms）：{1000*max(adaptive_times)}")

gauss_errors=np.array([])
gauss_times=np.array([])
for i in h_values:
    _st = time.time()
    gauss = np.abs(adaptive_integration(f, a, b, i))
    _ed = time.time()
    gauss_errors = np.append(gauss_errors, np.abs(gauss-np.power(np.pi,4)/15))
    gauss_times=np.append(gauss_times,_ed-_st)
print(f"复合Gauss两点最小误差：{np.min(gauss_errors)}，最大误差：{np.max(gauss_errors)}，最多用时（ms）：{1000*max(gauss_times)}")

plt.plot(h_values, trap_errors, label="Composite Trapezoidal")
plt.plot(h_values, simp_errors, label="Composite Simpson")
plt.plot(h_values, romberg_errors, label="Romberg")
plt.plot(h_values, adaptive_errors, label="Adaptive")
plt.plot(h_values, gauss_errors, label="Gauss")
plt.xscale('log')
plt.xlabel('h')
plt.ylabel('Error')
plt.gca().invert_xaxis()
plt.legend()
plt.show()

plt.plot(h_values, trap_times*1000, label="Composite Trapezoidal")
plt.plot(h_values, simp_times*1000, label="Composite Simpson")
plt.plot(h_values, romberg_times*1000, label="Romberg")
plt.plot(h_values, adaptive_times*1000, label="Adaptive")
plt.plot(h_values, gauss_times, label="Gauss")
plt.xscale('log')
plt.xlabel('h')
plt.ylabel('Run time(ms)')
plt.gca().invert_xaxis()
plt.legend()
plt.show()