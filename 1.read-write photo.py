import cv2
img = cv2.imread("sam.jpg")
cv2.imshow("SamikshaPhoto",img)
cv2.imwrite("SamikshaPhoto.jpg",img)
print(img.shape)
print(img.size)
print(img.dtype)
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("GrayImg.jpg",img)
cv2.imshow("Original",img)
cv2.imshow("GrayImg",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
