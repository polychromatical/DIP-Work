# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 17:18:56 2020

@author: User
"""

import cv2

char_img = cv2.imread("char.bmp", 0)
# cv2.imshow("Char", char_img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# zero_img = cv2.copyMakeBorder(char_img,1,1,1,1,cv2.BORDER_CONSTANT,0)

output1 = cv2.blur(char_img, (3, 3), cv2.BORDER_CONSTANT)

cv2.imshow("Output 1", output1)
cv2.waitKey()

output2 = cv2.blur(char_img, (5, 5), cv2.BORDER_CONSTANT)

cv2.imshow("Output 2", output2)
cv2.waitKey()

output3 = cv2.blur(char_img, (7, 7), cv2.BORDER_CONSTANT)

cv2.imshow("Output 3", output3)
cv2.waitKey()
cv2.destroyAllWindows()