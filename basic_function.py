import cv2 as cv

img= cv.imread('Images/boston.jpg')
resized =cv.resize(img,None, fx=0.5, fy=0.5)

# Converting to grayscale
gray= cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

# Blur
blur=cv.GaussianBlur(resized,(9,9),cv.BORDER_DEFAULT)

# Edge Cascade 
canny=cv.Canny(blur ,125,175)

# Dilating the image
dilated = cv.dilate(canny,(7,7), iterations=3)

# Eroding
eroded = cv.erode(dilated,(3,3),iterations=3 )

# Cropping 
cropped = img[50:400, 300:400]


cv.imshow('cropped',cropped)
# cv.imshow('eroded',eroded)
# cv.imshow("Dilated",dilated)
# cv.imshow('Canny', canny)
#cv.imshow('Gray',gray)
#cv.imshow('Original',img)
#cv.imshow('Blur',blur)

cv.waitKey(0)

cv.destroyAllWindows()
