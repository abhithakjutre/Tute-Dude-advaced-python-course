import cv2
img = cv2.imread(r"C:\Users\Abhishek Thakur\OneDrive\Documents\GitHub\Tute-Dude-advaced-python-course\MODULE 18\images\bird_image.jpg")

resize = cv2.resize(img,(600,  520))

d = 7 
sigmacolor  = 100
sigmaspace = 100
b = cv2.bilateralFilter(img,d,sigmacolor,sigmaspace )

cv2.imshow("input", resize)
cv2.imshow("Output",b)

cv2.waitKey(0)
cv2.destroyAllWindows()