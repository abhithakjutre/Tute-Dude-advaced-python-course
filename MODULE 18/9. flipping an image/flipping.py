import cv2

img = cv2.imread(r"C:\Users\Abhishek Thakur\OneDrive\Documents\GitHub\Tute-Dude-advaced-python-course\MODULE 18\images\example_image.jpg")
width = 400
height = 400
dim= (width, height)
resized = cv2.resize(img, dim) 
cv2.imshow("Original", resized)
print("Size in bytes: ", img.size)
# flip = cv2.flip(resized, 1)
# cv2.imshow("horizonal", flip)
# flip = cv2.flip(resized, 0)
# cv2.imshow("vertical", flip)
flip = cv2.flip(resized, -1)
cv2.imshow("Horizontal, vertical", flip)
cv2.waitKey(0)
cv2.destroyAllWindows()