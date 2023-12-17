import seaborn as sns
import pandas as pd
import numpy as np
import math
import openturns as ot
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
def statistic_AD(X: np.array, F, n: int, transpos=False) -> np.array:
  arr = np.array(list([(2 * i - 1) / n for i in range(1, n + 1)]))
  S = (np.log(F(np.sort(X))) +
        np.log(1 - F(-np.sort(-X))))
  T = -S.dot(arr) - n
  return T
data_table = pd.io.parsers.read_table("Rainfall.txt")
arr=data_table["Rainfall"].to_numpy()
arr1=[]
for i in range(len(arr)):
  arr1.append(np.log(arr[i]))
s=np.sqrt(np.log(1 + (np.std(arr) / np.mean(arr)) ** 2))
lambda_value = np.log(np.mean(arr)) - 0.5 * s ** 2
sample = ot.Sample.BuildFromPoint((arr1))
print(stats.anderson(arr, 'expon'))
#print(stats.anderson(arr, 'norm'))
test_result = ot.NormalityTest.AndersonDarlingNormal(sample)
print(test_result)
print(np.mean(arr1),(np.std(arr1)))
fig = sm.qqplot(arr, stats.expon, fit=True, line="45")
plt.show()
fig1 = sm.qqplot(arr, stats.lognorm, fit=True, line="45")
plt.show()