import cv2
import numpy as np

img=cv2.imread("C:\\Users\\Admin\\B21AI002_CVIP_C_FOLDER\\football.jpg")
rows,cols, a = img.shape

pt1=np.float32([[150,100],[160,150],[30,60]])

pt2=np.float32([[50,100],[130,150],[90,160]])

M=cv2.getAffineTransform(pt1, pt2)

dst=cv2.warpAffine(img,M,(cols,rows))
img2=np.hstack((img,dst))
cv2.imshow("affine transformation",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()