import cv2 as cv
import numpy as np

img=cv.imread('Images/cats.jpg')

cv.imshow("cats",img)

blank= np.zeros(img.shape,dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT )
# cv.imshow('Blur',blur)

canny=cv.Canny(blur,125 ,175)
cv.imshow('Canny Edges',canny)
# ret,thresh = cv.threshold(gray,125, 255, cv.THRESH_BINARY)


contours, hierarchies= cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found!')

cv.drawContours(blank, contours,-1,(0,0,255),1)
cv.imshow('contours drawn ',blank)

cv.imshow('Gray',gray)
# cv.imshow('thresh',thresh)

cv.waitKey(0)