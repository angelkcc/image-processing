import cv2
import numpy as np
img=cv2.imread("./images/mamogram.png")
print(img.shape)
img_negative=255-img
cv2.imshow("window (AngelK)",img)
cv2.imshow("window (AngelKhatri-04)",img_negative)
cv2.waitKey(0)