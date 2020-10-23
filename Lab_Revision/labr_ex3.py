# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:20:08 2020

@author: User
"""

import numpy as np
import cv2

cmr_img = cv2.imread("distorted_cameraman.bmp", 0)

cmrmn_img = cmr_img * 5
cmrmn_img += 30

concat_img = np.concatenate((cmr_img, cmrmn_img), axis=1)

cv2.imshow("Cameraman", concat_img)
cv2.waitKey()
cv2.destroyAllWindows()