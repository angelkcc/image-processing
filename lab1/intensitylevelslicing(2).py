#background preserve
import numpy as np
import cv2
import matplotlib.pyplot as plt
img =cv2.imread('images/building.jpg')
A,B=100,200
with_background=img.copy()
with_background[(img>=A) & (img<=B)] = 255

#display results
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img,cmap='gray')

plt.subplot(1,2,2)
plt.title("Background preserved image (AngelKhatri-04)")
plt.imshow(with_background,cmap='gray')
plt.show()