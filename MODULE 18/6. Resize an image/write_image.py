import cv2

import cv2
path = r"C:\Users\Abhishek Thakur\OneDrive\Documents\GitHub\Tute-Dude-advaced-python-course\MODULE 18\images\example_image.jpg"
img = cv2.imread(path)


width = 400
height = 300
dim = (width, height)
resized = cv2.resize(img, dim)
cv2.imshow("Orignial Image", img)
print("Dimensions of the Original image: ", img.shape)
print("Dimensions of the resized image: ", resized.shape)
# cv2.imwrite('nature_gray.jpg', img)
cv2.imshow("nature image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
