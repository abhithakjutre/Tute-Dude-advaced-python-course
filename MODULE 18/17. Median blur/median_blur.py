import cv2
img = cv2.imread(r"C:\Users\Abhishek Thakur\OneDrive\Documents\GitHub\Tute-Dude-advaced-python-course\MODULE 18\images\example_image.jpg")

resize = cv2.resize(img, (400, 600))

kernel = 3

blur= cv2.medianBlur(resize,kernel)
cv2.imshow("Input", resize)

cv2.imshow("Output",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
