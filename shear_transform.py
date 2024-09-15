import cv2
import numpy as np
#new line
img = cv2.imread("C:\\Users\\Admin\\football.jpg")
rows, cols, _ = img.shape

# Define the shear matrix
shear_matrix = np.float32([[1, 0.5, 0],  # Shear along the x-axis
                           [0.5, 1, 0]])  # Shear along the y-axis

# Apply the shear transformation
sheared_img = cv2.warpAffine(img, shear_matrix, (cols, rows), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

img2=np.hstack((img,sheared_img))

cv2.imshow("shear transformation", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
