#resize the image
import cv2
#import imutils
img = cv2.imread('photo.jpg')
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#bgr to gray
#gaussBlur = cv2.GaussianBlur(grayImg, (21,21),0)#smoothenning
thresholding = cv2.threshold(grayImg,180,255,cv2.THRESH_BINARY)[1]#color img to greay scale black 0 -- 180 --white 255
cv2.imshow('thresholding.jpg',thresholding)#src,threshold,maxvalue for threshold,binary,type
cv2.imwrite('thresholding.jpg',thresholding)
