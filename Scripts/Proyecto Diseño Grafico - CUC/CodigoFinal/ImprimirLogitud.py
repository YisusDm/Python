from tabulate import tabulate
import json
import os
import shutil

carpeta_json = "Json"
Archivos = []
ListaCapas = []
Capas_Cotas = []
LongitudCapas = []
resultado_final=[]
def BuscarArchivos():
    for archivo_existente in os.listdir(carpeta_json):
        archivo_completo = os.path.join(carpeta_json, archivo_existente)
        archivo_completo = archivo_completo.replace('Json\\', '')
        Archivos.append(archivo_completo)  
    AbrirArchivos()

def AbrirArchivos():

    for Archivo in Archivos:
        nombre_archivo_json = os.path.join(carpeta_json, Archivo) 
        with open(nombre_archivo_json, "r") as archivo_json_existente:
            contenido = json.load(archivo_json_existente)
            for resultados in contenido:
                if "DIMENSION" == resultados["Entidad"]:
                    capa = resultados['Capa']
                    cotas = resultados['Cotas']
                    identificadores = [cota["Identificador"] for cota in resultados["Cotas"]]
                    if identificadores not in (cota["Identificador"] for cota in resultados["Cotas"]):
                        resultado = [{'Capa': capa, 'Cotas': cotas}]
                        resultado_final.append(resultado)

                elif "LWPOLYLINE" == resultados["Entidad"]:
                    capa = resultados['Capa']
                    Coordenadas = resultados['Coordenadas']
                    resultado = [{'Capa': capa, 'Coordenadas': Coordenadas}]
                    resultado_final.append(resultado)
    RelacionarCotaCoordenada()                
                        
def RelacionarCotaCoordenada():
    for capa_resultados in resultado_final:
        for capa_seleccionada in capa_resultados:
            if capa_seleccionada['Capa'] == 'Cotas':
                for cota in capa_seleccionada['Cotas']:
                    Identificador = cota['Identificador']
                    LongitudCota = cota['Valor Cota']
                    puntos = cota['Puntos']
                    # Evalúa la cadena para obtener una lista de tuplas
                    coordenadas_cota  = eval(puntos)
                    (P1X1, P1Y1), (P2X2, P2Y2) = coordenadas_cota 
                    for capa_verificar in resultado_final: 
                        for capa in capa_verificar:
                            if capa['Capa'] != 'Cotas':
                                nombre_capa = capa['Capa']
                                if nombre_capa not in ListaCapas:
                                    ListaCapas.append(nombre_capa)
                                for coordenada1_capa in capa['Coordenadas']:
                                    coordenada1_capa = eval(coordenada1_capa)
                                    (C1X1, C1Y1) = coordenada1_capa
                                    if C1X1 == P1X1 and C1Y1 ==P1Y1:
                                        for coordenada2_capa in capa['Coordenadas']:
                                            coordenada2_capa = eval(coordenada2_capa)
                                            (C2X2, C2Y2) = coordenada2_capa
                                            if C2X2 == P2X2 and C2Y2 == P2Y2:
                                                Acotado = {
                                                    "Identificador": Identificador,
                                                    "Capa": nombre_capa,
                                                    "Cota": LongitudCota
                                                }
                                                Capas_Cotas.append(Acotado)
    AgruparLongitud()


def AgruparLongitud():
    for capa in ListaCapas:
        LongitudFinal = 0
        for capa_id in Capas_Cotas:
            idCapa = capa_id['Capa']
            if capa == idCapa:
                LongitudCota = capa_id['Cota']
                LongitudFinal += LongitudCota
        Acotado = {
            "Capa": capa,
            "Longitud": LongitudFinal
        }
        LongitudCapas.append(Acotado)
    MostrarResultado()       

def MostrarResultado():
        tabla_datos = []
        nombre_archivo = "AutoCAD.txt"
        for LogCap in LongitudCapas:
            nombre = LogCap['Capa']
            Longitud = LogCap['Longitud']
            tabla_datos.append([nombre, Longitud])
        #print(tabulate(tabla_datos, headers=['Capa Espesor', 'Longitud'], tablefmt="grid"))   

        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, "w") as archivo:
                archivo.write("")

        with open(nombre_archivo, "a") as archivo:
            print("    UNIVERSIDAD DE LA COSTA",file=archivo)
            print("       Proyecto de Aula",file=archivo)
            print ("	Diseño Gráfico",file=archivo)
            print ("	    2023-2",file=archivo)  
            print(tabulate(tabla_datos, headers=['Capa Espesor', 'Longitud'], tablefmt="grid"), file=archivo)
            print("                VERSION - 11.13",file=archivo)
            print("",file=archivo)
            print("Grupo: \nANGULO HENRY \nESTRADA JUAN \nMARQUEZ JESUS \nMENDOZA ARTURO \nVILLA BRANDON",file=archivo)

        EliminarTemp()
        # Abrir el archivo automáticamente
        os.system("notepad " + nombre_archivo) 
        

def EliminarTemp():

    # Eliminar archivos JSON existentes en la carpeta
    for archivo_existente in os.listdir(carpeta_json):
        archivo_completo = os.path.join(carpeta_json, archivo_existente)
        if os.path.isfile(archivo_completo):
            os.remove(archivo_completo)  

    # Eliminar solo si está vacía
    if os.path.exists(carpeta_json):
        try:
            os.rmdir(carpeta_json)
            print(f'Carpeta "{carpeta_json}" eliminada con éxito.')
        except OSError as e:
            print(f'Error al eliminar la carpeta "{carpeta_json}": {e}')

    # eliminar la carpeta y su contenido
    if os.path.exists(carpeta_json):
        try:
            shutil.rmtree(carpeta_json)
            print(f'Carpeta "{carpeta_json}" eliminada con éxito.')
        except OSError as e:
            print(f'Error al eliminar la carpeta "{carpeta_json}": {e}')        


#print(LongitudCapas)