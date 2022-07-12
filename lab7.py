import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi

x = io.imread('C:/Users/HP/Desktop/Image Processing/images2-21Mar/immagini2/mammografia.jpg')
plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')

#negative
y = 255 - x
plt.figure(2)
plt.imshow(y, clim=[0,255], cmap='gray')