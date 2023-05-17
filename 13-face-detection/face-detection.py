# Install OpenCV
# pip install opencv_python

import cv2

# Add haarscade_frontalface_default.xml pre written file
face_cascade = cv2.CascadeClassifier('13-face-detection/haarcascade_frontalface_default.xml')

# Add an image you want to test
img = cv2.imread('13-face-detection/test.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y +h), (225, 0, 0), 2)

cv2.imshow('img' , img)

cv2.waitKey()

cv2.imwrite("face_detected.jpg")