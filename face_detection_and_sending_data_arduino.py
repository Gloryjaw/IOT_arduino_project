from cvzone.SerialModule import SerialObject
import cv2
from cvzone.FaceDetectionModule import FaceDetector

cp = cv2.VideoCapture(0)
arduino = SerialObject("COM3")
detector = FaceDetector()

while True:
    success, img = cp.read()
    img, bbx = detector.findFaces(img)
    cv2.imshow("Image", img)
    if bbx:
        arduino.sendData([1])
    else:
        arduino.sendData([0])
    cv2.waitKey(1)
