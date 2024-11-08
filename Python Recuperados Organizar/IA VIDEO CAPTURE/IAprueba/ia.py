import cv2 #pip install opencv-python

def escalagris(clasificacion):
    disfraz = clasificacion.detectMultiScale(gray,
    scaleFactor = 5,
    minNeighbors = 91,
    minSize=(70,78))
    return disfraz

def clasificar(imagenesEscalaGris,tipo):
    for (x,y,w,h) in imagenesEscalaGris:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,tipo,(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('frame',frame)
    
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
celularClassif = cv2.CascadeClassifier('celular.xml')
lapizeroClassif = cv2.CascadeClassifier('lapizero.xml')
while True:
    
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    celularEscalaGris = escalagris(celularClassif)
    lapizeroEscalaGris = escalagris(lapizeroClassif)
    
    clasificar(celularEscalaGris,"Celular")
    clasificar(lapizeroEscalaGris,"Lapizero")
    
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()