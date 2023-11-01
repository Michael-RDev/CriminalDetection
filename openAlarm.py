import cv2 
from threading import Thread

def open_alarm_when_detected(img_thing, name:str, crime:str, criminal_detected:bool):
    while True:
        if criminal_detected:
            img = cv2.imread(img_thing)
            img = cv2.resize(img, (500, 500))
            x, y, _ = img.shape
            txtpoints = [x // 5, y - 100]
            font_size = min(x, y) / 600
            font_thick = int(3 * font_size)
            cv2.putText(img, f"Name: {name}, Crime: {crime}", (txtpoints[0], txtpoints[1]), cv2.FONT_HERSHEY_SIMPLEX, font_size, (0, 0, 0), font_thick)
            cv2.moveWindow("Alarm criminal", 500, 200)
            cv2.imshow("Alarm criminal", img)
            if cv2.waitKey(1) == ord('q'):
                break

cam_thread = Thread(target=open_alarm_when_detected, args =("imgs/Alarm.jpg", "bob", "wee", True))

cam_thread.start()