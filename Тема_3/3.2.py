import random
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import binom
from scipy import optimize
import matplotlib.pyplot as plt
data_table = pd.io.parsers.read_table("babysamp-98.txt")
print(data_table[["sex"]])
a=data_table['sex'].tolist()
b=[]
k=0
for i in range(200):
    if a[i]=='F':
        b.append(0)
    else:
        b.append(1)
        k=k+1
print(k)
otr11=k/200-1.96*np.sqrt((k/200)*(1-k/200)/200)
otr12=k/200+1.96*np.sqrt((k/200)*(1-k/200)/200)
print(otr11)
print(otr12)
print(0.44)
print(0.585)
def f(x):
    return (binom.cdf(k= 103 , n= 200 , p= x )-0.025)
def f1(x):
    return (binom.cdf(k= 102 , n= 200 , p= x )-0.975)
sol = optimize.root_scalar(f, bracket=[0, 1], method='brentq')
print('Solution:\n', sol.root)
sol1 = optimize.root_scalar(f1, bracket=[0, 1], method='brentq')
print('Solution:\n', sol1.root)
