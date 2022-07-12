import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndimage


x = np.float32(io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/cam.jpg'))
plt.figure(1)
plt.imshow(x, cmap='gray')


M = x.shape[0]
N = x.shape[1]

A = np.array([[1,0,N/2], [0,1,M/2],[0,0,1]], dtype=np.float32)

from skimage.transform import warp

y = warp(x, A, order=1)
plt.figure(2)
plt.imshow(y,cmap='gray')