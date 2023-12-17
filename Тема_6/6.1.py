import seaborn as sns
import pandas as pd
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr, data
from rpy2.robjects import numpy2ri
import numpy as np
import math
import openturns as ot
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
utils = importr('utils')

utils.chooseCRANmirror(ind=1)
utils.install_packages('BWStest')
BWStest = importr('BWStest')
N=200
n=20
n2=100
n1=4
p11=[]
p12=[]
p21=[]
p22=[]
p31=[]
p32=[]
p41=[]
p42=[]
p51=[]
p52=[]
a=0.8
for k in range(N):
    x=stats.norm(1,scale=1).rvs(size=n)
    x1=stats.norm(2,scale=2).rvs(size=n)
    x2=stats.norm(1,scale=1).rvs(size=n2)
    x3=stats.norm(2,scale=2).rvs(size=n2)
    y=[]
    for i in range(n):
        y.append([x[i],0])
        y.append([x1[i], 1])
    y1 = []
    for i in range(n2):
        y1.append([x2[i], 0])
        y1.append([x3[i], 1])
    y.sort()
    y1.sort()
    pop1 = np.zeros(n//5)
    pop2 = np.zeros(n//5)
    pop3 = np.zeros(n2//10)
    pop4 = np.zeros(n2//10)
    for i in range(n//5):
        for j in range(5):
            if y[i*5+j][1] == 0:
                pop1[i]=pop1[i]+1
            else:
                pop2[i] = pop2[i] + 1
    for i in range(n2//10):
        for j in range(10):
            if y1[i*10+j][1] ==0:
                pop3[i]=pop3[i]+1
            else:
                pop4[i] = pop4[i] + 1
    p11.append(stats.chi2_contingency([pop1,pop2]).pvalue)
    p12.append(stats.chi2_contingency([pop3,pop4]).pvalue)
    if np.isnan(stats.mannwhitneyu(x,x1).pvalue) or np.isnan(stats.mannwhitneyu(x2,x3).pvalue):
        continue
    if np.isnan(stats.ttest_ind(x,x1, equal_var=False).pvalue) or np.isnan(stats.ttest_ind(x2,x3, equal_var=False).pvalue):
        continue
    p21.append(stats.mannwhitneyu(x,x1).pvalue)
    p22.append(stats.mannwhitneyu(x2,x3).pvalue)
    p31.append(stats.ks_2samp(x,x1).pvalue)
    p32.append(stats.ks_2samp(x2,x3).pvalue)
    p41.append(stats.ttest_ind(x,x1, equal_var=False).pvalue)
    p42.append(stats.ttest_ind(x2,x3, equal_var=False).pvalue)
    numpy2ri.activate()
    x=np.asarray(x,dtype=float)
    x1=np.asarray(x1,dtype=float)
    rez=BWStest.bws_test(x,x1)
    rez1 = BWStest.bws_test(x2, x3)
    #print(rez)
    numpy2ri.deactivate()
    p51.append(np.array(rez[1])[0])
    p52.append(np.array(rez1[1])[0])
# fig, ax = plt.subplots(1, 2)
# stats.ecdf(p11).cdf.plot(ax[0])
# stats.ecdf(p12).cdf.plot(ax[1])
# plt.show()
fig, ax = plt.subplots(2, 5)
ax[0,0].set_title("Критерий Манна-Уитни")
stats.ecdf(p21).cdf.plot(ax[0,0])
stats.ecdf(p22).cdf.plot(ax[1,0])
ax[0,1].set_title("Критерий Колмогорова")
stats.ecdf(p31).cdf.plot(ax[0,1])
stats.ecdf(p32).cdf.plot(ax[1,1])
ax[0,2].set_title("Критерий Стьюдента")
stats.ecdf(p41).cdf.plot(ax[0,2])
stats.ecdf(p42).cdf.plot(ax[1,2])
ax[0,3].set_title("Критерий Баумгартнера-Вейсса-Шиндлера")
stats.ecdf(p51).cdf.plot(ax[0,3])
stats.ecdf(p52).cdf.plot(ax[1,3])
ax[0,4].set_title("Критерий хи-квадрат")
stats.ecdf(p11).cdf.plot(ax[0,4])
stats.ecdf(p12).cdf.plot(ax[1,4])
plt.show()
