import cv2
import threading

class VideoCaptureThread:
    def __init__(self, video_source=0):
        self.video_capture = cv2.VideoCapture(video_source)
        self.current_frame = None
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self._update_frame, daemon=True).start()

    def stop(self):
        self.running = False

    def _update_frame(self):
        while self.running:
            ret, frame = self.video_capture.read()
            if ret:
                self.current_frame = frame
            else:
                break

    def get_frame(self):
        return self.current_frame

video_thread1 = VideoCaptureThread()
video_thread2 = VideoCaptureThread()

video_thread1.start()
video_thread2.start()

while True:
    frame1 = video_thread1.get_frame()
    frame2 = video_thread2.get_frame()

    if frame1 is not None and frame2 is not None:
        cv2.imshow('Thread 1', frame1)
        cv2.imshow('Thread 2', frame2)

    if cv2.waitKey(1) == ord('q'):
        break

video_thread1.stop()
video_thread2.stop()
cv2.destroyAllWindows()
