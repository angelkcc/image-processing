import cv2
import numpy as np
img=cv2.imread("./images/xray.jpg")
print(img.shape)
img_negative=255-img
cv2.imshow("window",img_negative)
cv2.waitKey(0)