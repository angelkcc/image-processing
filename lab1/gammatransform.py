import cv2
import numpy as np
import matplotlib.pyplot as plt

#load the image in grayscale 
image=cv2.imread('./images/rabbit.jpg') #since the image is already in grayscale, we can read it without putting 0 as the second argument

#normalize the pixel values to the range [0,1] 
normalized_image=image/255.0 #divided by 255 to sclae the pixel values to [0,1]
#set the gamma value
gamma=2.2 #>1 for darkening and <1 for brigtnening

#apply power-law (gamma) transformation
gamma_corrected_image=np.power(normalized_image, gamma)

#rescale back to [0,255] and convert to 8bit unsigned integer
gamma_corrected_image=np.uint8(gamma_corrected_image*255)

#display the results
plt.imshow(image)
plt.show() #this displays the original image

#display both images side by side for comparison
plt.imshow(gamma_corrected_image)
plt.show() #this displays the gamma corrected image



