import face_recognition
import cv2

# Cargamos las imágenes de las personas a reconocer
imagen_persona1 = face_recognition.load_image_file("ruta_persona1.jpg")
imagen_persona2 = face_recognition.load_image_file("ruta_persona2.jpg")

# Codificamos las imágenes
codificacion_persona1 = face_recognition.face_encodings(imagen_persona1)[0]
codificacion_persona2 = face_recognition.face_encodings(imagen_persona2)[0]

# Lista de personas y sus codificaciones
personas_conocidas = [codificacion_persona1, codificacion_persona2]
nombres_personas = ["Persona 1", "Persona 2"]

# Inicializamos la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read(

    if not ret:
        break

    # Detectamos los rostros en el cuadro actual
    ubicaciones = face_recognition.face_locations(frame)
    codificaciones = face_recognition.face_encodings(frame, ubicaciones)

    for codificacion, ubicacion in zip(codificaciones, ubicaciones):
        # Comparamos la codificación actual con las codificaciones conocidas
        coincidencias = face_recognition.compare_faces(personas_conocidas, codificacion)

        nombre = "Desconocido"

        # Si encontramos una coincidencia, obtenemos el nombre
        if True in coincidencias:
            indice = coincidencias.index(True)
            nombre = nombres_personas[indice]

        # Dibujamos un rectángulo y el nombre sobre el rostro
        top, right, bottom, left = ubicacion
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, nombre, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    cv2.imshow('Reconocimiento de Rostros', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
