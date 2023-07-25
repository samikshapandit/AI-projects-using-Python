import cv2
img = cv2.imread("sample.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresholdImg = cv2.threshold(grayImg, 200, 270, cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImg.jpg",thresholdImg)
