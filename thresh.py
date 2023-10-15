import cv2 as cv
import numpy as np

img = cv.imread('Images/cats.jpg')
cv.imshow('Img',img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT )
#cv.imshow('Gray',gray)

#Simple thresholding
threshold, thres = cv.threshold(gray, 140, 255, cv.THRESH_BINARY)
#cv.imshow('Simple threshold',thres)

threshold, thres_inv = cv.threshold(gray, 130, 255, cv.THRESH_BINARY_INV)
#cv.imshow('Simple threshold Inverse',thres_inv)

#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(blur, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv.THRESH_BINARY_INV,11 ,3)
cv.imshow('Adaptive Threshold',adaptive_thresh)

cv.waitKey(0)