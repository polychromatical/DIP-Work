# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:20:00 2020

@author: User
"""

from matplotlib import pyplot as pt
import cv2

img_1 = cv2.imread("sunway_university.png")
img_2 = pt.imread("sunway_pyramid.png")

cv2.imshow("University", img_1)
cv2.waitKey()

img_plot = pt.imshow(img_2)
