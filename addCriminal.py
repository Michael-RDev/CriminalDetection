import cv2
import requests

photo_path = "data/"


def web_mode():
    pass


def photo_mode(camera):
    name = str(input("What is the name of convicts: "))

    crime = str(input("What is the crime committed: "))

    image_name = name + "_" + crime + ".jpg"
    while True:
        succ, frame = camera.read()
        if not succ:
            break
        cv2.imshow("convicts capture", frame)
        if cv2.waitKey(1) == ord('q'):
            cv2.imwrite(photo_path + image_name, frame)
            break


if __name__ == "__main__":
    cam = cv2.VideoCapture(1)
    mode = str(input("What mode do you want to capture the convict [Cam, Web]: Type (W or C))")).lower()
    if mode == "w":
        web_mode()
    elif mode == "c":
        photo_mode(cam)
    else:
        print("Mode not found please type 'w' or 'c'")

    
    