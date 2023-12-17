import seaborn as sns
import pandas as pd
import numpy as np
import random
import math
import openturns as ot
import scikit_posthocs as sp
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
data_table = pd.io.parsers.read_table("cholestg.txt")
print(data_table)
arr=data_table["cholest"].to_numpy()
group=data_table["group"].to_numpy()
day=data_table["day"].to_numpy()
pat=data_table["patient"].to_numpy()
k=[]
sam1=[]
sam2=[]
sam3=[]
for i in range(len(arr)):
    if math.isnan(arr[i]):
        k.append(pat[i])
for i in range(len(arr)):
    if math.isnan(arr[i]) or group[i]==2:
        continue
    if int(day[i])==2:
        if int(pat[i]) in k:
            continue
        sam1.append(int(arr[i]))
    elif int(day[i])==4:
        if int(pat[i]) in k:
            continue
        sam2.append(int(arr[i]))
    elif int(day[i])==14:
        sam3.append(int(arr[i]))
sam11=[]
sam12=[]
sam13=[]
for i in range(len(arr)):
    if math.isnan(arr[i]):
        continue
    if group[i]==2:
        sam13.append(int(arr[i]))
        continue
    if int(day[i])==2:
        sam11.append(int(arr[i]))
    if int(day[i])==14:
        sam12.append(int(arr[i]))
print(stats.friedmanchisquare(sam1,sam2,sam3))
print(stats.mannwhitneyu(sam11,sam13))
print(stats.mannwhitneyu(sam12,sam13))
sns.boxplot(data=[sam11,sam13])
plt.show()