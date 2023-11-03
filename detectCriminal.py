import face_recognition
import cv2
from loadFunctions import names, known_face_encodings, crimes
from openAlarm import open_alarm_when_detected

def face_recognition_cam(camera, known_face_encodings, names, crimes):
    process_this_frame = True
    criminal_photo = f"imgs/criminal.jpg"
    alarm_img = "imgs/Alarm.jpg"
    while True:
        ret, frame = camera.read()

        if not ret:
            break 
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        if process_this_frame:
            criminal_detected = False
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            face_names = []
            first_match_index = None

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                crime = "N/A"
                if True in matches:
                    criminal_detected = True
                    first_match_index = matches.index(True)
                    if first_match_index != 0:
                        face_locations.insert(first_match_index - len(face_locations), ())

   
                    if face_locations:
                        if 0 <= first_match_index <= len(face_locations):
                            name = names[first_match_index]
                            crime = crimes[first_match_index]
                            if face_locations[first_match_index] != []:
                                top, right, bottom, left = face_locations[first_match_index]
                                face_img = small_frame[top:bottom, left:right]
                                cv2.imwrite(criminal_photo , face_img)  
                        else:
                            pass
                        

                face_names.append(f"Name: {name}, Crime: {crime}")

        process_this_frame = not process_this_frame

        print("face_locations: ", face_locations)
        for indx, location in enumerate(face_locations):
            if location[indx] != []:
                for (top, right, bottom, left), name in zip(location[indx], face_names):
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 255), 2)
                    cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 3)
        if criminal_detected == True:
            open_alarm_when_detected(alarm_img, name, crime, criminal_detected, criminal_photo)
        frame = cv2.resize(frame,(500,300))
        cv2.imshow('criminal recognition weee', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = cv2.VideoCapture(1)
    face_recognition_cam(camera, known_face_encodings, names, crimes)