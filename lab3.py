import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi

#file not in specifies format as like jpg 
#it is color format
x = np.fromfile('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/lena.y', np.uint8)
x = np.reshape(x, (512,512))

plt.figure(1)
plt.imshow(x)

#to change color to gray scle image

plt.figure(2)
plt.imshow(x, clim=[0,255], cmap='gray')


#save and load of file in python format
np.save('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/lena.npy', x)
y = np.load('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/lena.npy')

plt.figure(3)
plt.imshow(y, clim=[0,255], cmap='gray')

#saving in jpeg format
z = np.uint8(x)
io.imsave('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/lena_save1.jpg', z, quality=100)

#save lena in raw format
np.uint8(z).tofile('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/lena.raw')

#loading color images
x = io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/colore/fragole.jpg')
plt.figure(4)
plt.imshow(x)