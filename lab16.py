# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:52:28 2022

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndimage


x = np.float32(io.imread('C:/Users/HP/Desktop/Image Processing/images1-17Mar+24Mar/immagini1/bianco_nero/cam.jpg'))
plt.figure(1)
plt.imshow(x, cmap='gray')


M = x.shape[0]
N = x.shape[1]

A1 = np.array([[1,0,N/2], [0,1,M/2],[0,0,1]], dtype=np.float32)
A2 = np.array([[np.cos(np.pi/4),np.sin(np.pi/4),0],
              [-np.sin(np.pi/4),np.cos(np.pi/4),0],
              [0,0,1]], dtype=np.float32)
A3 = np.array([[1,0,-N/2], [0,1,-M/2],[0,0,1]], dtype=np.float32)

A =A1@A2@A3
from skimage.transform import warp

y = warp(x, A, order=1)
plt.figure(2)
plt.imshow(y,cmap='gray')