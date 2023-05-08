##Second_Week_3A.py
import matplotlib.pyplot as plt
import numpy as np
x=np.zeros(200,dtype=float)
x[0]=1
x[1]=1/3
ep=np.zeros(200,dtype=float)
for i in range(2,200):
    x[i]=x[i-1]*13/3-x[i-2]*4/3
    ep[i]=np.abs(1/np.power(3,i)-x[i])
plt.plot(np.arange(2,200), ep[2:200])
plt.xlabel('n')
plt.ylabel('error')
plt.yscale('log')
plt.title('Error plot')
plt.show()