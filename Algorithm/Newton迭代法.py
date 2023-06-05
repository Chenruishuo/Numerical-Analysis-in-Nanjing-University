#Newton 迭代法
def f(x):
    return x**3 + 2*x - 1
def df(x):
    return 3*x**2 + 2
def newton(f, df, x0, tol=1e-6, maxiter=100):
    for i in range(maxiter):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return x1
print(newton(f, df, 1))