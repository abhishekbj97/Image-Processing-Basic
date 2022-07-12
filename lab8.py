import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi

x = io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/vista_aerea.jpg')
plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')

#power tansformation of image

x = np.float32(x)

y = x**3
plt.figure(2)
plt.imshow(y, cmap='gray')