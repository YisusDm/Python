from io import open
from os import path
 
class ContadorDePalabras:
    def __init__(self, archivo):
        self.archivo = archivo
 
    def contar_palabras(self):
        if path.isfile(self.archivo):  
            archivo_origen = open(self.archivo, 'r')  
            contenido = archivo_origen.read()  
            archivo_origen.close()  
 
            palabras = contenido.split()  
            return len(palabras)  
        else:
            print("El archivo no existe.")  
            return 0  
 
archivo = "archivo.txt"  
contador = ContadorDePalabras(archivo)
cantidad_de_palabras = contador.contar_palabras()
print(f"El archivo tiene {cantidad_de_palabras} palabras.")