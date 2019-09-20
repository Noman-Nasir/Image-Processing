

import cv2
import copy 
from matplotlib import pyplot as plt

imageNmae = 'class'
grayImage = cv2.imread(imageNmae+'.png',0)
#grayImage = cv2.cvtColor(grayImage, cv2.COLOR_BGR2GRAY)


orgImage = copy.copy(grayImage)

bit = 2

while bit<10:
    
    grayImage=copy.copy(orgImage)
    imgpos = 0

    i = 0
    while i < grayImage.__len__():
        j=0
        while j < grayImage[i].__len__():
            bitVal=format(grayImage[i][j], '#010b')
            if(bitVal[bit] == '1'):
                grayImage[i][j]=255
            else:
                grayImage[i][j]=0
            j=j+1
        i=i+1

    cv2.imwrite(imageNmae+str(bit-2)+'bitSlice.jpg',grayImage)
    plt.subplot(2,2,imgpos+1),plt.imshow(grayImage,'gray')
    plt.title("image"+str(bit-2))
    plt.xticks([]),plt.yticks([])
    imgpos=imgpos+1
    bit=bit+1
    plt.show()