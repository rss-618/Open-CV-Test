import cv2

print("Package Imported")

# Load the cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#  Grab Image
img = cv2.imread("Resources/test.jpg")  # make (0) if want to use webcam
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
# need to play around with last two arguments depending on image for accuracy
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
# Display the output
cv2.imshow('img', img)

k = cv2.waitKey()
""" 
img = cv2.VideoCapture("Resources/test.jpg")  # Keep empty if want to use webcam
while True:
    # gets each frame from video
    img = cap.read()
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    # need to play around with last two arguments depending on image for accuracy
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Display the output
    cv2.imshow('img', img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
"""
