import cv2
from loadFunctions import names, crimes, images
import numpy as np



def open_mug_shot(names_mug: list, crimes_mug: list, images_mug: list, name: str, crime: str, counter:int):
    macker = cv2.imread("imgs/hackercat.jpg")
    macker = cv2.resize(macker, (500, 500))
    if name in names_mug and crime in crimes_mug:
        if counter < 10 :
            #and name not in old_names
            random_index = np.random.randint(0, len(images_mug))
            random_img = cv2.imread(images_mug[random_index])
            cv2.moveWindow("--Scanning Database--", 0, 300)
            cv2.imshow("--Scanning Database--", macker)
            return random_img
        elif counter == 10:
            cv2.destroyWindow("--Scanning Database--")
            mug_shot_img = cv2.imread(images_mug[names_mug.index(name)])
            mug_shot_img = cv2.resize(mug_shot_img, (500, 500))
            cv2.imshow("Mug Shot Found", mug_shot_img)
            return mug_shot_img
        

def open_alarm_when_detected(img_thing, notification_image, name: str, crime: str, criminal_detected: bool, criminal_img: str, counter):
    img = None
    mug_shot = open_mug_shot(names, crimes, images, name, crime, counter)
    if criminal_detected:
        for target_image in images:
            if str("data/" + name + "_" + crime) in target_image:
                if target_image.endswith(".png"):
                    img = cv2.imread(notification_image)
                else:
                    img = cv2.imread(img_thing)
        if img is not None:
            img = cv2.resize(img, (500, 500))
            x, y, _ = img.shape
            txtpoints = [x // 5, y - 100]
            font_size = min(x, y) / 600
            font_thick = int(3 * font_size)
            criminal = cv2.imread(criminal_img)
            criminal = cv2.resize(criminal, (500, 500))
            if mug_shot is not None:
                combined_img = cv2.hconcat([img, criminal])
                cv2.putText(combined_img, f"Name: {name}, Crime: {crime}", (txtpoints[0], txtpoints[1]), cv2.FONT_HERSHEY_SIMPLEX, font_size, (0, 0, 0), font_thick)
                cv2.moveWindow("Alarm criminal", 500, 200)
                cv2.imshow("Alarm criminal", combined_img)
            else: 
                combined_img = cv2.hconcat([img, criminal])
                cv2.putText(combined_img, f"Name: {name}, Crime: {crime}", (txtpoints[0], txtpoints[1]), cv2.FONT_HERSHEY_SIMPLEX, font_size, (0, 0, 0), font_thick)
                cv2.moveWindow("Alarm criminal", 500, 200)
                cv2.imshow("Alarm criminal", combined_img)

            if cv2.waitKey(1) == ord('q'):
                cv2.destroyWindow("Alarm criminal")
                criminal_detected = False
                exit()
    else:
        cv2.destroyAllWindows()

