import matplotlib.pyplot as plt
import numpy as np
import skimage.io as io
import scipy.ndimage as ndi

x = io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/granelli.jpg')
plt.figure(1)
plt.imshow(x)

#color changing from color to gray scale by using clim=[0,255] and cmap='gray'

y = io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/granelli.jpg')
plt.figure(2)
plt.imshow(y, clim=[0,255], cmap='gray')