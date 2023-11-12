import cv2
import time
from loadFunctions import images


# Michael I've only written 4 lines and have error pls help
for imgs in images:
    cv2.imshow("gobbledigoo", imgs)
    time.sleep(1)
