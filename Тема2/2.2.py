#Дано равномерное распределение на отрезке [-a,a], построить оценки ОМП и методом спейсингов, сравнить асимп. нормальн.
import random
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def t_omp(x):
    return max(max(x),-min(x))
def t_sps(x):
    if len(x)>1:
        return ((len(x)*(max(x)-min(x))+np.sqrt((max(x)+min(x))*(max(x)+min(x))*len(x)*len(x)-4*max(x)*min(x)))/(2*len(x)-2))
    else:
        return max(x)
a=1
och1=[]
och2=[]
for j in range(300):
    vib=[]
    r = random.randint(1, 100)
    for i in range(r):
       x = 2*a*(random.random()-0.5)
       vib.append(x)
    och1.append(np.sqrt(r)*(t_omp(vib)-a))
    och2.append(np.sqrt(r)*(t_sps(vib)-a))
print(och1)
print(och2)
plt.subplot(1, 2, 1)
razb=[(2*a* (i /12-0.5)) for i in range(12)]
plt.hist(np.array(och1), bins = razb)
plt.subplot(1,2,2)
plt.hist(np.array(och2), bins = razb)
plt.xticks([-a,-a/2, 0,a/2,a])
plt.show()





