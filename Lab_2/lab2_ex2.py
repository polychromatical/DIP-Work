# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:03:10 2020

@author: User
"""
import numpy

array1 = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

array2 = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])

array3 = numpy.array([[1],[2],[3],[4]])

array2D_int = numpy.array ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],dtype=numpy.int32)

array2D_int[0:4,0] = 2,0,1,4

