#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:29:19 2021

@author: ijin
"""

import numpy as np
import matplotlib.pyplot as plt

m = 10
sigma = 2
x1 = np.random.randn(10000)
x2 = m + sigma*np.random.randn(10000)

plt.figure(figsize =(10, 6))
plt.hist(x1, bins = 20, alpha =0.4)
plt.hist(x2, bins = 20, alpha = 0.4)
plt.show()