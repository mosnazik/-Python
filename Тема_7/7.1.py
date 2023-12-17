import seaborn as sns
import pandas as pd
import numpy as np
import math
import dcor
from hyppo.independence import HHG
import openturns as ot
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
from tqdm import tqdm
n=20
n1=50
N=30
p1=np.zeros((5, N))
p2=np.zeros((5, N))
p3=np.zeros((5, N))
p4=np.zeros((5, N))
p5=np.zeros((5, N))
p6=np.zeros((5, N))
for k in range(N):
    x=stats.norm(1,scale=1).rvs(size=n)
    y=stats.norm(1,scale=1).rvs(size=n)
    x1=stats.norm(1,scale=1).rvs(size=n1)
    y1=stats.norm(1,scale=1).rvs(size=n1)
    a = stats.multivariate_normal(mean=[1.0, 1.0], cov=[[1, 0.5], [0.5, 1]]).rvs(size=n)
    a = a.T
    x4=a[0]
    y4=a[1]
    a = stats.multivariate_normal(mean=[1.0, 1.0], cov=[[1, 0.5], [0.5, 1]]).rvs(size=n1)
    a = a.T
    x5=a[0]
    y5=a[1]
    x2=np.zeros(n)
    y2=np.zeros(n)
    for j in range(5):
        a=stats.multivariate_normal(mean=[1.0, 1.0], cov=[[1, 0.5], [0.5, 1]]).rvs(size=n)
        a=a.T
        for i in range(n):
            x2[i]=x2[i] + a[0][i]**2
            y2[i] = y2[i] + a[1][i]**2
    x3=np.zeros(n1)
    y3=np.zeros(n1)
    for j in range(5):
        a=stats.multivariate_normal([1.0, 1.0], [[1, 0.5], [0.5, 1]]).rvs(size=n1)
        a=a.T
        for i in range(n1):
            x3[i]=x3[i] + a[0][i]**2
            y3[i] = y3[i] + a[1][i]**2
    sum1=np.zeros(n)
    sum2=np.zeros(n)
    for j in range(5):
        a=stats.multivariate_normal([1.0, 1.0], [[1, 0.5], [0.5, 1]]).rvs(size=n)
        a=a.T
        for i in range(n):
            sum1[i]=sum1[i] + a[0][i]**2
            sum2[i] = sum2[i] + a[1][i]**2
    sum3=np.zeros(n1)
    sum4=np.zeros(n1)
    for j in range(5):
        a=stats.multivariate_normal([1.0, 1.0], [[1, 0.5], [0.5, 1]]).rvs(size=n1)
        a=a.T
        for i in range(n1):
            sum3[i]=sum3[i] + a[0][i]**2
            sum4[i] = sum4[i] + a[1][i]**2
    for i in range(n):
        x4[i]=x4[i]/np.sqrt(sum1[i]/5)
        y4[i]=y4[i]/np.sqrt(sum2[i]/5)
    for i in range(n1):
        x5[i]=x5[i]/np.sqrt(sum3[i]/5)
        y5[i]=y5[i]/np.sqrt(sum4[i]/5)
    # for i in range(len(x)):
    #     y.append(-2*x[i])
    p1[0][k]=(stats.pearsonr(x,y).pvalue)
    p1[1][k] =(stats.spearmanr(x, y).pvalue)
    p1[2][k]=(stats.kendalltau(x,y).pvalue)
    p1[3][k]=(dcor.independence.distance_correlation_t_test(x,y).pvalue)
    p1[4][k]=(HHG().test(x, y).pvalue)
    p2[0][k]=(stats.pearsonr(x1,y1).pvalue)
    p2[1][k]=(stats.spearmanr(x1, y1).pvalue)
    p2[2][k]=(stats.kendalltau(x1,y1).pvalue)
    p2[3][k]=(dcor.independence.distance_correlation_t_test(x1,y1).pvalue)
    p2[4][k]=(HHG().test(x1, y1).pvalue)
    x=np.array(x2)
    y=np.array(y2)
    p3[0][k] = (stats.pearsonr(x, y).pvalue)
    p3[1][k] = (stats.spearmanr(x, y).pvalue)
    p3[2][k] = (stats.kendalltau(x, y).pvalue)
    p3[3][k] = (dcor.independence.distance_correlation_t_test(x, y).pvalue)
    p3[4][k] = (HHG().test(x, y).pvalue)
    x1=np.array(x3)
    y1=np.array(y3)
    p4[0][k] = (stats.pearsonr(x1, y1).pvalue)
    p4[1][k] = (stats.spearmanr(x1, y1).pvalue)
    p4[2][k] = (stats.kendalltau(x1, y1).pvalue)
    p4[3][k] = (dcor.independence.distance_correlation_t_test(x1, y1).pvalue)
    p4[4][k] = (HHG().test(x1, y1).pvalue)
    x=np.array(x4)
    y=np.array(y4)
    p5[0][k] = (stats.pearsonr(x, y).pvalue)
    p5[1][k] = (stats.spearmanr(x, y).pvalue)
    p5[2][k] = (stats.kendalltau(x, y).pvalue)
    p5[3][k] = (dcor.independence.distance_correlation_t_test(x, y).pvalue)
    p5[4][k] = (HHG().test(x, y).pvalue)
    x1=np.array(x5)
    y1=np.array(y5)
    p6[0][k] = (stats.pearsonr(x1, y1).pvalue)
    p6[1][k] = (stats.spearmanr(x1, y1).pvalue)
    p6[2][k] = (stats.kendalltau(x1, y1).pvalue)
    p6[3][k] = (dcor.independence.distance_correlation_t_test(x1, y1).pvalue)
    p6[4][k] = (HHG().test(x1, y1).pvalue)
fig, ax = plt.subplots(2, 5)
ax[0,0].set_title("Критерий Пирсона")
stats.ecdf(p1[0]).cdf.plot(ax[0,0])
ax[0,1].set_title("Критерий Спирмена")
stats.ecdf(p1[1]).cdf.plot(ax[0,1])
ax[0,2].set_title("Критерий Кенделла")
stats.ecdf(p1[2]).cdf.plot(ax[0,2])
ax[0,3].set_title("Критерий Cекея-Риззо")
stats.ecdf(p1[3]).cdf.plot(ax[0,3])
ax[0,4].set_title("Критерий Хеллера, Хеллера и Горфина")
stats.ecdf(p1[4]).cdf.plot(ax[0,4])
stats.ecdf(p2[0]).cdf.plot(ax[1,0])
stats.ecdf(p2[1]).cdf.plot(ax[1,1])
stats.ecdf(p2[2]).cdf.plot(ax[1,2])
stats.ecdf(p2[3]).cdf.plot(ax[1,3])
stats.ecdf(p2[4]).cdf.plot(ax[1,4])
plt.show()
fig, ax = plt.subplots(2, 5)
ax[0,0].set_title("Критерий Пирсона")
stats.ecdf(p3[0]).cdf.plot(ax[0,0])
ax[0,1].set_title("Критерий Спирмена")
stats.ecdf(p3[1]).cdf.plot(ax[0,1])
ax[0,2].set_title("Критерий Кенделла")
stats.ecdf(p3[2]).cdf.plot(ax[0,2])
ax[0,3].set_title("Критерий Cекея-Риззо")
stats.ecdf(p3[3]).cdf.plot(ax[0,3])
ax[0,4].set_title("Критерий Хеллера, Хеллера и Горфина")
stats.ecdf(p3[4]).cdf.plot(ax[0,4])
stats.ecdf(p4[0]).cdf.plot(ax[1,0])
stats.ecdf(p4[1]).cdf.plot(ax[1,1])
stats.ecdf(p4[2]).cdf.plot(ax[1,2])
stats.ecdf(p4[3]).cdf.plot(ax[1,3])
stats.ecdf(p4[4]).cdf.plot(ax[1,4])
plt.show()
fig, ax = plt.subplots(2, 5)
ax[0,0].set_title("Критерий Пирсона")
stats.ecdf(p5[0]).cdf.plot(ax[0,0])
ax[0,1].set_title("Критерий Спирмена")
stats.ecdf(p5[1]).cdf.plot(ax[0,1])
ax[0,2].set_title("Критерий Кенделла")
stats.ecdf(p5[2]).cdf.plot(ax[0,2])
ax[0,3].set_title("Критерий Cекея-Риззо")
stats.ecdf(p5[3]).cdf.plot(ax[0,3])
ax[0,4].set_title("Критерий Хеллера, Хеллера и Горфина")
stats.ecdf(p5[4]).cdf.plot(ax[0,4])
stats.ecdf(p6[0]).cdf.plot(ax[1,0])
stats.ecdf(p6[1]).cdf.plot(ax[1,1])
stats.ecdf(p6[2]).cdf.plot(ax[1,2])
stats.ecdf(p6[3]).cdf.plot(ax[1,3])
stats.ecdf(p6[4]).cdf.plot(ax[1,4])
plt.show()
