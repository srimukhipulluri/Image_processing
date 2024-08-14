import cv2
import numpy as np

img=cv2.imread("C:\\Users\\Admin\\football.jpg",cv2.IMREAD_GRAYSCALE)
height,width=img.shape
sliced_img=np.zeros((height,width),dtype=np.uint8)
min_range=100
max_range=255
for i in range(height):
    for j in range(width):
        pixel_value=img[i,j]
        if min_range<=pixel_value<=max_range:
            sliced_img[i,j]=255
        else:
            sliced_img[i,j]=0
            
cv2.imshow('original image',img)
cv2.imshow('original image',sliced_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

