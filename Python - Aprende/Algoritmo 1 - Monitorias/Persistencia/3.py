
from io import open
from os import path
 
class ConcatenadorDeArchivos:
    def _init_(self, archivos_origen, archivo_destino):
        self.archivos_origen = archivos_origen
        self.archivo_destino = archivo_destino
 
    def concatenar(self):
        contenido_concatenado = ""  
 
        for archivo in self.archivos_origen:
            if path.isfile(archivo):  
                archivo_origen = open(archivo, 'r')
                contenido = archivo_origen.read()
                archivo_origen.close()
                contenido_concatenado += contenido  
            else:
                print(f"El archivo {archivo} no existe.")      
 
        archivo_destino = open(self.archivo_destino, 'w')  
        archivo_destino.write(contenido_concatenado)  
        archivo_destino.close()

    def Iniciar_Archivos(self):
        print("Ingrese los nombres de los archivos que desea concatenar:")
        archivos_origen = []
        while True:
            archivo = input("Nombre del archivo (vacio para finalizar): ")
            if archivo == "":
                break
            archivos_origen.append(archivo)

        self.archivos_origen = archivos_origen    

a = ConcatenadorDeArchivos("Arch.txt", "Archivo.txt")

a = a.Iniciar_Archivos()
# a.concatenar()