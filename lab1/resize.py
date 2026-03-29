import cv2
import numpy as np
img=cv2.imread("./images/cat.jpg")
print(img.shape)
img_resize=cv2.resize(img,(300,300))
print(img_resize.shape)
cv2.imshow("window",img_resize)
cv2.imwrite("./images/cat_resize.jpg",img_resize)
cv2.waitKey(0)