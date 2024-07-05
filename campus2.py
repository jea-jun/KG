import numpy as np
import cv2

# 빈 이미지 생성
img1 = np.zeros((300, 300), dtype='uint8')
img = np.zeros((300, 300), dtype='uint8')

# 사각형 그리기
cv2.rectangle(img1, (25, 25), (275, 275), 225, 1)

# 원 그리기
cv2.circle(img, (150, 150), 150, 255, 1)

# 비트 연산
bitwisexor = cv2.bitwise_xor(img1, img)

while True:
    cv2.imshow("img1", img1)
    cv2.imshow("img2", bitwisexor)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
