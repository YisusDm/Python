import ezdxf
import re
import json
import os


# Nombre del archivo DXF
archivo_dxf = "REFPA.dxf"

# Abre el archivo DXF
doc = ezdxf.readfile(archivo_dxf)
carpeta_json = "Json"
# Accede a la sección ENTITIES
entities_section = doc.modelspace()

# Función para obtener las coordenadas de una entidad LWPOLYLINE
def obtener_coordenadas(entidad):
    coordenadas = [(p[0], p[1]) for p in entidad.get_points()]
    return coordenadas


def formatearCoordenada(coordenada):
    # Utilizar expresión regular para extraer las coordenadas
    coincidencia = re.match(r"\((-?\d+\.\d+), (-?\d+\.\d+)", coordenada)

    if coincidencia:
        x = round(float(coincidencia.group(1)), 2)
        y = round(float(coincidencia.group(2)), 2)
        # z = float(coincidencia.group(3))  # Si necesitas también la coordenada z

        return f"({x}, {y})"
        # print("Coordenada z:", z)  # Descomenta si necesitas también la coordenada z
    else:
        print("Entrada no válida en formato coordenadas.")

def cargarJson(Tipo_Entidad,capa,coordenadaFormateada):
    contenido = []  
    nombre_archivo_json = os.path.join(carpeta_json, f"{Tipo_Entidad}.json") 

    if os.path.exists(nombre_archivo_json):
        with open(nombre_archivo_json, "r") as archivo_json_existente:
            contenido = json.load(archivo_json_existente)
            for resultados in contenido:
                if capa == resultados["Capa"]:
                    # Verificar si la clave "Coordenadas" ya existe
                    if "Coordenadas" in resultados:
                        if coordenadaFormateada not in resultados["Coordenadas"]:
                            # Agregar la coordenada a la lista existente
                            resultados["Coordenadas"].append(coordenadaFormateada)
                    else:
                        # Crear la clave "Coordenadas" con la lista
                        resultados["Coordenadas"] = [coordenadaFormateada]

                    # Guardar el JSON actualizado
                    with open(nombre_archivo_json, "w") as archivo_json_actualizado:
                        json.dump(contenido, archivo_json_actualizado, indent=2) 
    

def IterarEntidad():

    for entidad in entities_section:
        if entidad.dxftype() == 'LWPOLYLINE':
            Tipo_Entidad = entidad.dxftype()
            capa = entidad.get_dxf_attrib("layer", default=None)
            coordenadas = obtener_coordenadas(entidad)

            for coord in coordenadas:
                coordenadaFormateada = formatearCoordenada(str(coord))
                cargarJson(Tipo_Entidad,capa,coordenadaFormateada)



