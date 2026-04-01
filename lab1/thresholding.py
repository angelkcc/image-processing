#image thresholding//backgroun is not preserved
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("./images/catglasses.jpg")
t,thresholdimage=cv2.threshold(img,110,255,cv2.THRESH_BINARY)
#display results
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img,cmap='gray')

plt.subplot(1,2,2)
plt.title("threshold image (AngelKhatri-04)")
plt.imshow(thresholdimage,cmap='gray')
plt.show()