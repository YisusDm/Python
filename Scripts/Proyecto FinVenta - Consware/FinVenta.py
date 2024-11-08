from os import system, name
from tqdm import tqdm
from FinVenta_Rango_Fecha import *
from FinVenta_Buscar_NumeroDocumentos import *

def limpiar():
    #Limpia la linea de comandos
    if name == "nt":
        system("cls")
    else:
        system("clear")

while True:
    limpiar()
    action = input("""1. Armar Json Ventas en Rango de Fechas
                    \n2. Armar Json Ventas Especificas
                    \n3. Salir del Progarama
                        Elige la accion: """)

    if action == "1":
        limpiar()
        VentaRangoFechaAviso()
        limpiar()
        VentaRangoFecha()

    elif action == "2":
        limpiar()    
        BuscarNumeroDocumento()
        time.sleep(15)
    elif action == "3":
        break

    else:
        print("¡Escoja una de las tres opciones del menu!")
        input("Presione ENTER") 











