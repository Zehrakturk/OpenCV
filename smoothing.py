import cv2 as cv
import numpy as np

img = cv.imread('Images/cats.jpg')
#cv.imshow('Cats',img)

#average
average= cv.blur(img,(3,3))
cv.imshow('Average',average)

#gauss
gauss = cv.GaussianBlur(img, (3,3) ,0)
cv.imshow('Gauss',gauss)

#median
median=cv.medianBlur(img, 3)
cv.imshow('Median',median)

#bilateral
#if you have huge sigmaSpace and sigmaColor , you have much blur to image
bilateral = cv.bilateralFilter(img,30, 100, 100)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)