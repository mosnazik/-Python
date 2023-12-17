import seaborn as sns
import pandas as pd
import numpy as np
import random
import math
import openturns as ot
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
import scikit_posthocs as sp
auto=pd.read_csv("Automobile_data.csv")
loc=auto["fuel-type"].to_numpy()
mpg=auto["city-mpg"].to_numpy()
price=auto["price"].to_numpy()
sam1=[]
sam2=[]
for i in range(len(mpg)):
    if loc[i]=='gas':
        sam1.append(mpg[i])
    if loc[i]=='diesel':
        sam2.append(mpg[i])
print(stats.mannwhitneyu(sam1,sam2))
print(stats.anderson_ksamp([sam1,sam2]))
sam3=[]
sam4=[]
for i in range(len(price)):
    if price[i]=='?':
        continue
    if loc[i]=='gas':
        sam3.append(int(price[i]))
    if loc[i]=='diesel':
        sam4.append(int(price[i]))
print(stats.mannwhitneyu(sam3,sam4))
print(stats.anderson_ksamp([sam3,sam4]))