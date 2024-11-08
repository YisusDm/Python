import tkinter as tk
from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
import cv2
import imutils
import webbrowser

ventana =Tk()
ventana.iconbitmap("IA_Reconocimiento/sources/img/ico3.ico")
ventana.title("Reconocimiento")
ventana.resizable(width=False , height=False)
ventana.config(width=887,height=617) 
fondo = PhotoImage(file="IA_Reconocimiento/sources/img/fondo.png")
fondo1= Label(ventana,image=fondo).place(x=0,y=0,relwidth=1, relheight=1)

cascadeClasf = cv2.CascadeClassifier('IA_Reconocimiento/sources/xml/cascade.xml')

#funciones
video = None

def video_Stream():
    global video
    video = cv2.VideoCapture(0)
    iniciar()

def iniciar():
    global video
    ret, frame = video.read()
    if ret == True:
        etiq_de_video.place(x=61, y=87)
        frame =imutils.resize(frame, width=580)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        image = ImageTk.PhotoImage(image= img)
        etiq_de_video.configure(image=image)
        etiq_de_video.image = image
        etiq_de_video.after(10, iniciar)

        obj = cascadeClasf.detectMultiScale(frame,
        scaleFactor = 9,
        minNeighbors = 91,
        minSize=(70,78))#se convierte la imagen en escala de gris y se guarda en variable toy
        
        for (x,y,w,h) in obj:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)#dibujar el rectangulo
            cv2.putText(frame,'Pirata',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)#colocar el nombre del objeto
            Btn3.place(x=715,y=280)
        
def quitar():
    global video
    etiq_de_video.place_forget()
    video.release()

#colores
fondo_boton = "#005aff"
#botones
boton = tk.Button(ventana,text="Iniciar en vivo", bg=fondo_boton, relief="flat",curso="hand2",command = video_Stream, width=12, height=2, font=("Calisto MT", 12, "bold"))
boton.place(x=715,y=90)

boton2 = tk.Button(ventana,text="Finalizar en vivo", bg=fondo_boton, relief="flat", curso="hand2", command = quitar,width=12, height=2, font=("Calisto MT", 12, "bold"))
boton2.place(x=715,y=470)
#
etiq_de_video = tk.Label(ventana, bg="black")
etiq_de_video.place(x=0, y=0)

#
#nuevo = 1
url = "https://youtu.be/nzfnpmD6-5I"
def openweb ():
    webbrowser.open (url)

Btn3 = tk.Button (ventana, text = "Consultar disfraz",bg = fondo_boton, relief = "flat", curso = "hand2", command = openweb, width = 12, height = 2, font = ("Calisto MT", 12, "bold"))
Btn3.place(x=715,y=280)
Btn3.place_forget()
#Btn3.pack ()

ventana.mainloop()