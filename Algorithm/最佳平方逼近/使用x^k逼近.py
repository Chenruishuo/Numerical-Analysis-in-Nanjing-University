import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quad
from scipy.linalg import hilbert
import time

def f(x, k):
    return x**k * np.exp(x)

def integral(k,f): 
    result, error = quad(f, 0, 1, args=(k,))
    return result

def approx(x, a):
    return sum(a[i] * x**i for i in range(len(a)))
start=time.time()
n=5
b=np.array([integral(i,f=f) for i in range(n+1)])
A=hilbert(n+1)
X=np.linalg.solve(A,b)
fig,ax1=plt.subplots()
x = np.linspace(0, 1, 1000)
y = np.e**x
y_approx = approx(x, X)
end=time.time()
print("run time:",end-start)
line1,=ax1.plot(x, y, label='e^x')
line2,=ax1.plot(x, y_approx, label='approximation')
ax2=ax1.twinx()
line3,=ax2.plot(x,y_approx-y,label='error',color='r')
lines = [line1, line2, line3]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels,loc='best')
plt.show()