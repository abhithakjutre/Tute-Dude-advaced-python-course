import cv2

import cv2

img = cv2.imread(r"C:\Users\Abhishek Thakur\OneDrive\Documents\GitHub\Tute-Dude-advaced-python-course\MODULE 18\images\example_image.jpg", 0)


cv2.imwrite(r'5. writing an image\nature_gray.jpg', img)
cv2.imshow("nature image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
