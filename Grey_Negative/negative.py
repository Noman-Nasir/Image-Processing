# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:19:48 2019

@author: Noman Nasir
"""

import cv2


imageNmae = 'blue'
grayImage = cv2.imread(imageNmae+'.jpg',1)

i = 0
while i < grayImage.__len__():
    j=0
    while j < grayImage[i].__len__():
        grayImage[i][j]=255-grayImage[i][j]
        j=j+1
    i=i+1

cv2.imwrite(imageNmae+'invert.jpg',grayImage)
