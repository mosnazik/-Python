import random
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
n=1000
pi=3.141592
sum=0
for i in range(n):
    x=random.random()
    sum=sum+np.abs(np.cos(x*2*pi))
sum=sum/n
print(sum)
fi=random.random()*2*pi
x=np.cos(fi)
y=np.sin(fi)
c=plt.Circle((0, 0), radius=1, fill=False)
plt.gca ().add_artist (c)
plt.scatter(x,y)
plt.axis([-2,2,-2,2])
plt.show()
