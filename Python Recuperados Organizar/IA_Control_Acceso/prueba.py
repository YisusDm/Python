import cv2

# Cargamos el clasificador preentrenado para detección de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Si deseas utilizar una cámara en tiempo real, cambia el argumento a 0
# Para cargar una imagen, proporciona la ruta de la imagen en lugar de 0 o 1
cap = cv2.VideoCapture(0)

while True:
    # Captura un marco de video
    ret, frame = cap.read()

    if not ret:
        break

    # Convierte la imagen a escala de grises para el reconocimiento de rostros
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostros en la imagen
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Dibuja rectángulos alrededor de los rostros detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Muestra la imagen resultante
    cv2.imshow('Reconocimiento de Rostros', frame)

    # Si se presiona la tecla 'q', sale del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra todas las ventanas
cap.release()
cv2.destroyAllWindows()
