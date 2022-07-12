import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndimage

x = np.float32(io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/cam.jpg'))
plt.figure(1)
plt.imshow(x, cmap='gray')

#warp of image
#for this we import warp

from skimage.transform import warp

M = x.shape[0]
N = x.shape[1]

#define afffine matrix
A = np.array([[2/3,0,0],[0,2/3,0],[0,0,1]], dtype=np.float32)
y = warp(x,A, output_shape=(int(3/2*M), int(3/2*N)), order=1)
plt.figure(2)
plt.imshow(y, cmap='gray')