import cv2
img = cv2.imread("photo.jpg")#to read an image
cv2.imshow('show', img)   #to display the image
cv2.imwrite('myphoto.jpg',img) #to save the image

cv2.waitKey(10000)
cv2.destroyAllWindows()
