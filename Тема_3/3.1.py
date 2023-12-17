import random
import seaborn as sns
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
data_table = pd.io.parsers.read_table("amazon-books.txt")
print(data_table[["Amazon Price"]])
a=data_table['Amazon Price'].tolist()
print(data_table[["NumPages"]])
b=data_table['NumPages'].tolist()
k=[]
for i in range(325):
    if math.isnan(b[i]):
        k.append(i)
for i in range(len(k)):
    a.pop(k[i]-i)
    b.pop(k[i]-i)

sum=np.mean(a)
sum1=np.mean(b)
sr=np.std(a)*np.std(a)*len(a)
sr1=np.std(b)*np.std(b)*len(b)
kor=np.cov([a,b])[0][1]*(len(a)-1)
koeff=kor/(np.sqrt(sr*sr1))
kor=kor/323
okor=[]
okor1=[]
mean=[sum,sum1]
cov=[[sr/323,kor],[kor,sr1/323]]
for i in range(200):
    x=[]
    y=[]
    for j in range(323):
        #x.append(random.normalvariate(sum, np.sqrt(sr/322)))
        #y.append(random.normalvariate(sum1, np.sqrt(sr1/322)))
        x1 = np.random.multivariate_normal(mean, cov)
        x.append(x1[0])
        y.append(x1[1])
    sum2 = np.mean(x)
    sum3 = np.mean(y)
    sr2=np.std(x)*np.std(x)*len(x)
    sr3=np.std(y)*np.std(y)*len(y)
    sum4=np.cov([x,y])[0][1]*(len(x)-1)
    okor.append(sum4/(np.sqrt(sr2)*np.sqrt(sr3)))
    okor1.append(sum4 /(np.sqrt(sr2)*np.sqrt(sr3))-koeff)
okor.sort()
okor1.sort()
print(okor[4])
print(okor[194])
print(koeff-okor1[194])
print(koeff-okor1[4])