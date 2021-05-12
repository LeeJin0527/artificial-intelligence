#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 22:12:16 2021

@author: ijin
"""

import matplotlib.pylab as plt
from sklearn import linear_model
import numpy as np
reg = linear_model.LinearRegression()
n_point = 18
x_batch = np.linspace(0, 175, n_point)

random_noise = 2*np.random.randn(n_point)
y = 0.2 * x_batch + random_noise
x_batch = np.reshape(x_batch, (-1,1))

reg.fit(x_batch, y)
plt.scatter(x_batch, y, color = 'black')

y_pred = reg.predict(x_batch)

x_batch = x_batch.reshape(-1)
y_pred = y_pred.reshape(-1)

plt.plot(x_batch, y_pred, color='blue',linewidth=3)
plt.show()
answer = input("주택의 면적을 입력하세요: ")

print("예상 주택 가격은:" , reg.predict([[int(answer)]]))