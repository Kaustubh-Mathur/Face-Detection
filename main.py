
""""
import threading
import deepface
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter=0

face_match=False

reference_img=cv2.imread("reference.jpg")


def check_face(frame):
    
    global face_match

    try:
        result = deepface.verify_face(frame, reference_img.copy())
        
        if result['verified']:
            face_match=True
        else:
            face_match=False
    except ValueError:
        face_match=False


while True:
    ret,frame=cap.read()
    if ret:
        if counter % 30 == 0: 
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter+=1

        if face_match:
            cv2.putText(frame," MATCH !!", (20,450), cv2.FONT_ITALIC, 2, (0,255,0),3)
        else:
            cv2.putText(frame,"NO MATCH !!", (20,450), cv2.FONT_ITALIC, 2, (0,0,255),3)
        cv2.imshow("Video",frame)

    key=cv2.waitKey(1)

    if key==ord("q"):
        break

cv2.destroyAllWindows()


"""

"""

import threading
import cv2
import face_recognition

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

counter = 0
face_match = False

reference_img = face_recognition.load_image_file("refrence.jpg")
reference_encoding = face_recognition.face_encodings(reference_img)[0]

def check_face(frame):
    global face_match

    frame_encodings = face_recognition.face_encodings(frame)

    if len(frame_encodings) > 0:
        frame_encoding = frame_encodings[0]
        face_distances = face_recognition.face_distance([reference_encoding], frame_encoding)
        if face_distances[0] < 0.6:
            face_match = True
        else:
            face_match = False

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 2) 

        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, "MATCH", (50, 100), cv2.FONT_HERSHEY_PLAIN, 6, (52, 255, 12), 4)
        else:
            cv2.putText(frame, "NO MATCH", (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (5, 0, 225), 4)
        cv2.imshow("Video", frame)

    key = cv2.waitKey(2)
    if key == ord("q"):
        break

cv2.destroyAllWindows()


"""

import threading
import cv2
import face_recognition

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_locations = []

def detect_faces(frame):
    global face_locations

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)

while True:
    ret, frame = cap.read()
    if ret:
        if counter % 30 == 0:
            threading.Thread(target=detect_faces, args=(frame.copy(),)).start()
        counter += 1

        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, 'Face', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()


