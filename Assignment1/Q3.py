import cv2
from matplotlib import pyplot as plt

imageNmae = 'blue'
extension = '.jpg'
grayImage = cv2.imread(imageNmae+extension,0)

image_hist = cv2.calcHist([grayImage],[0],None,[256],[0,256])

for idx,val in enumerate(image_hist):
    print (idx," : ",int(val))

plt.hist(grayImage.ravel(),256,[0,256])
plt.show()
