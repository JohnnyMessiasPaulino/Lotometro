import cv2
import os

#parametros de acesso a camera
#USERNAME = 'admin'
#PASSWORD = '12345678'
IP = '192.168.0.100'
PORT = '4747'

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

#URL no formato do app droid cam para teste utilizando camera de celularf - não pode estar sendo visualizado no navegador
URL = 'http://{}:{}/video'.format(IP, PORT)

webCamera = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)
classificadorVideoFace = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')

while True:
    camera, frame = webCamera.read()

    cinza = cv2.cvtColor(frame, 1)
    detecta = classificadorVideoFace.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=8, minSize=(25, 25))
    for(x, y, l, a) in detecta:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 0), 2)

        contador = str(detecta.shape[0])

        cv2.putText(frame, contador, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.putText(frame, "Número de pessoas: " + contador, (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Video WebCamera", frame)

    if cv2.waitKey(1) == ord('f'):
        break

webCamera.release()
