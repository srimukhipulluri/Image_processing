import cv2
import numpy as np
#hello
img=cv2.imread("C:\\Users\\Admin\\football.jpg",cv2.IMREAD_GRAYSCALE)
bit_planes=[]
for i in range(8):
    plane=np.bitwise_and(img,2**i)
    bit_planes.append(plane)
for i in range(8):
    cv2.imshow(f'Bitplane{i}',bit_planes[i]*255)
    cv2.waitKey(500)
cv2.waitKey(100)
cv2.destroyAllWindows(0)