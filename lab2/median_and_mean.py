import cv2
import numpy as np

img=cv2.imread("./images/saltandpepper.jpg")
#median filter
median=cv2.medianBlur(img,5)
#mean filter
img1=cv2.imread("./images/lena.jpg")
mean=cv2.blur(img1,(5,5))

#display result
cv2.imshow("Median Filter(AngelKhatri-04)", np.hstack((img, median)))
cv2.imshow("Mean Filter(AngelKhatri-04)", np.hstack((img1, mean)))
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
