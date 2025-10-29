import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Abhishek Thakur\OneDrive\Documents\GitHub\Tute-Dude-advaced-python-course\MODULE 18\images\example_image.jpg")

threshold_value = 100
_,binary_threshold = cv2.threshold(img,threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow("Orignial image", img)
cv2.imshow("Binary Threshold", binary_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()