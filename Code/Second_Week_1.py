##Second_Week_1.py
import math
import matplotlib.pyplot as plt
plt.rc('text',usetex=True)
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] 
def calc_y(x):
    if abs(x)>=2:
        y=x-math.sin(x)
        return y
    else:
        rad = x
        return rad**3/6 - rad**5/120 + rad**7/5040 - rad**9/362880 + rad**11/39916800 -rad**13/6227020800
def precise(x):
    return x-math.sin(x)
a = [10**i for i in range(-10,1)][::-1]
b = [calc_y(n) for n in a]
c = [precise(n) for n in a]
plt.plot(a,b,label='Taylor',color='green')
plt.plot(a,c,label='Direct',color='blue')
plt.xlabel('$x$',fontsize=13)
plt.ylabel('$x-\sin{x}$',fontsize=13)
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

