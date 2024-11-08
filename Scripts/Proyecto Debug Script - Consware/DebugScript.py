import os
import sqlite3
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, Text

BDLocal = []
TXTLocal = []

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Debug Script")
        
        # Frame para los botones
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(side=tk.RIGHT, padx=20, pady=20)

        # Botón para seleccionar archivo DB3
        self.btn_db3 = tk.Button(self.frame_botones, text="Select Database", command=self.abrir_archivo_DB3)
        self.btn_db3.config(bg="orange")
        self.btn_db3.pack(pady=10)

        # Botón para seleccionar archivo TXT
        self.btn_txt = tk.Button(self.frame_botones, text="   Select Script   ", command=self.abrir_archivo_txt)
        self.btn_txt.config(bg="orange")
        self.btn_txt.pack(pady=10)

        # Botón para iniciar el proceso
        self.btn_start = tk.Button(self.frame_botones, text="Start", command=self.iniciar_proceso)
        self.btn_start.config(bg="silver")
        self.btn_start.pack(pady=10)

        # Frame para la barra de progreso y porcentaje
        self.frame_progress = tk.Frame(root)
        self.frame_progress.pack(side=tk.BOTTOM, pady=20)

        # Barra de progreso
        self.progress = ttk.Progressbar(self.frame_progress, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        # Label para mostrar porcentaje de progreso
        self.lbl_progress = tk.Label(self.frame_progress, text="")
        self.lbl_progress.pack(pady=5)

        # Text widget para la consola gráfica
        self.console = Text(root, height=15, width=80)
        self.console.pack(side=tk.RIGHT, padx=20, pady=20)

    def mostrar_mensaje(self, mensaje):
        self.console.insert(tk.END, mensaje + "\n")
        self.console.see(tk.END)

    def abrir_archivo_DB3(self):
        try:
            ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos DB3", "*.db3")])
            if not ruta_archivo:
                self.btn_db3.config(bg="red")
                raise Exception("No se ha seleccionado un archivo db3.")
            
            _BDLocal_ = (ruta_archivo)
            BDLocal.append(_BDLocal_)
            self.btn_db3.config(bg="lime")

        except Exception as e: 
            self.mostrar_mensaje(f"Error al abrir el archivo db3: {e}")

    def abrir_archivo_txt(self):
        try:
            ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos txt", "*.txt")])
            if not ruta_archivo:
                self.btn_txt.config(bg="red")
                raise Exception("No se ha seleccionado un archivo txt.")
            
            _TXTLocal_ = (ruta_archivo)
            TXTLocal.append(_TXTLocal_)
            self.btn_txt.config(bg="lime")

        except Exception as e: 
            self.mostrar_mensaje(f"Error al abrir el archivo txt: {e}")    

    def ejecutar_consultas_desde_archivo(self, archivo_sql, conexion):
        self.btn_start.config(bg="aqua")
        with open(archivo_sql, 'r') as archivo:
            lineas = archivo.readlines()
            consulta = lineas[0].strip()  # Primera línea es la consulta
            valores = lineas[1:]          # Resto de las líneas son los valores

            self.progress["maximum"] = len(valores)
            self.progress["value"] = 0

            for valor in valores:
                valor = valor.strip()
                if valor.endswith(","):
                    valor = valor[:-1]  # Eliminar la coma final
                consulta_valor = consulta + valor
                try:
                    conexion.execute(consulta_valor)
                    self.progress["value"] += 1
                    porcentaje = int((self.progress["value"] / self.progress["maximum"]) * 100)
                    self.lbl_progress.config(text=f"{porcentaje}%")
                    self.root.update()
                except sqlite3.Error as error:
                    self.mostrar_mensaje(f"Error al ejecutar consulta SQL: {error}")
                    self.mostrar_mensaje(f"{valor}")
                    return False
            
            return True

    def iniciar_proceso(self):
        if not BDLocal:
            self.mostrar_mensaje("Debe seleccionar un archivo DB3.")
            return
        
        if not TXTLocal:
            self.mostrar_mensaje("Debe seleccionar un archivo TXT.")
            return

        self.mostrar_mensaje("Iniciando proceso...")
        
        for nombre_base_datos in BDLocal:
            if os.path.isfile(nombre_base_datos): 
                try:     
                    conexion = sqlite3.connect(nombre_base_datos, check_same_thread=False)
                    cursor = conexion.cursor()

                    VehiculoLocal = f"""DELETE FROM VehiculoLocal  """

                    cursor.execute(VehiculoLocal)

                    for txt in TXTLocal:
                        if not self.ejecutar_consultas_desde_archivo(txt, cursor):
                            self.mostrar_mensaje(f"Error al procesar el archivo {txt}")

                        conexion.commit()

                    self.mostrar_mensaje("Ejecucion finalizada.")

                except sqlite3.Error as error:
                    self.mostrar_mensaje(f"Error al conectar a la base de datos SQLite: {error}")
                finally:
                    if conexion:
                        conexion.close()
            else:
                self.mostrar_mensaje("La base de datos no existe.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
