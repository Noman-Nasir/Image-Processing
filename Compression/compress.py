

import cv2
import copy
import numpy as np 
from matplotlib import pyplot as plt

imageNmae = 'blue'
grayImage = cv2.imread(imageNmae+'.jpg',0)
#grayImage = cv2.cvtColor(grayImage, cv2.COLOR_BGR2GRAY)

binaries = [0b00000001,0b00000010,0b00000100,0b00001000,0b00010000,
            0b00100000,0b01000000,0b10000000]

print (binaries)

orgImage = copy.copy(grayImage)

bit = 7

compImage = np.zeros((grayImage.shape[0],grayImage.shape[1]))

while bit>=0:
    
    grayImage=copy.copy(orgImage)
    imgpos = 0
    grayImage=cv2.bitwise_and(grayImage,binaries[bit])
    cv2.imwrite(imageNmae+str(bit)+'bitSlice.jpg',grayImage)
    imgpos=imgpos+1
    if(bit>=4):
        compImage = compImage + grayImage
    bit=bit-1
    
cv2.imwrite(imageNmae+"comp"+'.jpg',compImage)