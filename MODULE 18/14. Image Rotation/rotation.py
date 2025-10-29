import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Abhishek Thakur\OneDrive\Documents\GitHub\Tute-Dude-advaced-python-course\MODULE 18\images\example_image.jpg")

column = img.shape[0]
row = img.shape[1]

center = (column/ 2, row/2)
angle = 180

r = cv2.getRotationMatrix2D(center, angle, 1)

rotate = cv2.warpAffine(img, r, (column,row))

cv2.imshow("Original Image", img)
cv2.imshow("Rotation image", rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()