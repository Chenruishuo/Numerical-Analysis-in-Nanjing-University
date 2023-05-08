##Second_Week_2.py
import numpy as np
import math
import matplotlib.pyplot as plt
plt.rc('text',usetex=True)
y1=np.zeros(2**24+1)
n=2
for i in list(range(0,2**24))[::-1]:
    y1[i]=(math.e-y1[i+1])/(i+1)
if n>2**24:
    print("y_n=",0)
else:
    print("y_n={:.23f}".format(y1[n]))
y2=np.zeros(101)
y2[0]=math.e-1
for j in range(0,100):
    y2[j+1]=math.e-(j+1)*y2[j]
y2=[abs(k) for k in y2]
fig,ax=plt.subplots()
ax.set_xlabel(r'$n$',fontsize=13)
ax.set_ylabel(r'$\left|y_{n}\right|$',rotation=0,fontsize=13)
ax.plot(range(1,101),y1[1:101],label='Backward recursion',color='blue')
ax.plot(range(1,101),y2[1:101],label='Forward recursion',color='red')
ax.legend()
plt.yscale('log')
plt.show()
