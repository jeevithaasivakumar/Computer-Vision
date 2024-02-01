#resize the image
import cv2
import imutils
img = cv2.imread('photo.jpg')
resizedImg = imutils.resize(img, width=100)
cv2.imshow('originalImage.jpg',img)
cv2.imshow('Resized.jpg',resizedImg)
cv2.imwrite('resizedImage.jpg',resizedImg)
