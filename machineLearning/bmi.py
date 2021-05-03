#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:27:42 2021

@author: ijin
"""
import numpy as np
start = 1
end = 2
heights = np.round_((end - start)*np.random.rand(10) +start , 2)
weights = np.random.randint(50, 100, size = 10 )

print("random heights:", heights)
print("random weights:" ,weights)

np_heights = np.array(heights)
np_weights = np.array(weights)

bmi =np.round_(np_weights / (np_heights ** 2) , 2)

print("bmi >= 25:", bmi[bmi >= 25])


