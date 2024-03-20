import cv2
import mediapipe as mp
import numpy as np
mp_drawing =mp.solutions.drawing_utils
mp_pose =mp.solutions.pose

cap =cv2.VideoCapture('dance.mp4')

with mp_pose.Pose(min_setection_confidence=0.5, min_tracking_confidence=0.5)as pose:
    while cap.isOpened():
        ret, image=cap.read()
        if ret:
            image_pose=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results=pose.process(image_pose)
            mp_drawing.draw_landmarks(

                
            )
            cv2.imshow("Image",image)
            if cv2.waitKey(1)==ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()