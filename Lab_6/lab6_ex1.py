# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:06:22 2020

@author: User
"""

import numpy as np

arr2D = np.array([[9,8], [19,60]])
print(arr2D)

dft_arr2D = np.fft.fft2(arr2D)
print(dft_arr2D)

redft_arr2D = np.fft.ifft2(dft_arr2D)
redft_arr2D = np.abs(redft_arr2D)
print(redft_arr2D)