import cv2
import mediapipe as mp
import time


class HandDetection:
    def __init__(self,static_image_mode=False, max_num_hands=2, model_complexity=1, min_detection_confidence=0.5, min_tracking_confidence=0.5):

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode, max_num_hands, model_complexity, min_detection_confidence, min_tracking_confidence)
        self.mpdraw = mp.solutions.drawing_utils

    def detector(self, img, show_image=False):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        if show_image:
            if self.result.multi_hand_landmarks:
                for landmarks in self.result.multi_hand_landmarks:
                    self.mpdraw.draw_landmarks(img, landmarks, self.mpHands.HAND_CONNECTIONS)

    def get_hand_positions(self,img, hand_no=0):
        pos_list = []
        if self.result.multi_hand_landmarks:
            hand_landmarks = self.result.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(hand_landmarks.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                pos_list.append([id, cx, cy])
                # cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
            return pos_list


def main():
    cp = cv2.VideoCapture(0)
    ctime = 0
    ptime = 0
    detection = HandDetection()
    while True:
        success, img = cp.read()
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        detection.detector(img, True)
        pos_list = detection.get_hand_positions(img)
        if pos_list:
            cv2.circle(img,(pos_list[4][1],pos_list[4][2]), 7, (0,255,0),cv2.FILLED)
            cv2.circle(img, (pos_list[8][1], pos_list[8][2]), 7, (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
