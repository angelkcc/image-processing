#image thresholding//background is preserved//intensity slicing
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("./images/building.jpg")
A,B=100,200
without_background=np.zeros_like(img)

mask = (img >= A) & (img <= B)
without_background[mask] = 255
#display results
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img,cmap='gray')

plt.subplot(1,2,2)
plt.title("background removed image (AngelKhatri-04)")
plt.imshow(without_background,cmap='gray')
plt.show()