import cv2
import os


def escalaGrisesCamara(cap):#Covierte a escala de grises el video que captura la camara
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame, gray
    
def clasificar(clasificacion,gray):#Con la clasificacion xml y el video analiza y clasifica que objetos cumplen con los requisitos
    imagen = clasificacion.detectMultiScale(gray,
    scaleFactor = 10,
    minNeighbors = 20,
    minSize=(200,200))
    return imagen

def identificar(imagen,frame,tipo):#Muestra encerrado en un cuadrado y con un mensaje los objetos que cumplen con los requisitos
    for (x,y,w,h) in imagen:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,tipo,(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
        

if os.path.isfile('IA_Reconocimiento/sources/xml/pirate.xml'):
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    pirateClassif = cv2.CascadeClassifier('IA_Reconocimiento/sources/xml/pirate.xml')
else:
    print("Error: El archivo 'pirate.xml' no existe en la ubicación especificada.")

if pirateClassif.empty():
    print("Error: Cascade classifier not loaded.")

while True:
    frame, gray = escalaGrisesCamara(cap)
    
    #Clasificacion del pirata
    imagen = clasificar(pirateClassif,gray)
    identificar(imagen,frame,"PIRATA")
    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()