import cv2
import time
import Hand_mesh_module as hmm
import cvzone
from cvzone.SerialModule import SerialObject
import numpy as np

arduino = SerialObject("COM4", digits=3)
wCam = 640
hCam = 480
sent_list = [0,0, 0,0]
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
ptime = 0
detector = hmm.HandDetection(min_detection_confidence=0.7)
myClassifier = cvzone.Classifier("./keras_model.h5", "./labels.txt")
access = False
while True:
    success, img = cap.read()
    detector.detector(img, True)
    length = detector.get_distance(img)
    predictions, index = myClassifier.getPrediction(img)
    print(predictions)
    if not access:
        if predictions[1]>0.75:
            access = True
            sent_list[0] = 1
            arduino.sendData(sent_list)

        else:
            sent_list[0] = 0
            arduino.sendData(sent_list)
    if predictions[0]>0.85:
        access = False
    if length and access==True:

        ard_len = np.interp(length, [30, 150], [0, 255])
        brightness = np.interp(ard_len, [0,255], [0,100])
        sent_list[3] = int(brightness)
        if ard_len == 0:
            sent_list[1] = 0
        elif ard_len == 255:
            sent_list[1] = 255
        else:
            sent_list[1] = 0
        sent_list[2] = int(ard_len)
        arduino.sendData(sent_list)
        print(sent_list)



    cv2.imshow("Image", img)
    cv2.waitKey(1)