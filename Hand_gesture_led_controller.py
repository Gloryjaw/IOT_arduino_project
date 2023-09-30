import cv2
import time
import Hand_mesh_module as hmm
from cvzone.SerialModule import SerialObject
import numpy as np

arduino = SerialObject("COM3")
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
    length = detector.get_distance(img)
    if length:
        ard_len = np.interp(length, [20, 145], [0, 255])
        arduino.sendData([ard_len])
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, f"FPS: {int(fps)}", (40, 70), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 255), 1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)