import cv2
import numpy as np

def callBack1(value):
    pass
def callBack2(value):
    pass

img_path = 'Alien.jpg'
img = cv2.imread(img_path)
img = cv2.resize(img, (400, 400))

cv2.namedWindow("Style")
cv2.createTrackbar("sigma_s","Style" ,0, 200, callBack1)
cv2.createTrackbar("sigma_r", "Style", 0, 100, callBack2)


while True:
    sigma_s = cv2.getTrackbarPos("sigma_s", "Style")
    sigma_r = cv2.getTrackbarPos("sigma_r","Style")/100
    img_style = cv2.stylization(img, sigma_s=sigma_s,sigma_r=sigma_r)

    cv2.imshow('image',img)
    cv2.imshow("Style", img_style)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()