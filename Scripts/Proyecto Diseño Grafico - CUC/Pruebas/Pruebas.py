import ezdxf

def calcular_longitudes_muros(archivo_dxf):

    # Abre el archivo DXF
    doc = ezdxf.readfile(archivo_dxf)

    # Inicializa variables para las longitudes de muros de diferentes espesores
    longitud_muros_10cm = 0
    longitud_muros_15cm = 0

    # Itera a través de las entidades en el archivo DXF
    for entity in doc.modelspace().query("LINE"):
        # Verifica el espesor del muro (puedes implementar tu propia lógica aquí)
        espesor_muro = determinar_espesor_muro(entity)

        # Calcula la longitud de la línea
        longitud_linea = entity.length

        # Agrega la longitud de la línea al espesor correspondiente
        if espesor_muro == 10:
            longitud_muros_10cm += longitud_linea
        elif espesor_muro == 15:
            longitud_muros_15cm += longitud_linea

    # Imprime las longitudes totales
    print("Longitud total de muros de 10cm:", longitud_muros_10cm)
    print("Longitud total de muros de 15cm:", longitud_muros_15cm)

def determinar_espesor_muro(entity):
    # Implementa tu propia lógica para determinar el espesor del muro
    # Puedes analizar propiedades como el color, la capa, los atributos, etc.
    # En este ejemplo, simplemente se devuelve un valor ficticio.
    return 10

def Main():
    archivo_dxf = "REFPA.dxf"  # Nombre de archivo específico
    calcular_longitudes_muros(archivo_dxf)

Main()