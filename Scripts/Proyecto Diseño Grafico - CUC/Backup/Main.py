import ezdxf
import tkinter as tk
from tkinter import filedialog
import json
import os


# Carpeta donde se guardarán los JSON
carpeta_json = "Json"
json_resultados = []

def abrir_archivo_dxf():
    try:
        root = tk.Tk()
        root.withdraw() 

        # Abrir gestor de archivo para seleccionar un DXF
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos DXF", "*.dxf")])

        if not ruta_archivo:
            raise Exception("No se ha seleccionado un archivo DXF.")

        # Leer el archivo DXF y cargarlo
        doc = ezdxf.readfile(ruta_archivo)

        return doc.modelspace()
    except Exception as e:
        raise Exception(f"Error al abrir el archivo DXF: {e}")
    
def LimpiarJson():
    # Crear la carpeta Json si no existe
    if not os.path.exists(carpeta_json):
        os.makedirs(carpeta_json)

    # Eliminar archivos JSON existentes en la carpeta
    for archivo_existente in os.listdir(carpeta_json):
        archivo_completo = os.path.join(carpeta_json, archivo_existente)
        if os.path.isfile(archivo_completo):
            os.remove(archivo_completo)   

    
def init():
    # Accede a la sección ENTITIES
    entities_section = abrir_archivo_dxf()
    list_LWPOLYLINE=[]
    list_DIMENSION=[]

    for entidad in entities_section:
        # Verifica el tipo de entidad
        if entidad.dxftype() == 'LWPOLYLINE':
            if entidad.dxf.layer not in list_LWPOLYLINE:
                list_LWPOLYLINE.append(entidad.dxf.layer)
                resultado = {
                    "Entidad": entidad.dxftype(),
                    "Capa": entidad.dxf.layer
                }
                json_resultados.append(resultado)
                
 
        elif entidad.dxftype() == 'DIMENSION':
            if entidad.dxf.layer not in list_DIMENSION:
                list_DIMENSION.append(entidad.dxf.layer)
                resultado = {
                    "Entidad": entidad.dxftype(),
                    "Capa": entidad.dxf.layer
                }
                json_resultados.append(resultado)
    
    cargarJson()   
     


def cargarJson():

    contenido = []   
    for resultados in json_resultados:
        Nombre = resultados["Entidad"]
        nombre_archivo_json = os.path.join(carpeta_json, f"{Nombre}.json") 

        if os.path.exists(nombre_archivo_json):
            with open(nombre_archivo_json, "r") as archivo_json_existente:
                contenido = json.load(archivo_json_existente)

            # Nueva información que deseas agregar
            nueva_informacion = {
                "Entidad": resultados["Entidad"],
                "Capa": resultados["Capa"]
            }
            contenido.append(nueva_informacion)

            # Guardar el JSON actualizado
            with open(nombre_archivo_json, "w") as archivo_json_actualizado:
                json.dump(contenido, archivo_json_actualizado, indent=2) 
        else:
            # Si el archivo no existe, crear uno nuevo con la información actual
            with open(nombre_archivo_json, "w") as archivo_json_nuevo:
                json.dump([resultados], archivo_json_nuevo, indent=2)


LimpiarJson()
init()
 