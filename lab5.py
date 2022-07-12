import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

x = io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/colore/fragole.jpg')

plt.figure(1)
plt.imshow(x)

R = x[:,:,0]
plt.figure(2)
plt.imshow(R)

G = x[:,:,1]
plt.figure(3)
plt.imshow(G)

B = x[:,:,2]
plt.figure(4)
plt.imshow(B)

M = x.shape[0]
N = x.shape[1]

R = np.zeros((M,N), x.dtype)
y = np.stack((R,G,B),2)

plt.figure(5)
plt.imshow(y)

#------------------------------------------
# green set to zeros

M = x.shape[0]
N = x.shape[1]

G = np.zeros((M,N), x.dtype)
y = np.stack((R,G,B),-1)

plt.figure(6)
plt.imshow(y)

#-----------------------------------------
# blue set to zero

M = x.shape[0]
N = x.shape[1]

B = np.zeros((M,N), x.dtype)
y = np.stack((R,G,B),2)

plt.figure(7)
plt.imshow(y)
  


