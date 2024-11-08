import os
import sqlite3
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm

BDLocal = []
TXTLocal = []



def abrir_archivo_DB3():
    try:
        root = tk.Tk()
        root.withdraw()

        # Abrir gestor de archivo para seleccionar un DXF
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos DB3", "*.db3")])

        if not ruta_archivo:
            raise Exception("No se ha seleccionado un archivo db3.")

        _BDLocal_ = (ruta_archivo)
        BDLocal.append(_BDLocal_)
        init(BDLocal)

        return _BDLocal_
    except Exception as e: 
        raise Exception(f"Error al abrir el archivo db3: {e}")
    
def abrir_archivo_txt():
    try:
        root = tk.Tk()
        root.withdraw()

        # Abrir gestor de archivo para seleccionar un DXF
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos txt", "*.txt")])

        if not ruta_archivo:
            raise Exception("No se ha seleccionado un archivo txt.")

        _TXTLocal_ = (ruta_archivo)
        TXTLocal.append(_TXTLocal_)
        init(TXTLocal)

        return _TXTLocal_
    except Exception as e: 
        raise Exception(f"Error al abrir el archivo txt: {e}")    


def ejecutar_consultas_desde_archivo(archivo_sql, conexion):
    with open(archivo_sql, 'r') as archivo:
        lineas = archivo.readlines()
        consulta = lineas[0].strip()  # Primera línea es la consulta
        valores = lineas[1:]          # Resto de las líneas son los valores

        for valor in tqdm(valores, desc="Procesando", ncols=100):
            valor = valor.strip()
            if valor.endswith(","):
                valor = valor[:-1]  # Eliminar la coma final

            consulta_valor = consulta + valor
            try:
                conexion.execute(consulta_valor)
            except sqlite3.Error as error:
                print(f"Error al ejecutar consulta SQL: {error}")
                print(f"'{valor}'")
                return False
        
        return True


def init(BDLocal):
    for nombre_base_datos in BDLocal:
        if os.path.isfile(nombre_base_datos): # Validar si la base de datos existe
            try:     # Conectar a la base de datos SQLite
                conexion = sqlite3.connect(nombre_base_datos, check_same_thread=False)
                cursor = conexion.cursor()

                # Consulta SQL para Limpiar las tablas
                VehiculoLocal = f"""DELETE FROM VehiculoLocal  """

                # Ejecutar la consulta SQL
                cursor.execute(VehiculoLocal)

                abrir_archivo_txt()
                for txt in TXTLocal:
                    # Ejecutar consultas SQL desde el archivo
                    if not ejecutar_consultas_desde_archivo(txt, cursor):
                        print(f"Error al procesar el archivo {txt}")

                    # Guardar cambios
                    conexion.commit()


            except sqlite3.Error as error:
                print("Error al conectar a la base de datos SQLite:", error)
            finally:
                if conexion:
                    conexion.close()
        else:
            print("La base de datos no existe.")

abrir_archivo_DB3()
