# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:31:35 2020

@author: User
"""

import cv2
import numpy as np
from matplotlib import pyplot as pt
from filter import brfilter

# Original image
f = cv2.imread("cman_periodic.bmp", 0)

# Shifting image to spectrum mode
F = np.fft.fft2(f)
Fs = np.fft.fftshift(F)

spectrum_h = np.log(1+np.abs(Fs))

# Creating Band Reject filter

def calcLength(start, end):
    lgx = end[0] - start[0]
    lgy = end[1] - start[1]
    
    hypo = np.sqrt(np.power(lgx, 2) + np.power(lgy, 2))
    return hypo

pt1 = calcLength([128, 128], [103, 153])
pt2 = calcLength([128, 128], [78, 128])
pt3 = calcLength([128, 128], [103, 103])
pt4 = calcLength([128, 128], [128, 78])
pt5 = calcLength([128, 128], [153, 103])
pt6 = calcLength([128, 128], [178, 128])
pt7 = calcLength([128, 128], [128, 178])
pt8 = calcLength([128, 128], [153, 153])

[nrow, ncol] = f.shape

br1 = brfilter(nrow, ncol, "ideal", pt1, 2)
br2 = brfilter(nrow, ncol, "ideal", pt2, 2)


# Applying filter to image

img1 = br1 * br2 * Fs

spectrum_g = np.log(1+np.abs(img1))

img1s = np.fft.ifftshift(img1)
img1b = np.fft.ifft2(img1s)

g = img1b.real
g[g < 0] = 0
g[g > 255] = 255

# Display

pt.figure()
pt.subplot(1,2,1)
pt.imshow(f, cmap="gray")
pt.title("Before")

pt.subplot(1,2,2)
pt.imshow(g, cmap="gray")
pt.title("Final")