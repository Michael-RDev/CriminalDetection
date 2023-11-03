import os
from tqdm import tqdm
import face_recognition

training_path = "data/"

def load_image_faces(path: str):
    images = []
    names = []
    crimes = []
    for file in tqdm(os.listdir(path), desc="Loading Images: "):
        images.append(os.path.join(path, file))
        file_parts = file.split("_")
        if file.endswith(".jpg"):
            name, _ = os.path.splitext(file_parts[0])
            names.append(name)
            crimes.append(file_parts[1].split(".jpg")[0])
    return images, names, crimes


def find_face_encodings(images):
    known_face_encodings = []
    for image in tqdm(images, "Finding Face Encodings: "):
        img = face_recognition.load_image_file(image)
        encoding = face_recognition.face_encodings(img)[0]
        known_face_encodings.append(encoding)
    return known_face_encodings

images, names, crimes = load_image_faces(training_path)
known_face_encodings = find_face_encodings(images)