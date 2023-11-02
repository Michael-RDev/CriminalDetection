import cv2
import requests

photo_path = "data/"

cam = cv2.VideoCapture(1)


def web_mode():
    pass


def photo_mode(camera):
    name = str(input("What is the name of convicts: ")).strip()

    crime = str(input("What is the crime committed: ")).strip()

    image_name = name + "_" + crime + ".jpg"
    succ, frame = cam.read()
    if not succ:
        return
    cv2.imshow("convicts capture", frame)
    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite(photo_path + image_name, frame)
        return

if __name__ == "__main__":
    photo_mode(cam)
    
    