import cv2
import imutils
img = cv2.imread("sample.jpg")
resizedImg = imutils.resize(img, width=20)
cv2.imwrite("ResizedImg.jpg",resizedImg)
