import cv2 as cv
import numpy as np

img= cv.imread('Images/boston.jpg')

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated= translate(img,100,100)

# Rotation
def rotate(img ,angle, rotPoint=None):
    (height, width) =img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat= cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions= (width,height)
    
    return cv.warpAffine(img,rotMat,dimensions)
rotated= rotate(img,45)

#Flipping
flip= cv.flip(img,1)

# 0 --> vertical
# 1 --> horizontal
# -1 --> vertical,horizontal



cv.imshow('flip',flip)
cv.imshow('rotated',rotated)
cv.imshow('Boston', translated)
cv.waitKey(0)


