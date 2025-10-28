import cv2

import cv2
path = r"C:\Users\Abhishek Thakur\OneDrive\Documents\GitHub\Tute-Dude-advaced-python-course\MODULE 18\images\example_image.jpg"
img = cv2.imread(path, 0)

print("Dimensions of the image: ", img.shape)

scale = 50


width = int(img.shape[1]*scale /100)
height = int(img.shape[0]*scale /100)

dim = (width, height)
resized = cv2.resize(img, dim)
print("Dimension of Resized image:", resized.shape)


# cv2.imwrite('nature_gray.jpg', img)
cv2.imshow("resized", resized)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
