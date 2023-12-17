import seaborn as sns
import pandas as pd
import numpy as np
import math
import openturns as ot
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
sredn=1.6180339887
data_table = pd.io.parsers.read_table("shoshoni.txt")
arr=data_table["Ratio"].to_numpy()
s=np.sqrt(np.log(1 + (np.std(arr) / np.mean(arr)) ** 2))
lambda_value = np.log(np.mean(arr)) - 0.5 * s ** 2
arr1=[]
for i in range(len(arr)):
  arr1.append(np.log(arr[i]))
sample = ot.Sample.BuildFromPoint((arr1))
sample1 = ot.Sample.BuildFromPoint((arr))
print("sredneee",np.mean(arr))
print(stats.anderson(arr, 'expon'))
#print(stats.kstest(arr, stats.expon(scale=np.mean(arr)).cdf))
#print(stats.cramervonmises(arr, 'expon'))
#print(stats.kstest(arr, stats.lognorm(s=s,scale=np.exp(lambda_value)).cdf))
#print(stats.kstest(arr, stats.norm(np.mean(arr),scale=np.std(arr)).cdf))
#print(stats.cramervonmises(arr, 'norm'))
#print(stats.anderson(arr, 'norm'))
#print(stats.cramervonmises(arr1, 'norm'))
print(stats.anderson(arr1, 'norm'))
print(stats.normaltest(arr1).pvalue)
test_result = ot.NormalityTest.AndersonDarlingNormal(sample)
print(test_result)
test_result = ot.NormalityTest.AndersonDarlingNormal(sample1)
print(test_result)
print(stats.ttest_1samp(arr, popmean=1/sredn))
fig, ax = plt.subplots(1,3)
fig = sm.qqplot(arr, stats.expon, fit=True, line="45",ax=ax[0],)
ax[0].title.set_text('expon')
fig1 = sm.qqplot(arr, stats.lognorm, fit=True, line="45",ax=ax[1])
ax[1].title.set_text('lognorm')
fig1 = sm.qqplot(arr, stats.norm, fit=True, line="45",ax=ax[2])
ax[2].title.set_text('norm')
plt.show()