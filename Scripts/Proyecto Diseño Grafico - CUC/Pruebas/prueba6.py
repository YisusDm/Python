import ezdxf
import re

# Nombre del archivo DXF
archivo_dxf = "REFPA.dxf"

# Abre el archivo DXF
doc = ezdxf.readfile(archivo_dxf)

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

# Lista para almacenar las capas
CoordenadasMuros10 = []
CoordenadasMuros15 = []

for entidad in entities_section:
    if entidad.dxftype() == 'LWPOLYLINE':
        capa = entidad.get_dxf_attrib("layer", default=None)

        coordenadas = obtener_coordenadas(entidad)

        # Almacena las coordenadas en la lista correspondiente
        if capa == "Muro 10cm":
            for coord in coordenadas:
                coordenadaFormateada = formatearCoordenada(str(coord))
                if coordenadaFormateada not in CoordenadasMuros10:
                    CoordenadasMuros10.append(coordenadaFormateada)
        elif capa == "Muro 15cm":
            for coord in coordenadas:
                coordenadaFormateada = formatearCoordenada(str(coord))
                if coordenadaFormateada not in CoordenadasMuros15:
                    CoordenadasMuros15.append(coordenadaFormateada)

# Muestra las listas de coordenadas
print("\nCoordenadas Muros 10cm:")
print(CoordenadasMuros10)

print("\nCoordenadas Muros 15cm:")
print(CoordenadasMuros15)
