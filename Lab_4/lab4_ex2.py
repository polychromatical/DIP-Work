# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 03:04:08 2020

@author: User
"""

from matplotlib import pyplot as pt
import numpy as np
import cv2

build = cv2.imread("building.bmp", 0)
build_eq = cv2.equalizeHist(build)

build_n_build_eq = np.concatenate((build,build_eq),1)

cv2.imshow("Before & After", build_n_build_eq)
cv2.waitKey()

pt.figure()

pt.subplot(1,2,1)
pt.imshow(build, cmap="gray")
pt.title("Before")

pt.subplot(1,2,2)
pt.imshow(build_eq, cmap="gray")
pt.title("After")

pt.show()
