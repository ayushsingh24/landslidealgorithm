import cv2
from array import *

img = cv2.imread('slope.png',1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

colors = []

c_px = array('i', [0,0,0])
for i in range(519):
    for j in range(523):

        px = hsv[i,j]

        if (px[0] != c_px[0] and px[1] != c_px[1] and px[2] != c_px[2]):
        
            value = [px[0],px[1],px[2],i]
            colors.append(value)
            c_px = value

print(colors)

print(hsv.shape)