# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:56:08 2020

@author: User
"""

import numpy as np
import cv2
from matplotlib import pyplot as pt
from filter import lpfilter

f = cv2.imread("cameraman.bmp",0)

F = np.fft.fft2(f)
Fs = np.fft.fftshift(F)

spectrum_h = np.log(1+np.abs(Fs))

[nrow,ncol] = f.shape
H = lpfilter(nrow,ncol,"ideal",75)

G = H * Fs

spectrum_g = np.log(1+np.abs(G))

Gs = np.fft.ifftshift(G)
g = np.fft.ifft2(Gs)

g = g.real
g[g < 0] = 0
g[g > 255] = 255


pt.figure()
pt.subplot(2,2,1)
pt.imshow(spectrum_h,cmap="gray")
pt.title("Before")

pt.subplot(2,2,3)
pt.imshow(H,cmap="gray")
pt.title("Enchancement")

pt.subplot(2,2,2)
pt.imshow(spectrum_g,cmap="gray")
pt.title("Filter")

pt.subplot(2,2,4)
pt.imshow(g,cmap="gray")
pt.title("After")
