import cv2
vs = cv2.VideoCapture(0)#initializing the camera 0 for primary cam 1 means next cam
while True:
    _,img = vs.read()
    cv2.imshow("Videostream", img)
    key = cv2.waitKey(1)
    print(key)
    if key == ord("q"):
                  break
vs.release()
cv2.destroyAllWindows()
