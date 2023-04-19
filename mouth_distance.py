import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
import math
import pyautogui as auto

OPEN_MOUTH = 90

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img, faces = detector.findFaceMesh(img)

    if faces:
        # Obtener los puntos de los bordes de los labios superior e inferior
        upper_lip_top = faces[0][61][1]
        upper_lip_bottom = faces[0][64][1]
        lower_lip_top = faces[0][17][1]
        lower_lip_bottom = faces[0][20][1]

        # Calcular la distancia euclidiana entre los puntos de los bordes de los labios
        distance = math.sqrt((upper_lip_bottom - upper_lip_top)**2 + (lower_lip_bottom - lower_lip_top)**2)

        # Mostrar la distancia calculada en la pantalla
        cv2.putText(img, f"Apertura de la boquita: {distance:.2f}", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Presionar la tecla 'up' cuando se abre la boca
        if distance > OPEN_MOUTH:
            auto.press("up")

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()