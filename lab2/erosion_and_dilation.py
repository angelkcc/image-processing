import cv2
import numpy as np
img=cv2.imread("./images/fingerprint.png")
img1=cv2.imread("./images/fingerprint.png")

kernel=np.ones((5,5),np.uint8) #filter kernel
img_erosion=cv2.erode(img,kernel,iterations=1) #erosion

img_dilation=cv2.dilate(img1,kernel,iterations=1) #dilation

#open processing
img_erosion1=cv2.erode(img_dilation,kernel,iterations=1) #opening
#close processing
img_dilation1=cv2.dilate(img_erosion,kernel,iterations=1) #closing

cv2.imshow("Erosion(AngelKhatri-04)", np.hstack((img, img_erosion)))
cv2.imshow("Dilation(AngelKhatri-04)", np.hstack((img1, img_dilation)))
cv2.imshow("Opening(AngelKhatri-04)", np.hstack((img_erosion, img_erosion1)))
cv2.imshow("Closing(AngelKhatri-04)", np.hstack((img_dilation, img_dilation1)))
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

