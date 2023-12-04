from detectCriminal import faceRecoCam
from loadFunctions import names, known_face_encodings, crimes
import cv2

if __name__ == '__main__':
    alarm_img = "imgs/Alarm.jpg"
    cam_values = [1, 0]
    for cam_idx in cam_values:
        cam = cv2.VideoCapture(cam_idx)
        if cam.isOpened():
            break
        else:
            faceRecoCam(cam, known_face_encodings, names, crimes)

    