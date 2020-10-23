# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 15:37:25 2020

@author: User
"""

import numpy
import cv2

img = cv2.imread("ufo.bmp",0)
# cv2.imshow("Ufo",img)
# cv2.waitKey()

new_img = img * 10

cv2.imshow("New Ufo", new_img)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite("baboon.bmp", new_img)