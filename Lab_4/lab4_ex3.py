# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 03:20:58 2020

@author: User
"""

from matplotlib import pyplot as pt
import numpy as np
import cv2

coins = cv2.imread("coins.bmp",0)
[nrow,ncol] = coins.shape
bi_img = np.zeros((nrow,ncol),dtype=np.)

threshold = 100
for x in range(0,nrow):
    for y in range(0,ncol):
        if coins[x,y] >= threshold:
            bi_img[x,y] = 1
        else:
            bi_img[x,y] = 0
            
ex_coins = bi_img * coins

pt.figure()

pt.subplot(1,3,1)
pt.imshow(coins, cmap="gray")
pt.title("Original Image")

pt.subplot(1,3,2)
pt.imshow(bi_img, cmap="gray")
pt.title("Binary Image")

pt.subplot(1,3,3)
pt.imshow(ex_coins, cmap="gray")
pt.title("Extracted Coins")

pt.show()