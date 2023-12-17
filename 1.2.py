import random
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
l=1
mass=[]
for i in range(100):
    while True:
        ind = 1
        y = random.expovariate(l)
        ind=np.random.binomial(1,np.exp(l*l/2-l+l*y-y*y/2))
        if ind==1:
            mass.append(y)
            break
print(mass)
plt.subplot(1, 2, 1)
razb=[(3 * i /12) for i in range(12)]
plt.hist(np.array(mass), bins = razb)
plt.xticks([0,1,2,3])
mass1=[]
for i in range(100):
    r=random.randint(0,1)
    r=(r-0.5)*2
    mass1.append(mass[i]*r)
plt.subplot(1,2,2)
razb1=[(6 * (i /12-0.5)) for i in range(12)]
plt.hist(np.array(mass1), bins = razb1)
plt.xticks([-3,-2,-1, 0,1,2,3])
plt.show()

