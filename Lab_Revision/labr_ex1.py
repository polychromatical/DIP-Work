# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:19:17 2020

@author: User
"""

import numpy as np

img_a = np.array([[10,20,30,40]],dtype=np.uint8)
img_b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],dtype=np.float64)
img_c = np.zeros((10,100),dtype=np.float64)

num = 1
for x in range(0,10):
    for y in range(0,100):
        img_c[x,y] = num
        num += 1
        
# Part (i)

centrePixels = []
for m in range (0,4):
    for n in range (0,4):
        if m > 0 and m < 3:
            if n > 0 and n < 3: 
                centrePixels.append(int(img_b[m,n]))

# Part (ii)

for i in range(0,4):
    img_b[0,i] = img_a[0,i]
    
