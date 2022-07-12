import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndimage


x = np.float32(io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/cam.jpg'))
plt.figure(1)
plt.imshow(x, cmap='gray')

M = x.shape[0]
N = x.shape[1]

T = np.array([[np.cos(np.pi/4),np.sin(np.pi/4),0],
              [-np.sin(np.pi/4),np.cos(np.pi/4),0],
              [0,0,1]], dtype=np.float32)
A = T[[1,0,2],:][:,[1,0,2]].T

from skimage.transform import warp
y = warp(x,A, order=1)
plt.figure(2)
plt.imshow(y, cmap='gray')