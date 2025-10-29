import cv2
video = cv2.VideoCapture(r"C:\Users\Abhishek Thakur\OneDrive\Documents\GitHub\Tute-Dude-advaced-python-course\MODULE 18\videos\example_video.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('output.mp4', fourcc, 25.0, (1280, 720))
while video.isOpened():
    ret,frame = video.read()

    if ret: 
        output.write(frame)
        cv2.imshow(r"\videos\output.mp4",  frame)
        if cv2.waitKey(10) == ord('s'): 
            break
    else:
        break

cv2.destroyAllWindows()