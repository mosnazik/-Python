import seaborn as sns
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
file = open('kick_data_nice.csv', 'r')
#Посмотреть про хи квадрат документацию
line = file.readline()
n=0
arr=[]
while line != '':
    if n==0:
        line = file.readline()
        n=n+1
        continue
    a=line.split(";")

    arr.append(a[6])
    n=n+1
    line = file.readline()
quanar=[]
fibarr=np.zeros(9)
n1=0
for i in range(len(arr)):
    ar1=str(arr[i])
    if int(ar1[0])==0:
        continue
    fibarr[int(ar1[0])-1]=fibarr[int(ar1[0])-1]+1
    n1=n1+1
print(np.sum(fibarr),n1)
file = open('population.txt', 'r')
quan=np.zeros(9)
for i in range(9):
    quan[i]=round(math.log(1+1/(i+1),10),4)
line = file.readline()
quan1=np.zeros(9)
n=0
while line != '':
    a=line.split()
    quan1[int(a[len(a)-1][0])-1]=quan1[int(a[len(a)-1][0])-1]+1
    n=n+1
    line = file.readline()
x=[1,2,3,4,5,6,7,8,9]
print(quan)
file.close()
quan2=np.zeros(9)
fib1 = 1
fib2 = 1
fib=[1]
i = 0
n2=700
while i < n2:
    strok=str(fib2)
    fib.append(int(strok[0]))
    quan2[int(strok[0])-1]=quan2[int(strok[0])-1]+1
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
#print(fib)
fib.sort()
summ=0
for i in range(9):
    summ=summ+((fibarr[i]-n1*quan[i])**2)/(n1*quan[i])
print(summ)
summ=0
for i in range(9):
    summ=summ+((quan1[i]-n*quan[i])**2)/(n*quan[i])
print(summ)
summ=0
for i in range(9):
    summ=summ+((quan2[i]-n2*quan[i])**2)/(n2*quan[i])
print(summ)
vals = stats.chi2.ppf([0.01, 0.05, 0.1], 8)
print(vals)
#сайт со стартапами колво слов в описании старпами
quantest=np.zeros(9)
for i in range(len(quan)):
    quantest[i]=int(round(quan[i]*n1))
print(np.sum(quantest),n1)
print(stats.chisquare(fibarr,f_exp=quantest))
for i in range(len(quan)):
    quantest[i]=int(round(quan[i]*n))
print(np.sum(quantest),n)
print(stats.chisquare(quan1,f_exp=quantest))
for i in range(len(quan)):
    quantest[i]=round(quan[i]*n2+0.05)
print(np.sum(quantest),n2)
print(stats.chisquare(quan2,f_exp=quantest))