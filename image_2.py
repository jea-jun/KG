import cv2
import numpy as np
path1 = 'Alien.jpg'
path2 = 'cave painting.jpg'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
#print(img1.shape)
#print(img2.shape)
img1 = cv2.resize(img1, (img2.shape[1],img2.shape[0]))
print(img1.shape)
roi = img1[100:300,200:300,:]
roi[:,:,:]
img3 = cv2.add(img1, img2)

mask = np.ones((img2.shape[0], img2.shape[1],3), dtype='uint8')*50
img1_b = cv2.add(img1, mask)
img2_b = cv2.add(img2, mask)

#cv2.imshow("Alien", img1)
#cv2.imshow("Alien mask",img1_b)
#cv2.imshow("Alien + cave",img3)
#cv2.imshow("cave mask",img2_b)
cv2.imshow("+roi",roi)

cv2.waitKey()
cv2.destroyAllWindows()