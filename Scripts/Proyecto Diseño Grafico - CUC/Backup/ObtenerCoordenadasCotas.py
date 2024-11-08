import ezdxf
import re
import json
import os

# Nombre del archivo DXF
archivo_dxf = "REFPA1.dxf"


# Abre el archivo DXF
doc = ezdxf.readfile(archivo_dxf)
carpeta_json = "Json"

# Accede a la sección ENTITIES
entities_section = doc.modelspace()

# Lista para almacenar múltiples diccionarios
lista_cotas_coordenadas = []

def formatearCoordenada(coordenada):
    # Utilizar expresión regular para extraer las coordenadas
    coincidencia = re.match(r"\((-?\d+\.\d+), (-?\d+\.\d+), (-?\d+\.\d+)\)", coordenada)

    if coincidencia:
        x = round(float(coincidencia.group(1)), 2)
        y = round(float(coincidencia.group(2)), 2)
        # z = float(coincidencia.group(3))  # Si necesitas también la coordenada z

        return f"({x}, {y})"
        # print("Coordenada z:", z)  # Descomenta si necesitas también la coordenada z
    else:
        print("Entrada no válida en formato coordenadas.")

def cargarJson(Tipo_Entidad,capa,Cotas_coordenadas):
    contenido = []  
    nombre_archivo_json = os.path.join(carpeta_json, f"{Tipo_Entidad}.json") 

    if os.path.exists(nombre_archivo_json):
        with open(nombre_archivo_json, "r") as archivo_json_existente:
            contenido = json.load(archivo_json_existente)
            for resultados in contenido:
                if capa == resultados["Capa"]:
                    # Verificar si la clave "Cotas" ya existe
                    if "Cotas" in resultados:
                        identificadores = [cota["Identificador"] for cota in resultados["Cotas"]]
                        if Cotas_coordenadas["Identificador"] not in identificadores:
                            # Agregar la coordenada a la lista existente
                            resultados["Cotas"].append(Cotas_coordenadas)
                    else:
                        # Crear la clave "Cotas" con la lista
                        resultados["Cotas"] = [Cotas_coordenadas]

                    # Guardar el JSON actualizado
                    with open(nombre_archivo_json, "w") as archivo_json_actualizado:
                        json.dump(contenido, archivo_json_actualizado, indent=2)

def ObtenerCotas():
    for entidad in entities_section:
        if entidad.dxftype() == 'DIMENSION':
            Tipo_Entidad = entidad.dxftype()
            capa = entidad.dxf.layer
            Identificador = entidad.dxf.handle
            valor_cota = entidad.get_dxf_attrib("actual_measurement", default=None)
            defpoint1 = entidad.get_dxf_attrib("defpoint2", default=None)
            defpoint2 = entidad.get_dxf_attrib("defpoint3", default=None)

            if valor_cota is not None and defpoint1 is not None and defpoint2 is not None:
                valor_cota = round(valor_cota, 2)
                Punto1 = formatearCoordenada(str(defpoint1))
                Punto2 = formatearCoordenada(str(defpoint2))
                Punto = f"[{Punto1}, {Punto2}]"

                # Crea un nuevo diccionario
                Cotas_coordenadas = {
                    "Identificador": Identificador,
                    "Valor Cota": valor_cota,
                    "Puntos": Punto
                }

                cargarJson(Tipo_Entidad,capa,Cotas_coordenadas)



ObtenerCotas()

