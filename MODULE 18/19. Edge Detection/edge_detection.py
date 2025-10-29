# Canny Edge Detection
# Noise Reduction
# Intensity of the gradient of the image
# Non-maximum supperssion
# Thresholding

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Abhishek Thakur\OneDrive\Documents\GitHub\Tute-Dude-advaced-python-course\MODULE 18\images\bird_image.jpg")

resize = cv2.resize(img,(500, 450))

min_thresh = 100
max_thresh = 200
edges = cv2.Canny(resize, min_thresh, max_thresh)
cv2.imshow("Original Image", resize)
cv2.imshow("Edge Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()