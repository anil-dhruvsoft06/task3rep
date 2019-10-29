
import numpy as np
import cv2 as cv
img = cv.imread('Googleimage.png')
#img = cv.imread('Solarsystem.png')
print(img.shape)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(img,(17,17),0)
#ret, thresh = cv.threshold(blur, 127, 255, 0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
#th2 = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_MEAN_C,\
 #        cv.THRESH_BINARY_INV,11,1)
#contours, hierarchy = cv.FindContours_Impl(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
(contours,hierachy)=cv.findContours(th3,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blur, contours, -1, (0,255,0), 3)
#mask = np.zeros(imgray.shape,np.uint8)
#cv.drawContours(mask,[cnt],0,255,-1)
#pixelpoints = np.transpose(np.nonzero(mask))
#cnt = contours[4]
#cv.drawContours(img, [cnt], 0, (0,255,0), 3)
#cv.drawContours(img, contours, 3, (0,255,0), 3)
c=0
for cnt in contours:

    #area=cv.contourArea(cnt) #contour area
    perimeter = cv.arcLength(cnt,True)

    if (perimeter>150):
        cv.drawContours(img,[cnt],0,(0,255,0),2)
        cv.imshow('RGB',img)
        cv.waitKey(1000)
        print(len(cnt))
        c=c+1



(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(img,center,radius,(0,255,0),2)


print("Number of objects in the  Solarsystem:"+ str(c))





cv.imshow("Image",blur)

cv.waitKey(0)
cv.destroyAllWindows