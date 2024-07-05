import cv2
import numpy as up

path = 'new_image.jpg'
image = cv2.imread(path)
print(image.shape)
print(image.shape[0])

cv2.circle(image, (image.shape[1] //2 , image.shape[0]//2), 50, (0,0,0), -1)


cv2.imshow("Cat", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
