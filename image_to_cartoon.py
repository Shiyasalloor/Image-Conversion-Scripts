import cv2
import numpy as np

image = cv2.imread("dog.png")
gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray_img = cv2.medianBlur(gray_img,3)

edges = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,13,11)
color = cv2.bilateralFilter(image,9,250,250)

cartoon_image = cv2.bitwise_and(color,color,mask=edges)

cv2.imshow("Original Image",image)
cv2.imshow("Cartooned Image",cartoon_image)

cv2.waitKey(0)
cv2.destroyAllWindows()