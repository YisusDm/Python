import ezdxf
import re

archivo_dxf = "REFPA1.dxf"

# Abre el archivo DXF
doc = ezdxf.readfile(archivo_dxf)

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

def ObtenerCotas():
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

                # Crea un nuevo diccionario
                Cotas_coordenadas = {
                    "Nombre": Nombre,
                    "Identificador": Identificador,
                    "Valor Cota": valor_cota,
                    "Puntos": [Punto1, Punto2]
                }
                lista_cotas_coordenadas.append(Cotas_coordenadas)
   
print("Datos finales:")
print(lista_cotas_coordenadas)
