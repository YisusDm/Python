  
class ConversorDeImagen:

    def __init__(self, archivo_png, archivo_jpg):
        self.archivo_png = archivo_png  # Nombre del archivo PNG
        self.archivo_jpg = archivo_jpg  # Nombre del archivo JPG

    def definir_nombre_archivos(self):

        archivo_png = input("Digite el nombre del archivo Png (sin la extencion de formato): ")
        
        self.archivo_png = f"{archivo_png}.png"
        self.archivo_jpg = f"{archivo_png}.jpg"
 

    def convertir_a_jpg(self):

        # Paso 1: Abrir el archivo PNG en modo lectura binaria
        with open(self.archivo_png, "rb") as archivo_png:
            datos_png = archivo_png.read()  # Leer los datos binarios del PNG
 
        # Paso 2: Abrir el archivo JPG en modo escritura binaria
        with open(self.archivo_jpg, "wb") as archivo_jpg:
            archivo_jpg.write(datos_png)  # Escribir los datos binarios en el archivo JPG
 
# Ejemplo de uso


conversor = ConversorDeImagen("imagen.png", "imagen_convertida.jpg")
conversor.definir_nombre_archivos()
conversor.convertir_a_jpg()
print("La conversión de PNG a JPG se ha realizado con éxito.")    
 

