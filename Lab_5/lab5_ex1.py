# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:52:34 2020

@author: User
"""
import numpy as np
import cv2

img = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.float64)

zero_img = cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_CONSTANT,0)
repli_img = cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_REPLICATE)