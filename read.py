import cv2 as cv

# ımage reading.......
# img= cv.imread('Images/cat_large.jpg')

# cv.imshow('Cat',img)

# Video reading.......

capture= cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF == ord ('z'):
        break
    
capture.release()
cv.waitKey(0)