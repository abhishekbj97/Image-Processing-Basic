# granelli histogram visualization

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi

x = io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/granelli.jpg')
plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')

#histogram plotting
n, b = np.histogram(x, np.arange(257))
plt.figure(2)
plt.bar(np.arange(256),n)

#full scale histogram streching for above figure
x = np.float32(x)

xmin = np.min(x)
xmax = np.max(x)
print(xmin)
print(xmax)

k =256
y = (k-1)*(x-xmin)/(xmax-xmin)

plt.figure(3)
plt.imshow(y, cmap='gray')