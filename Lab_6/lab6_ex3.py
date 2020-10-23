# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:08:04 2020

@author: User
"""

import numpy as np
import cv2
from matplotlib import pyplot as pt

c_img = cv2.imread("cameraman.bmp", 0)

fourier_coeff = np.fft.fft2(c_img)
fourier_coeff_center = np.fft.fftshift(fourier_coeff)

spectrum = np.abs(fourier_coeff_center)
spectrum_log = np.log(1+spectrum)

phase = np.angle(fourier_coeff_center)
phase = np.abs(phase)

pt.figure()
pt.subplot(2, 2, 1)
pt.imshow(c_img, cmap="gray")
pt.title("Original Image")

pt.subplot(2, 2, 2)
pt.imshow(spectrum, cmap="gray")
pt.title("Spectrum before Log Enhancement")

pt.subplot(2, 2, 3)
pt.imshow(spectrum_log, cmap="gray")
pt.title("Spectrum After Log Enhancement")

fourier_coeff_origin = np.fft.ifftshift(fourier_coeff_center)
fourier_coeff_inv = np.fft.ifft2(fourier_coeff_origin)
recreated_img = np.abs(fourier_coeff_inv)

pt.subplot(2, 2, 4)
pt.imshow(phase, cmap="gray")
pt.title("Phase")

pt.show()
