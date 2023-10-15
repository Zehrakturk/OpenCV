import cv2 as cv
import numpy as np

img = cv.imread('Images/boston.jpg')
img=cv.resize(img,(0,0), fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
cv.imshow('Boston', img)

blank=np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)
blue= cv.merge([b,blank,blank])
green =cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

merged= cv.merge([b,g,r])
cv.imshow('merged', merged)

cv.waitKey(0)

