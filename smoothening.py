#resize the image
import cv2
#import imutils
img = cv2.imread('photo.jpg')
gaussianImg = cv2.GaussianBlur(img, (41,41),50)
gaussianImg1 = cv2.GaussianBlur(img, (21,21),0)#smoothenning
cv2.imshow('originalImage.jpg',img)
cv2.imshow('gaussian.jpg',gaussianImg)
cv2.imwrite('gaussianImg1.jpg',gaussianImg1)
