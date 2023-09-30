import cv2
import numpy as np
import time
import Hand_mesh_module as hmm

wCam = 640
hCam = 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
ptime = 0
detector = hmm.HandDetection(min_detection_confidence=0.7)

while True:
    success, img = cap.read()
    detector.detector(img, True)
    pos_list = detector.get_hand_positions(img)

    print(pos_list)
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(img, f"FPS: {int(fps)}", (40, 70), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 255), 1)
    cv2.imshow("Image", img)
    cv2.waitKey(1)