import cv2
import urllib.request
import numpy as np

photo_path = "data/"


def web_mode(imagelink):
    name = str(input("What is the name of convicts: "))
    crime = str(input("What is the crime committed: "))
    image_name = name + "_" + crime + ".jpg"

    open_url = urllib.request.urlopen(imagelink)
    url_array = np.array(bytearray(open_url.read()), dtype=np.uint8)
    image = cv2.imdecode(url_array, cv2.IMREAD_COLOR)

    cv2.imshow("Press something if correct", image)
    if cv2.waitKey(0):
        cv2.imwrite(photo_path+image_name, image)
        cv2.destroyAllWindows()

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
    cam = cv2.VideoCapture(0)
    mode = str(input("What mode do you want to capture the convict [Cam, Web]: Type (W or C))")).lower()
    if mode == "w":
        imagelink = input("Provide image link here:")
        web_mode(imagelink)
    elif mode == "c":
        photo_mode(cam)
    else:
        print("Mode not found please type 'w' or 'c'")
