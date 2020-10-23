# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 15:35:11 2020

@author: User
"""

import numpy as np
import cv2

word1 = cv2.imread("word1.bmp",0)
word1_f64 = word1.astype(np.float64)

word2 = cv2.imread("word2.bmp",0)
word2_f64 = word2.astype(np.float64)

word3 = cv2.imread("word3.bmp",0)
word3_f64 = word3.astype(np.float64)

full_word = word1_f64 + word2_f64 + word3_f64

max_value = full_word.max()
scl_word = (full_word/max_value)*255

norm_word = scl_word.astype(np.uint8)
cv2.imshow("Full Word", norm_word)
cv2.waitKey()
cv2.destroyAllWindows()

