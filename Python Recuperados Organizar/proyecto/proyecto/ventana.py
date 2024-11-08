import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import font
import cv2
import imutils

ventana =Tk()

ventana.resizable(width=False , height=False)
ventana.config(width=764,height=650) 
fondo = PhotoImage(file="fondoooo.png")
fondo1= Label(ventana,image=fondo).place(x=0,y=0,relwidth=1, relheight=1)

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
        etiq_de_video.place(x=100, y=75)
        frame =imutils.resize(frame, width=550)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        image = ImageTk.PhotoImage(image= img)
        etiq_de_video.configure(image=image)
        etiq_de_video.image = image
        etiq_de_video.after(10, iniciar)

def quitar():
    global video
    etiq_de_video.place_forget()
    video.release()
    
        
    

#colores
fondo_boton = "#005aff"
#botones
boton = tk.Button(ventana,text="Iniciar envivo", bg=fondo_boton, relief="flat",curso="hand2",command = video_Stream, width=10, height=2, font=("Calisto MT", 12, "bold"))
boton.place(x=130,y=562)

boton2 = tk.Button(ventana,text="Finalizar envivo", bg=fondo_boton, relief="flat", curso="hand2", command = quitar,width=10, height=2, font=("Calisto MT", 12, "bold"))
boton2.place(x=528,y=562)
#
etiq_de_video = tk.Label(ventana, bg="black")
etiq_de_video.place(x=100, y=75)



ventana.mainloop()



