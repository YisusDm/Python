import ezdxf
import re

archivo_dxf = "REFPA.dxf"
doc = ezdxf.readfile(archivo_dxf)
entities_section = doc.modelspace()

def formatearCoordenada(coordenada):
    coincidencia = coordenada
    if coincidencia:
        x = round(float(coincidencia.group(1)), 2)
        y = round(float(coincidencia.group(2)), 2)
        return f"({x}, {y})"
    else:
        return ""

def ObtenerCotas():
    lista_cotas_coordenadas = []
    for entidad in entities_section:
        if entidad.dxftype() == 'DIMENSION':
            Nombre = entidad.dxf.layer
            Identificador = entidad.dxf.handle
            valor_cota = entidad.get_dxf_attrib("actual_measurement", default=None)
            defpoint1 = entidad.get_dxf_attrib("defpoint2", default=None)
            defpoint2 = entidad.get_dxf_attrib("defpoint3", default=None)

            if valor_cota is not None and defpoint1 is not None and defpoint2 is not None:
                valor_cota = round(valor_cota, 2)
                Punto1 = formatearCoordenada(str(defpoint1))
                Punto2 = formatearCoordenada(str(defpoint2))

                Cotas_coordenadas = {
                    "Nombre": Nombre,
                    "Identificador": Identificador,
                    "Valor Cota": valor_cota,
                    "Puntos": [Punto1, Punto2]
                }
                lista_cotas_coordenadas.append(Cotas_coordenadas)
   

