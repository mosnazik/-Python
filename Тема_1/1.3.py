import random
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
m=500
xcord_t=[]
ycord_t=[]
xcord_c=[]
ycord_c=[]
def generator():
    x=random.random()*100
    y=random.random()*100
    return x, y
for i in range(1):
    vector = []
    x_1=random.random()*100
    y_1=random.random()*100
    vector.append(x_1)
    vector.append(y_1)
    for i in range(1,5):
        x,y=generator()
        while True:
            ind = 1
            for j in range(i):
                if np.sqrt((vector[2*j]-x)*(vector[2*j]-x)+(vector[2*j+1]-y)*(vector[2*j+1]-y))<40:
                    x, y = generator()
                    ind = 0
            if ind==1:
                break
        vector.append(x)
        vector.append(y)
    for i in range(10):
        x,y=generator()
        while True:
            ind = 1
            if (np.sqrt((vector[2*(i//2)] - x) * (vector[2*(i//2)] - x) + (vector[2*(i//2) + 1] - y) * (vector[2*(i//2) + 1] - y)) > 20) or (np.sqrt((vector[2*(i//2)] - x) * (vector[2*(i//2)] - x) + (vector[2*(i//2) + 1] - y) * (vector[2*(i//2) + 1] - y)) < 10):
                x, y = generator()
                ind = 0
            for j in range(0, i):
                if np.sqrt((vector[10+2*j]-x)*(vector[10+2*j]-x)+(vector[2*j+11]-y)*(vector[2*j+11]-y))<10:
                    x, y = generator()
                    ind = 0
            if ind==1:
                break
        vector.append(x)
        vector.append(y)
    #print(vector)
    for i in range(m):
        n=random.randint(0,14)
        if n<5:
            x, y = generator()
            while True:
                ind = 1
                for j in range(5):
                    if j==n:
                        continue
                    if np.sqrt((vector[2 * j] - x) * (vector[2 * j] - x) + (vector[2 * j + 1] - y) * (
                            vector[2 * j + 1] - y)) < 40:
                        x, y = generator()
                        ind = 0
                if ind == 1:
                    break
            vector[2 * n] = x
            vector[2 * n + 1] = y
            n = 2 * n + 5
            for i in range(2):
                n=n+i
                x, y = generator()
                while True:
                    ind = 1
                    if (np.sqrt((vector[2 * ((n - 5) // 2)] - x) * (vector[2 * ((n - 5) // 2)] - x) + (
                            vector[2 * ((n - 5) // 2) + 1] - y) * (
                                        vector[2 * ((n - 5) // 2) + 1] - y)) > 20) or (
                            np.sqrt((vector[2 * ((n - 5) // 2)] - x) * (vector[2 * ((n - 5) // 2)] - x) + (
                                    vector[2 * ((n - 5) // 2) + 1] - y) * (
                                            vector[2 * ((n - 5) // 2) + 1] - y)) < 10):
                        x, y = generator()
                        ind = 0
                    for j in range(10):
                        if j == (n - 5):
                            continue
                        if np.sqrt((vector[10 + 2 * j] - x) * (vector[10 + 2 * j] - x) + (vector[2 * j + 11] - y) * (
                                vector[2 * j + 11] - y)) < 10:
                            x, y = generator()
                            ind = 0
                    if ind == 1:
                        break
                vector[2 * n] = x
                vector[2 * n + 1] = y
        else:
            x, y = generator()
            while True:
                ind = 1
                if (np.sqrt((vector[2 * ((n-5) // 2)] - x) * (vector[2 * ((n-5) // 2)] - x) + (vector[2 * ((n-5) // 2) + 1] - y) * (
                        vector[2 * ((n-5) // 2) + 1] - y)) > 20) or (
                        np.sqrt((vector[2 * ((n-5) // 2)] - x) * (vector[2 * ((n-5) // 2)] - x) + (vector[2 * ((n-5) // 2) + 1] - y) * (
                                vector[2 * ((n-5) // 2) + 1] - y)) < 10):
                    x, y = generator()
                    ind = 0
                for j in range(10):
                    if j==(n-5):
                        continue
                    if np.sqrt((vector[10 + 2 * j] - x) * (vector[10 + 2 * j] - x) + (vector[2 * j + 11] - y) * (
                            vector[2 * j + 11] - y)) < 10:
                        x, y = generator()
                        ind = 0
                if ind == 1:
                    break
            vector[2 * n]=x
            vector[2 * n + 1]=y
    #print(vector)
    for i in range(15):
        if i<5:
            xcord_t.append(vector[2*i])
            ycord_t.append(vector[2*i+1])
        else:
            xcord_c.append(vector[2 * i])
            ycord_c.append(vector[2 * i + 1])
plt.scatter(xcord_t,ycord_t, marker='s')
plt.scatter(xcord_c,ycord_c, marker='^')
plt.axis([-10, 110, -10, 110])
plt.legend(["Towns", "Caves"])
plt.show()
