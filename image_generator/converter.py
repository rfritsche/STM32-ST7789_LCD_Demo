#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 08:58:30 2021

@author: terminator
"""
import matplotlib.pyplot as plt
import numpy as np

filename="Untitled.bmp"

a=plt.imread(filename) #RGB 888
b=(a/np.r_[2**3, 2**2, 2**3]).round(0).astype(int)
b=b.clip(np.r_[0,0,0], np.r_[2**5-1, 2**6-1, 2**5-1])

rows=[]

for row in b:
    pixels=[]
    for pix in row:
        pix_16=f'{pix[0]:05b}{pix[1]:06b}{pix[2]:05b}'
        pix_16=pix_16[8:]+pix_16[:8]    #swap bytes
        pixels.append(f'0x{int(pix_16, base=2):04X}')   # ... turning all 16 bits
    rows.append('{'+','.join(pixels)+'}')
as_text=',\n'.join(rows)

with open(filename+'.txt', 'w') as file:
    file.writelines(as_text)
    
plt.imshow(b)