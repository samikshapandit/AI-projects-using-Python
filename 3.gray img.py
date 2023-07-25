import cv2
img = cv2.imread("sam.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("GrayImg.jpg",img)
cv2.imshow("Original",img)
cv2.imshow("GrayImg",grayImg)
cv2.waitkey(0)
cv2.destroyAllWindows()
