# pip install deepface

import cv2
from deepface import DeepFace
import time

from mood_helper import select_image, send_email, speak_message

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

################################
wCam, hCam = 640, 480
################################
 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

cTime = 0
pTime = 0
allowed_emotions = {"happy", "sad", "angry", "fear"}
current_emotion = None
captured = False

while True:
    success, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for x, y, w, h in face:
        image = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        try:
            analyze = DeepFace.analyze(img, actions=['emotion'], silent=True)
            emotion = analyze[0]['dominant_emotion']
            if emotion in allowed_emotions and emotion != current_emotion:
                current_emotion = emotion
                captured = False
                cTime = time.time()
        except:
            print('face not recognized')

    pTime = time.time()
    diff = pTime - cTime

    if diff >= 3:
        captured = True
        file_name = select_image(current_emotion)
        send_email("iddhomies@gmail.com", "zpakin@hpeprint.com", "MoodHelper has tuned into your " + current_emotion + " mood. Here's a picture to brighten your day!", file_name, open('gmail_password.key', 'r').read().strip())
        speak_message(current_emotion)

    cv2.putText(img, f'TIME: {int(diff)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
    cv2.putText(img, current_emotion, (40, 80), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (255, 0, 0), 3)
    cv2.putText(img, f'CAPT: {str(captured)}', (40, 110), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()