import cv2
import numpy as np

def imageSize(image):
    print ('Size of Image is :')
    print ('Height :', len(image) )
    print ('Width :', len(image[0]))

def imageType(image):
    if(len(image.shape)==3):
        if(len(image[0][0])):
            if(len(image[0][0])==3):
                return 'RGB Image'
            if(len(image[0][0])==4):
                return 'RGBA Image'
    elif(len(image.shape)==2):
        return 'GrayScale Image'


imageNmae = 'red'
template = cv2.imread(imageNmae+'.jpg',1)

print (imageType(template))
imageSize(template)

template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


print ('\n'+imageType(template_gray))
imageSize(template_gray)

sideBySide = np.concatenate((template,cv2.cvtColor(template_gray, cv2.COLOR_GRAY2BGR)),axis=1)

cv2.imwrite("grayAndBGR"+'.jpg',sideBySide)


bool_idx = template_gray < np.mean(template_gray)
template_gray[bool_idx] = 0
bool_idx = template_gray >= np.mean(template_gray)
template_gray[bool_idx] = 255

cv2.imwrite("binary"+'.jpg',template_gray)

template_gray=template_gray[50:len(template_gray)-50,50:len(template_gray[0])-50]

cv2.imwrite("binary_cut"+'.jpg',template_gray)
