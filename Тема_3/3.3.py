import random
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data_table = pd.io.parsers.read_table("nissan.txt")
print(data_table[["mpg"]])
a=data_table['mpg'].tolist()
sum=0
sum1=0
for i in range(100):
    sum=sum+a[i]
sum=sum/100
print(sum)
for i in range(100):
    sum1=sum1+(a[i]-sum)*(a[i]-sum)
sum1=sum1/99
sum3=0
for i in range(50):
    sum2=0
    for j in range(100):
        sum2=sum2+random.normalvariate(sum, np.sqrt(sum1))
    sum3=sum3+(sum2/100-sum)*(sum2/100-sum)
sum3=sum3/50
otr11=sum-1.66*np.sqrt(sum1/100)
otr12=sum+1.66*np.sqrt(sum1/100)
otr21=sum-1.96*np.sqrt(sum1/100)
otr22=sum+1.96*np.sqrt(sum1/100)
otr31=sum-1.96*np.sqrt(sum3)
otr32=sum+1.96*np.sqrt(sum3)
print(otr11)
print(otr12)
print(otr21)
print(otr22)
print(otr31)
print(otr32)