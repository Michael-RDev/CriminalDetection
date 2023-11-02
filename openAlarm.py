import cv2

def open_alarm_when_detected(img_thing, name: str, crime: str, criminal_detected: bool, criminal_img:str):
        if criminal_detected:
            img = cv2.imread(img_thing)
            img = cv2.resize(img, (500, 500))
            x, y, _ = img.shape
            txtpoints = [x // 5, y - 100]
            font_size = min(x, y) / 600
            font_thick = int(3 * font_size)
            criminal = cv2.imread(criminal_img)
            criminal = cv2.resize(criminal, (500, 500))
            cv2.putText(img, f"{name}, {crime}", (txtpoints[0], txtpoints[1]), cv2.FONT_HERSHEY_SIMPLEX, font_size, (0, 0, 0), font_thick)
            cv2.moveWindow("Alarm criminal", 500, 200)
            cv2.imshow("Alarm criminal", img)
            cv2.moveWindow("criminal photo", 700, 100)
            cv2.imshow("criminal photo", criminal)
            if cv2.waitKey(1) == ord('e'):
                print("Destroy Videos")
                cv2.destroyWindow("Alarm criminal")
                cv2.destroyWindow("criminal photo")
        else:
             cv2.destroyAllWindows()


#open_alarm_when_detected("imgs/Alarm.jpg", "test", "crime", True, "imgs/criminal.jpg")

def open_criminal_file(filename:str):
    pass