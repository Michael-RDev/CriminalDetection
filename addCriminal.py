import cv2
import urllib.request
import numpy as np
import time

photo_path = "data/"

# jpg is current, png is former
def get_image_name():
    name = str(input("What is the name of convict: "))
    crime = str(input("What is the crime committed: "))
    type = str(input("Is this a current or former criminal? (C or F)")).lower()
    if type == "c":
        return name + "_" + crime + ".jpg"
    elif type == "f":
        return name + "_" + crime + ".png"
    else:
        print("Neither keys C nor F were pressed")
        exit()

def web_mode(imagelink):

    image_name = get_image_name()

    open_url = urllib.request.urlopen(imagelink)
    url_array = np.array(bytearray(open_url.read()), dtype=np.uint8)
    image = cv2.imdecode(url_array, cv2.IMREAD_COLOR)

    cv2.imshow("Press something if correct", image)
    if cv2.waitKey(0):
        cv2.imwrite(photo_path+image_name, image)
        cv2.destroyAllWindows()

def photo_mode(camera):
    
    image_name = get_image_name()
    print("Press the Q-Key when you want the picture taken")
    time.sleep(3)
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
        imagelink = input("Provide image link here, then press enter:")
        web_mode(imagelink)
    elif mode == "c":
        photo_mode(cam)
    else:
        print("Mode not found please type 'W' or 'C'")