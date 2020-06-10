import cv2
import numpy as np

print("OpenCV Imported")
cap = cv2.VideoCapture("Resources/test.mp4")  # Keep empty to use webcam
print("Video Assigned")
ret, frame1 = cap.read()  # Frame 1
ret, frame2 = cap.read()  # Frame 2

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #  Get Rid of noise (if you want all the noise comment out for loop and uncomment .drawContours)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (20, 30), cv2.FONT_ITALIC,
                    .9
                    , (0, 0, 255), 3)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv2.imshow("motion detection", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(30) == 27:  # Exit is escape button
        break
cv2.destroyAllWindows()
cap.release()
exit()
