import cv2 as cv
import numpy as np

blank =np.zeros((500,500,3),dtype='uint8')

#paint the image a certain colour
blank[:] =0,255,0


# painting a specific area of ​​the image
blank[200:300 ,300:400]= 0,0,255

#Draw a regtangle
cv.rectangle(blank,(0,0),(200,200),(20,10,80),thickness=cv.FILLED)#thickness=-1 

#Draw a circle 
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(140,130,125),thickness=4)
# Draw a line 
cv.line(blank,(0,500),(200,200),(210,100,200),thickness=3)

# Write the text on image 
cv.putText(blank,'Hello my name is Zehra', (0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(230,120,190),2)


cv.imshow('Blank',blank)




cv.waitKey(0)

