import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Canvas for drawing
canvas = np.zeros((720, 1280, 3), np.uint8)

# Default settings
draw_color = (0, 0, 255)  # red
brush_thickness = 10
eraser_thickness = 50
xp, yp = 0, 0  # previous points

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)  # mirror view

    hands, frame = detector.findHands(frame, flipType=False)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)

        x, y = lmList[8][0], lmList[8][1]  # index finger tip

        # *** MODE 1: SELECTION MODE (2 fingers up) ***
        if fingers[1] and fingers[2]:   # faster and more stable

            xp, yp = 0, 0  # reset to stop drawing

            # RED
            if 0 < x < 200 and y < 150:
                draw_color = (0, 0, 255)

# GREEN
            elif 210 < x < 410 and y < 150:
                draw_color = (0, 255, 0)

# BLUE
            elif 420 < x < 620 and y < 150:
                draw_color = (255, 0, 0)

# ERASER
            elif 630 < x < 830 and y < 150:
                draw_color = (0, 0, 0)

            cv2.rectangle(frame, (x - 25, y - 25),
                          (x + 25, y + 25), draw_color, cv2.FILLED)

        # *** MODE 2: DRAWING MODE (1 finger up) ***
        elif fingers[1] == 1 and fingers[2] == 0:
            if xp == 0 and yp == 0:
                xp, yp = x, y

            if draw_color == (0, 0, 0):   # eraser
                cv2.line(frame, (xp, yp), (x, y), (0, 0, 0), eraser_thickness)
                cv2.line(canvas, (xp, yp), (x, y), (0, 0, 0), eraser_thickness)
            else:
                cv2.line(frame, (xp, yp), (x, y), draw_color, brush_thickness)
                cv2.line(canvas, (xp, yp), (x, y), draw_color, brush_thickness)

            xp, yp = x, y

    # Merge drawing + camera
    gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray_canvas, 50, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, inv)
    frame = cv2.bitwise_or(frame, canvas)

    # Draw top color selection bar
    cv2.rectangle(frame, (0, 0), (200, 150), (0, 0, 255), cv2.FILLED)
    cv2.putText(frame, "RED", (140, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.rectangle(frame, (210, 0), (410, 150), (0, 255, 0), cv2.FILLED)
    cv2.putText(frame, "GREEN", (330, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.rectangle(frame, (420, 0), (620, 150), (255, 0, 0), cv2.FILLED)
    cv2.putText(frame, "BLUE", (540, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.rectangle(frame, (630, 0), (830, 150), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, "ERASER", (720, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Air Drawing / Virtual Painter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
