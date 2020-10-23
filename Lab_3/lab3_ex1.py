# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 15:33:28 2020

@author: User
"""
import numpy
import cv2

img = cv2.imread("cameraman.bmp",0)

cv2.imshow("Cameraman",img)
cv2.waitKey()
cv2.destroyAllWindows()

height, width = img.shape

for x in range(0, width):
    for y in range(0, height):
        if x < (width/2) and y < (height/2):
            img[x,y] = 0

cv2.imshow("New Cameraman",img)
cv2.waitKey()
cv2.destroyAllWindows()

