import cv2 as cv
import numpy as np

img = cv.imread('Images/cats.jpg')
cv.imshow('Img',img)

blank = np.zeros(img.shape[:2], dtype= 'uint8')
cv.imshow('Blank',blank)

circle_small= cv.circle(blank.copy(),(img.shape[1]//2+26,img.shape[0]//2-4),50,255,-1)
circle_big=cv.circle(blank, (img.shape[1]//2+26,img.shape[0]//2-10),100,255,-1)
mask=cv.bitwise_and(circle_small,circle_big)

cv.imshow('circle_small',circle_small)
cv.imshow('circle_big',circle_big)
cv.imshow('Mask',mask)

masked= cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masked)

cv.waitKey(0)