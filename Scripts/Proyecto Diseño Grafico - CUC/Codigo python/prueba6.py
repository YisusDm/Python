import ezdxf
import re

archivo_dxf = "REFPA.dxf"
doc = ezdxf.readfile(archivo_dxf)
entities_section = doc.modelspace()

def obtener_coordenadas(entidad):
    coordenadas = [(p[0], p[1]) for p in entidad.get_points()]
    return coordenadas


def formatearCoordenada(coordenada):
    coincidencia = coordenada
    if coincidencia:
        x = round(float(coincidencia.group(1)), 2)
        y = round(float(coincidencia.group(2)), 2)
        return f"({x}, {y})"
    else:
        return ""

CoordenadasMuros10 = []
CoordenadasMuros15 = []

for entidad in entities_section:
    if entidad.dxftype() == 'LWPOLYLINE':
        capa = entidad.get_dxf_attrib("layer", default=None)
        coordenadas = obtener_coordenadas(entidad)
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


