# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:57:37 2020

@author: User
"""

import numpy as np
import cv2
from matplotlib import pyplot as pt
from filter import lpfilter

f = cv2.imread("cameraman.bmp",0)

F = np.fft.fft2(f)
Fs = np.fft.fftshift(F)

[nrow,ncol] = f.shape

# Ideal

Hi = lpfilter(nrow,ncol,"ideal",25)

Gi = Hi * Fs

Gsi = np.fft.ifftshift(Gi)
gi = np.fft.ifft2(Gsi)

gi = gi.real
gi[gi < 0] = 0
gi[gi > 255] = 255

pt.figure()
pt.subplot(1,2,1)
pt.imshow(f,cmap="gray")
pt.title("Before Ideal")

pt.subplot(1,2,2)
pt.imshow(gi,cmap="gray")
pt.title("After Ideal")

# Butterworth

Hb = lpfilter(nrow,ncol,"btw",25,5)

Gb = Hb * Fs

Gsb = np.fft.ifftshift(Gb)
gb = np.fft.ifft2(Gsb)

gb = gb.real
gb[gb < 0] = 0
gb[gb > 255] = 255

pt.figure()
pt.subplot(1,2,1)
pt.imshow(f,cmap="gray")
pt.title("Before Butterworth")

pt.subplot(1,2,2)
pt.imshow(gb,cmap="gray")
pt.title("After Butterworth")

# Gaussian

Hg = lpfilter(nrow,ncol,"gaussian",25)

Gg = Hg * Fs

Gsg = np.fft.ifftshift(Gg)
gg = np.fft.ifft2(Gsg)

gg = gg.real
gg[gg < 0] = 0
gg[gg > 255] = 255

pt.figure()
pt.subplot(1,2,1)
pt.imshow(f,cmap="gray")
pt.title("Before Gaussian")

pt.subplot(1,2,2)
pt.imshow(gg,cmap="gray")
pt.title("After Gaussian")