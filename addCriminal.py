import cv2

photo_path = "data/"

cam = cv2.VideoCapture(1)

name = str(input("What is the name of criminal: ")).strip()

crime = str(input("What is the crime committed: ")).strip()

image_name = name + "_" + crime + ".jpg"

while True:
    succ, frame = cam.read()
    if not succ:
        break
    cv2.imshow("criminal capture", frame)
    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite(photo_path + image_name, frame)
        break