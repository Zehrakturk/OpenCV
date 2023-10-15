import cv2 as cv
import numpy as np

# img = cv.imread('Images/')
# cv.imshow('Img',img)

blank = np.zeros((400,400), dtype ='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200, 255,-1)

#BITWISE_AND
bitwise_and=cv.bitwise_and(rectangle,circle)

#BITWISE_OR 
bitwise_or=cv.bitwise_or(rectangle,circle)

#BITWISE_XOR
bitwise_xor=cv.bitwise_xor(rectangle,circle)

#BITWISE_NOT
bitwise_not=cv.bitwise_not(circle)

cv.imshow('Bitwise_AND',bitwise_and )
cv.imshow('Bitwise_OR',bitwise_or )
cv.imshow('Bitwise_XOR',bitwise_xor )
cv.imshow('Bitwise_NOT',bitwise_not )

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)



cv.waitKey(0)