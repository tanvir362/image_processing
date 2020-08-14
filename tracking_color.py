import cv2
import numpy as np



cap = cv2.VideoCapture(0)

yellow_lower = np.array([22, 93, 0])
yellow_upper = np.array([45, 255, 255])


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    # cv2.imshow('mask', mask)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cnt_img = cv2.drawContours(frame, contours, -1, (255, 0, 0), 3)
    # cv2.imshow('contours', cnt_img)


    for c in contours:
        area = cv2.contourArea(c)
        if area > 400:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # if y < prev_y:
            #     pyautogui.press('space')

            # prev_y = y
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()

# print(zeros)