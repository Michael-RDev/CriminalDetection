import cv2


def is_inside(rect, box):
    rect_x, rect_y, rect_w, rect_h = rect
    box_x1, box_y1, box_x2, box_y2 = box

    if (box_x1 <= rect_x <= box_x2 and
            box_y1 <= rect_y <= box_y2 and
            box_x1 <= rect_x + rect_w <= box_x2 and
            box_y1 <= rect_y + rect_h <= box_y2):
        return True
    else:
        return False

def detectRectangles(camera):
    while True:
        succ, frame = camera.read()
        if not succ:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        #bounding box
        x, y, _ = frame.shape
        top_left = (int(y / 3), int(x / 8))
        bottom_right = (int(y * 3 / 5), int(x * 3 / 3))
        color = (255, 0, 0)
        thickness = 2

        bounding_box = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])

        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.03 * perimeter, True)

            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                rect_coords = (x, y, w, h)
                if is_inside(rect_coords, bounding_box):
                    cv2.putText(frame, 'Inside Bounding Box', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (0, 0, 255), 2)

        cv2.rectangle(frame, top_left, bottom_right, color, thickness)
        cv2.imshow('Detected Rectangles', frame)
        if cv2.waitKey(1) == ord('q'):
            break


if __name__ == '__main__':
    cam = cv2.VideoCapture(1) 
    detectRectangles(cam)
    cam.release()
    cv2.destroyAllWindows()
