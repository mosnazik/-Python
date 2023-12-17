import random
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#Выпадение зла - 0.5, добра - 0.2, хаоса - 0.3
#267-два синяя, 73 - два зеленая, 29- два красная, 140 - к и з, 193 - к и с, 298 - с и з
#c=1,з=0,к=-1
import numpy as np
p1=2000
p2=0
p3=0
for i in range(267):
    p1=p1-2
    p2 = p2 + 2
    p3 = p3
for i in range(29):
    p1=p1-2
    p2 = p2
    p3 = p3+2
for i in range(140):
    p1=p1-1
    p2 = p2
    p3 = p3+1
for i in range(193):
    p1=p1-2
    p2 = p2 + 1
    p3 = p3+1
for i in range(298):
    p1=p1-1
    p2 = p2 + 1
    p3 = p3
a=[0.2,0.3,0.2,0.5,0.3,0.2,0.3,0.5,0.5,0.3,0.5,0.2]
b=p1*np.log(a[0])+p2*np.log(a[1])+p3*np.log(1-a[0]-a[1])
k=0
for i in range(6):
    c=p1*np.log(a[i*2])+p2*np.log(a[i*2+1])+p3*np.log(1-a[i*2]-a[i*2+1])
    print(c)
    if c>b:
        c=b
        k=i
    #print(a[i*2],a[i*2+1])
print("Синий с вер:",a[k*2],"Зеленый с вер:",a[k*2+1],"Красный с вер:", 1-a[k*2]-a[k*2+1])