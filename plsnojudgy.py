import cv2
import time
import os
from tqdm import tqdm


# Michael I've only written 4 lines and have error pls help
def load_image_faces(path: str):
    images = []
    for file in tqdm(os.listdir(path), desc="Mug Shot Imgs: "):
        images.append(os.path.join(path, file))
    return images


