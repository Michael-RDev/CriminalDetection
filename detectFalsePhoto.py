import cv2
import torch
import time
from PIL import Image
from transformers import DetrImageProcessor, DetrForObjectDetection
from threading import Thread


def detectPhone(processor, model, saved_pil_image):
    inputs = processor(images=saved_pil_image, return_tensors="pt")
    outputs = model(**inputs)

    target_sizes = torch.tensor([saved_pil_image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

    phone_detected = False
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        class_name = model.config.id2label[label.item()]
        confidence = round(score.item(), 3)
        print(class_name)
        if class_name == "cell phone":
            print("FOUND CELL PHONE")
            phone_detected = True

    return phone_detected

def runPhoneThread(camera):
    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
    model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

    save_interval = 5 
    start_time = time.time()
    last_save_time = start_time

    while True:
        succ, frame = camera.read()
        if not succ:
            break

        current_time = time.time()
        elapsed_time = current_time - last_save_time

        if elapsed_time >= save_interval:
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            pil_image.save("imgs/checkingPhone.jpg")
            last_save_time = current_time  

            saved_image = cv2.imread("imgs/checkingPhone.jpg")
            saved_pil_image = Image.fromarray(cv2.cvtColor(saved_image, cv2.COLOR_BGR2RGB))

            detection_thread = Thread(target=detectPhone, args=(processor, model, saved_pil_image))
            detection_thread.start()

        cv2.imshow('perchance finding phone', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    cam = cv2.VideoCapture(1)
    runPhoneThread(cam)
