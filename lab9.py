import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi

x = io.imread('C:/Users/HP/Desktop/Image Processing/images2-21Mar/immagini2/marte.jpg')
plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')

x = np.float32(x)

#gamma value

y = x**0.3
plt.figure(2)
plt.imshow(y, cmap='gray')


#equalization

import skimage.exposure as exposure
z = exposure.equalize_hist(x)
plt.figure(3)
plt.imshow(z, cmap='gray')