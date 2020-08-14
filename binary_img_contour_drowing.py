import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    frame = cv2.flip(frame, 1)
    org_img = frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, frame = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt_img = cv2.drawContours(org_img, contours, -1, (0, 255, 0), 3)

    cv2.imshow('video', cnt_img)
    

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()