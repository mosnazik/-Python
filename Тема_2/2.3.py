from scipy.optimize import minimize
import scipy.special as sc
import random
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def f(x,vib):
    sum=0
    for i in range(len(vib)):
        sum=sum+(x[0]-1)*np.log(vib[i])+(x[1]-1)*np.log(1-vib[i])-np.log(sc.beta(x[0],x[1]))
    return sum
a=1
b=1
och1=[]
och2=[]
for j in range(100):
    vib=[]
    r = 100
    for i in range(100):
       x = random.betavariate(a,b)
       vib.append(x)
    def f1(x):
       return (-f(x,vib))
    sum=np.sum(vib)/r
    sum1=0
    for i in range(r):
        sum1=sum1+(vib[i]-sum)*(vib[i]-sum)
    sum1=sum1/(r-1)
    res = minimize(f1, [sum*(sum*(1-sum)/sum1-1),(1-sum)*(sum*(1-sum)/sum1-1)],method='nelder-mead')
    #och1.append(res.x[0])
    #och2.append(res.x[1])
    och1.append(np.sqrt(r)*(res.x[0]-a))
    och2.append(np.sqrt(r)*(res.x[1]-b))
print(och1)
print(och2)
sns.displot (och1)
sns.displot (och2)
plt.show()



n=30
pPerc, pPiv = np.zeros(n), np.zeros(n)
#истинное значение параметра theta
th=5
och1=[]
och2=[]
g=[]
a=5
sum1=0
sum2=0
for j in range(n):
    #моделируем нормальную выборку и оцениваем ее средним
    x=rand.normal(size=30)+th
    th1=np.mean(x)
    thX=np.zeros(20)
    for i in range(20):
        thX[i]=np.mean(rand.normal(size=30)+th1)
    sum1=sum1+(th1-th)*(th1-th)
    sum2=sum2+(2*th1-np.mean(thX)-th)*(2*th1-np.mean(thX)-th)
    och1.append(np.sqrt(n) * (th1-th))
    och2.append(np.sqrt(n) * (2*th1-np.mean(thX)-th))
    g.append(['1',np.sqrt(n) * (th1-th)])
    g.append(['2', np.sqrt(n) * (2*th1-np.mean(thX)-th)])
print(sum1/(n-1))
print(sum2/(n-1))
df = pd.DataFrame(g, columns=['name', 'dist'])
print(df)
#sns.displot(och1)
#sns.displot(och2)
sns.displot(data=df,x='dist', hue='name', kind='kde')
#sns.displot(och2, kind='kde')
plt.show()
