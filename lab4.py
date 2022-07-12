import matplotlib.pyplot as plt
import numpy as np
import skimage.io as io
import scipy.ndimage as ndi

x = io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/colore/fragole.jpg')
plt.figure(1)
plt.imshow(x)

red = x[:,:,0]
plt.figure(2)
plt.imshow(red, clim=[0,255], cmap='gray')

green = x[:,:,1]
plt.figure(3)
plt.imshow(green, clim=[0,255], cmap='gray')

blue = x[:,:,2]
plt.figure(4)
plt.imshow(blue, clim=[0,255], cmap='gray')