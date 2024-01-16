import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

try:
    while True:
        (success, img) = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    print(id, cx, cy)
                    if id == 4:  # finger 1
                        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        czas = time.localtime()[5]
        cv2.putText(img, f'in sec:{int(czas)}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 120, 50), 2)
        cv2.imshow("Test", img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
