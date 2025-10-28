import cv2
import numpy as np


img = cv2.imread(r"C:\Users\Abhishek Thakur\OneDrive\Documents\GitHub\Tute-Dude-advaced-python-course\MODULE 18\images\example_image.jpg")
cv2.line(img, (0, 0), (150, 150), (255,0,0), 2)
cv2.rectangle(img,(200,150,), (250, 300), (0,255, 0), 3)
cv2.circle(img, (300, 75), 70, (255,0,255), 3)
cv2.waitKey(0)

cv2.destroyAllWindows()