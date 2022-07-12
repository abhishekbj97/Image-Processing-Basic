import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndimage

x = io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/fragole.jpg')
plt.figure(1)
plt.imshow(x)

y = io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/dorian.jpg');
plt.figure(2)
plt.imshow(y)