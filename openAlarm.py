import cv2
from loadFunctions import names, crimes, images
import time
import numpy as np


def open_mug_shot(names_mug: list, crimes_mug: list, images_mug: list, name: str, crime: str, counter:int):
    criminal_names = [name for name in names_mug]
    criminal_crimes = [crime for crime in crimes_mug]
    criminal_imgs = [image for image in images_mug]
    if name in criminal_names and crime in criminal_crimes:
        if counter < 10:
            random_index = np.random.randint(0, len(criminal_imgs))
            random_img = cv2.imread(criminal_imgs[random_index])
            return random_img
        elif counter > 10:
            mug_shot_img = cv2.imread(criminal_imgs[criminal_names.index(name)])
            return mug_shot_img
    return None
        

def open_alarm_when_detected(img_thing, notification_image, name: str, crime: str, criminal_detected: bool, criminal_img: str, counter):
    if criminal_detected:

        for i in images:
            if str("data/" + name + "_" + crime) in i:
                target_image = i
                if target_image.endswith(".png"):
                    img = cv2.imread(notification_image)
                else:
                    img = cv2.imread(img_thing)
                
        img = cv2.resize(img, (500, 500))
        x, y, _ = img.shape
        txtpoints = [x // 5, y - 100]
        font_size = min(x, y) / 600
        font_thick = int(3 * font_size)
        criminal = cv2.imread(criminal_img)
        criminal = cv2.resize(criminal, (500, 500))
        mug_shot = open_mug_shot(names, crimes, images, name, crime, counter)
        if mug_shot is not None:
            mug_shot = cv2.resize(mug_shot, (1000, 500))
            combined_img = cv2.hconcat([img, criminal])
            combined_img = cv2.vconcat([combined_img, mug_shot])
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
    else:
        cv2.destroyAllWindows()
