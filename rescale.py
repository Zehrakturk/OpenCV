import cv2 as cv

img=cv.imread('Images/cat_large.jpg')
cv.imshow('cat_large.jpg', img)

def rescaleFrame(frame,scale=0.75):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    
    dimensions= (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img,scale=0.2)
cv.imshow('cat_resized', resized_image)

capture= cv.VideoCapture('Videos/dog.mp4')


# Only live videos 
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)


while True:
    isTrue, frame  = capture.read()
    frame_resized = rescaleFrame(frame,scale=0.2)
    cv.imshow('Videos/dog.mp4',frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord ('z'):
        break
    
capture.release()
cv.waitKey(0)
    