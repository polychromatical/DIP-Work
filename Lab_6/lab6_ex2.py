# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:08:04 2020

@author: User
"""

import numpy as np
import cv2
from matplotlib import pyplot as pt

simple_image = np.zeros((256,256),dtype=np.float64)
simple_image[124:132,124:132] = 255

fourier_coeff = np.fft.fft2(simple_image)
fourier_coeff_center = np.fft.fftshift(fourier_coeff)
spectrum = np.abs(fourier_coeff_center)
spectrum_log = np.log(1+spectrum)

fourier_coeff_origin = np.fft.ifftshift(fourier_coeff_center)
fourier_coeff_inv = np.fft.ifft2(fourier_coeff_origin)
recreated_img = np.abs(fourier_coeff_inv)

pt.figure()
pt.subplot(2,2,1)
pt.imshow(simple_image,cmap="gray")
pt.title("Simple Image")

pt.subplot(2,2,2)
pt.imshow(spectrum,cmap="gray")
pt.title("Before Log Enhanced")

pt.subplot(2,2,3)
pt.imshow(spectrum_log,cmap="gray")
pt.title("After Log Enhanced")
pt.show()

pt.subplot(2,2,4)
pt.imshow(recreated_img, cmap="gray")
pt.title("Simple Image (Recreated)")

pt.show()
