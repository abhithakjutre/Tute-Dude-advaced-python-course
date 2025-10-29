import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Abhishek Thakur\OneDrive\Documents\GitHub\Tute-Dude-advaced-python-course\MODULE 18\images\example_image.jpg")

column = img.shape[1]
row = img.shape[0]

s = np.float32([(1, 0, 150), (0,1,170)])

shifted = cv2.warpAffine(img, s, (column, row))

cv2.imshow("Image", img)

cv2.imshow("Shifting Image",shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()