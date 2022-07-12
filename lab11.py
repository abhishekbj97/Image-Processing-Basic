import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi

x = io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/dorian.jpg')
plt.figure(1)
plt.imshow(x,cmap='gray')

from skimage.transform import rescale

y = rescale(x, 3/2, order=0)
plt.figure(2)
plt.imshow(y,cmap='gray')

y = rescale(x, 3/2, order=1)
plt.figure(3)
plt.imshow(y, cmap='gray')

y = rescale(x, 3/2, order=3)
plt.figure(4)
plt.imshow(y, cmap='gray')