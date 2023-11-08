import cv2
from loadFunctions import names, known_face_encodings, crimes, images

def open_alarm_when_detected(img_thing, name: str, crime: str, criminal_detected: bool, criminal_img: str, names_mug: list, crimes_mug: list, images_mug: list):
    if criminal_detected:
        # criminal_names = [name for name in names_mug]
        # criminal_crimes = [crimes for crimes in crimes_mug]
        # criminal_imgs = [img for img in images_mug]
        # if name in criminal_names and crime in criminal_crimes:
        #     print(f"name: {name}")
        img = cv2.imread(img_thing)
        img = cv2.resize(img, (500, 500))
        x, y, _ = img.shape
        txtpoints = [x // 5, y - 100]
        font_size = min(x, y) / 600
        font_thick = int(3 * font_size)
        criminal = cv2.imread(criminal_img)
        criminal = cv2.resize(criminal, (500, 500))
        combined_img = cv2.hconcat([img, criminal])
        cv2.putText(combined_img, f"{name}", (txtpoints[0], txtpoints[1]), cv2.FONT_HERSHEY_SIMPLEX, font_size, (0, 0, 0), font_thick)
        cv2.moveWindow("Alarm criminal", 500, 200)
        cv2.imshow("Alarm criminal", combined_img)

        if cv2.waitKey(1) == ord('e'):
            cv2.destroyWindow("Alarm criminal")
    else:
        cv2.destroyAllWindows()


while True:
    open_alarm_when_detected("imgs/Alarm.jpg", "Michael", "test", True, "imgs/criminal.jpg",names, crimes, images)

