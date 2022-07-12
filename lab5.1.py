import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

x = io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/dorian.jpg')
plt.figure(1)
plt.imshow(x, cmap='gray')

#global statistics
xm = np.mean(x)
xv = np.var(x)
xs = np.std(x)

#local statistics
y = ndi.generic_filter(x,np.mean,(3,3))
plt.figure(2)
plt.imshow(y, cmap='gray')

#histogram computation
n, b = np.histogram(x, np.arange(257))
plt.figure(3)
plt.bar(np.arange(256), n)