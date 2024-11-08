import json
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

def abrir_archivo_dxf():
    try:
        root = tk.Tk()
        root.withdraw()

        # Abrir gestor de archivo para seleccionar un DXF
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos TXT", "*.txt")])

        if not ruta_archivo:
            raise Exception("No se ha seleccionado un archivo TXT.")

      

        return ruta_archivo
    except Exception as e:
        raise Exception(f"Error al abrir el archivo TXT: {e}")


# Función para formatear la fecha
def formatear_fecha(fecha_str):
    if fecha_str:
        fecha_dt = datetime.strptime(fecha_str, "%Y/%m/%d %H:%M:%S")
        return {
            "ano": fecha_dt.year,
            "mes": fecha_dt.month,
            "dia": fecha_dt.day,
            "hora": fecha_dt.hour,
            "minuto": fecha_dt.minute,
            "segundo": fecha_dt.second
        }
    else:
        return None


# Nombre de los archivos de entrada y salida"
archivo_salida = "Result.txt"    
archivo_entrada = abrir_archivo_dxf()


# Leer el archivo de entrada
with open(archivo_entrada, "r", encoding="utf-8") as archivo_entrada:
    contenido = archivo_entrada.read()
    try:
        datos_entrada = json.loads(contenido)
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
        # Puedes imprimir el contenido para ver qué hay en el archivo
        print("Contenido del archivo:")
        print(contenido)

# Procesar y modificar los datos según los requisitos
datos_salida = []
for elemento in datos_entrada:
    elemento_modificado = elemento.copy()

    # Formatear fechas
    elemento_modificado["FechaInicial"] = formatear_fecha(elemento_modificado["fInicial"])
    elemento_modificado["FechaFin"] = formatear_fecha(elemento_modificado["fFin"])

    # Establecer "Estado" en 3
    elemento_modificado["Estado"] = 3

    elemento_modificado["fInicial"] = 'null'
    elemento_modificado["fFin"] = 'null'

    datos_salida.append(elemento_modificado)

# Escribir los datos modificados en el archivo de salida
with open(archivo_salida, "w", encoding="utf-8") as archivo_salida:
    json.dump(datos_salida, archivo_salida, ensure_ascii=False, indent=2)


