import cv2
import numpy as np
try:
    cap = cv2.VideoCapture(0)
    cap.set(4,1024)
    # detector=HandDetector(detectionCon=0.8,maxHands=1)

    while True:
        success , img=cap.read()
        image=cv2.flip(img,1)
        # Convert Image to Image HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Defining lower and upper bound HSV values
        lower = np.array([0, 100, 100])
        upper = np.array([90, 255, 255])

        # Defining mask for detecting color
        mask = cv2.inRange(hsv, lower, upper)

        # Display Image and Mask
        cv2.imshow("Image", image)
        cv2.imshow("Mask", mask)
        key = cv2.waitKey(1)
        if key== ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()