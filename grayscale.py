import cv2
image = cv2.imread("photo.jpg")#to read an image
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('original',image)
cv2.imshow('Gray',grayImage)
cv2.imwrite('graynew.jpg',image)
print(image.size)
print(image.shape)
