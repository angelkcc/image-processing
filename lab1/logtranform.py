import cv2
import numpy as np
img=cv2.imread("./images/lena.jpg")
print(img.shape)
c=255/(np.log(1+np.max(img)))
log_image=c*(np.log(1+img))
log_image=np.array(log_image,dtype=np.uint8)
cv2.imshow("window (AngelK)",log_image)
cv2.waitKey(0)
