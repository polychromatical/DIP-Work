# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 02:38:17 2020

@author: User
"""

from matplotlib import pyplot as pt
import numpy as np
import cv2

# Not normalised histograms

# Book

book = cv2.imread("book.bmp",0)
cv2.imshow("Book", book)
cv2.waitKey()

hist_book = cv2.calcHist([book],[0],None,[256],[0,256])

pt.figure()

pt.title("Grayscale Histogram Book")
pt.xlabel("Bins")
pt.ylabel("Number of Pixels")

pt.plot(hist_book)
pt.xlim([0,256])

pt.show()

# Car

car = cv2.imread("car.bmp",0)
cv2.imshow("Car", car)
cv2.waitKey()

hist_car = cv2.calcHist([car],[0],None,[256],[0,256])

pt.figure()

pt.title("Grayscale Histogram Car")
pt.xlabel("Bins")
pt.ylabel("Number of Pixels")

pt.plot(hist_car)
pt.xlim([0,256])

pt.show()

# Building

building = cv2.imread("building.bmp",0)
cv2.imshow("Building", building)
cv2.waitKey()

hist_building = cv2.calcHist([building],[0],None,[256],[0,256])

pt.figure()

pt.title("Grayscale Histogram Building")
pt.xlabel("Bins")
pt.ylabel("Number of Pixels")

pt.plot(hist_building)
pt.xlim([0,256])

pt.show()

# Subway

subway = cv2.imread("subway.bmp",0)
cv2.imshow("Subway", subway)
cv2.waitKey()

hist_subway = cv2.calcHist([subway],[0],None,[256],[0,256])

pt.figure()

pt.title("Grayscale Histogram Subway")
pt.xlabel("Bins")
pt.ylabel("Number of Pixels")

pt.plot(hist_subway)
pt.xlim([0,256])

pt.show()

# Normalised Histograms

# Book

[nrow,ncol] = book.shape
total_no_pixels = nrow * ncol
norm_book = hist_book / total_no_pixels

pt.title("Normalised Histogram Book")
pt.xlabel("Bins")
pt.ylabel("Number of Pixels")

pt.plot(norm_book)
pt.xlim([0,256])

pt.show()

# Car

[nrow,ncol] = car.shape
total_no_pixels = nrow * ncol
norm_car = hist_car / total_no_pixels

pt.title("Normalised Histogram Car")
pt.xlabel("Bins")
pt.ylabel("Number of Pixels")

pt.plot(norm_car)
pt.xlim([0,256])

pt.show()

# Building

[nrow,ncol] = building.shape
total_no_pixels = nrow * ncol
norm_building = hist_building / total_no_pixels

pt.title("Normalised Histogram Building")
pt.xlabel("Bins")
pt.ylabel("Number of Pixels")

pt.plot(norm_building)
pt.xlim([0,256])

pt.show()

# Subway

[nrow,ncol] = subway.shape
total_no_pixels = nrow * ncol
norm_subway = hist_subway / total_no_pixels

pt.title("Normalised Histogram Subway")
pt.xlabel("Bins")
pt.ylabel("Number of Pixels")

pt.plot(norm_subway)
pt.xlim([0,256])

pt.show()