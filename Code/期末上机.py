import numpy as np
from matplotlib import pyplot as plt

def y(x):
    return x**2-x**3+1/2*x**4+x**2*np.log(x)

def f(x, y):
    return (-3/x)*y+6*x-6*x**2+7/2*x**3+5*x*np.log(x)


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

h_list = [1/200,1/100,1/50,1/25,1/10,1/5,1/4]
error_x_eq_2=np.zeros(len(h_list))
y0 = 1/2
for i in range(len(h_list)):
    h=h_list[i]
    n=int(1/h)
    x = np.linspace(1, 2, n+1)
    y_cal=runge_kutta(x, y0, f)
    error_x_eq_2[i]=np.abs(y_cal[-1]-y(2))
print(error_x_eq_2)

h_list_log=np.log(h_list)
error_x_eq_2_log=np.log(error_x_eq_2)

coefficients = np.polyfit(
    h_list_log, error_x_eq_2_log, 1)
print(
    f"对于拟合的函数式为 ln(error) = {coefficients[0]}ln(h) + {coefficients[1]}")
error_log_fit=coefficients[0]*h_list_log+coefficients[1]

plt.figure(figsize=(12, 8))
plt.plot(h_list_log, error_x_eq_2_log, label='Runge-Kutta error')
plt.plot(h_list_log, error_log_fit, label='fit for Runge-Kutta error')
plt.legend(loc='best')
plt.xlabel('ln h')
plt.ylabel('ln Error')
plt.xlim((np.log(1/200),np.log(1/4)))
plt.grid(True)
plt.show()