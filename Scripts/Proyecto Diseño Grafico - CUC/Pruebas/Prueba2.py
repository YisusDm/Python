# # Vista previa archivos DXF en una ventana Grafica: ezdxf view REFPA.dxf 
# # Imprima información básica sobre archivos DXF: ezdxf info REFPA.dxf 
# # Mostrar información detallada y estructuras de archivos DXF: ezdxf browse REFPA.dxf 
# # Auditar archivos DXF: ezdxf audit REFPA.dxf

# import sys
# import ezdxf
# import math

# def longitud(punto1, punto2):
#     # Sirve para obtener la longitud de una línea con solo dos decimales
#     return round(math.dist(punto1, punto2), 2)

# # Helper Functions
# def print_entity(e):
#     print("LINE on Layer: %s" % e.dxf.layer)
#     #print("Start point: %s" % e.dxf.start)
#     #print("End point: %s" % e.dxf.end)
#     #print("Length: %s" % longitud(e.dxf.start, e.dxf.end))
#     #print("Color: %s\n" % e.dxf.color)

# if __name__ == "__main__":
#     archivo_dxf = "REFPA.dxf"  # Nombre de archivo específico


# try:
#     doc = ezdxf.readfile(archivo_dxf)
#     msp = doc.modelspace()

#     for e in msp:
#         #print(e)
#         if e.dxftype() == 'LWPOLYLINE':
#             print_entity(e)
#         elif e.dxftype() == 'DIMENSION':
#             print_entity(e)
# except Exception as e:
#     print("Error:", str(e))

# ###########################################################################

# # Abre el espacio de modelo (modelspace)
# msp = doc.modelspace()

# # Crea un conjunto para almacenar todas las capas únicas encontradas
# capas = set()

# # Itera a través de las entidades en el espacio de modelo
# for entidad in msp.query('*'):
#     # Accede al atributo de capa de la entidad
#     capa = entidad.dxf.layer
#     # Agrega la capa al conjunto
#     capas.add(capa)

# # Ahora, puedes iterar sobre las capas únicas encontradas
# for capa in capas:
#     print("Capa:", capa)

# # Cierra el archivo DXF
# #doc.close()




# ########################################################################

# # Accede a la tabla de capas
# capas = doc.layers

# # Itera a través de las capas en la tabla de capas
# for capa in capas:
#     # Imprime el nombre de la capa
#     print("Nombre de la capa:", capa.dxf.name)
    
#     # Imprime las propiedades de la capa
#     print("Color de la capa:", capa.get_color())
#     #print("Linetype de la capa:", capa.get_linetype())
#     print("Visibilidad de la capa:", capa.is_on())
    
#     # Agrega más propiedades de capa según sea necesario
    
#     print()  # Línea en blanco para separar las capas

# # Cierra el archivo DXF
# #doc.close()

#####################################################################

import ezdxf

# Nombre del archivo DXF
archivo_dxf = "REFPA.dxf"

# Abre el archivo DXF
doc = ezdxf.readfile(archivo_dxf)

# Accede a la tabla de capas
capas = doc.layers

# Nombres de las capas que deseas trabajar
nombres_capas = ["Muro 10cm", "Muro 15cm", "Cotas"]

# # Itera a través de las capas en la tabla de capas
for capa in capas:
    # Verifica si el nombre de la capa está en la lista de nombres de capas deseadas
    if capa.dxf.name in nombres_capas:
        # Imprime el nombre de la capa
        print("Nombre de la capa:", capa.dxf.name)
        
        # Imprime las propiedades de la capa
        print("Color de la capa:", capa.get_color())
        print("Visibilidad de la capa:", capa.is_on())
        
        # Agrega más propiedades de capa según sea necesario
        
        print()  # Línea en blanco para separar las capas


####################################################################


# import ezdxf

# # Nombre del archivo DXF
# archivo_dxf = "REFPA.dxf"

# # Abre el archivo DXF
# doc = ezdxf.readfile(archivo_dxf)

# # Nombres de las capas que deseas inspeccionar
# nombres_capas = ["Muro 10cm", "Muro 15cm"]

# # Abre el espacio de modelo (modelspace)
# msp = doc.modelspace()

# # Diccionario para almacenar las dimensiones de los muros
# dimensiones_muros = {}

# # Itera a través de las entidades en el espacio de modelo
# for entidad in msp:
#     # Verifica si la capa de la entidad está en la lista de nombres de capas deseadas
#     if entidad.dxf.layer in nombres_capas:
#         # Si la entidad es una cota (DIMENSION)
#         if entidad.dxftype() == 'DIMENSION':
#             # Accede a la propiedad DIMENSION (actual_measurement)
#             longitud = entidad.dxf.actual_measurement
#             # Agrega la longitud del muro al diccionario
#             dimensiones_muros[entidad.handle] = longitud

# # Muestra las dimensiones de los muros
# for handle, longitud in dimensiones_muros.items():
#     print(f"Entidad con Handle {handle}: Longitud del muro = {longitud}")

# # Cierra el archivo DXF
# #doc.close()





