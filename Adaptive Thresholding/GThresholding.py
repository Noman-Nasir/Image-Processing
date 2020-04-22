
import cv2
import numpy as np

imageName = 'blue'
extension = '.jpg'

image = cv2.imread(imageName+extension,0)

mean = np.mean(image)

threshold = mean
meanG1 = 0
meanG2 = 0

i = 0
previousThreshold = 0

while previousThreshold!=threshold :
    
    print('Threshold is ',threshold)
    bool_idx = (image > threshold)
    meanG1 = np.mean(image[bool_idx])
    bool_idx = (image < threshold)
    meanG2 = np.mean(image[bool_idx])
    previousThreshold = threshold
    threshold = (meanG1+meanG2)/2
    
    i=i+1
    


bool_idx = (image < threshold)
image[bool_idx] = 0
bool_idx = (image >= threshold)
image[bool_idx] = 255

# cv2.imwrite(imageName+'GT'+extension,image)

cv2.imshow('a',image)
cv2.waitKey()







