import cv2
#hi
#hello
img=cv2.imread("C:\\Users\\Admin\\football.jpg",cv2.IMREAD_GRAYSCALE)
binary=cv2.threshold(img,140,255, cv2.THRESH_BINARY)[1]

cv2.imwrite("C:\\Users\\Admin\\binary.jpg",binary)

img2=cv2.imread("C:\\Users\\Admin\\football.jpg")
cv2.imshow("Image2",img2)
#real, binary1=cv2.threshold(img2,128,255, cv2.THRESH_BINARY)
#cv2.imshow("binImage",binary1)

cv2.imshow("Image",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
