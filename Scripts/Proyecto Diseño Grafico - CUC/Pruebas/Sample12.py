import ezdxf

# Escala de dibujo en metros por unidad de dibujo
escala_dibujo = 0.001  # Por ejemplo, 1 unidad de dibujo = 1 mm = 0.001 metros

def Main():
    archivo_dxf = "REFPA.dxf"  # Ruta completa de tu archivo DXF
    analizar_dibujo(archivo_dxf)


def analizar_dibujo(dxf_file_path):
    doc = ezdxf.readfile(dxf_file_path)

    # Diccionario para almacenar las cantidades de muros por espesor
    cantidades_muros = {"Muro 10cm (Verde)": 0, "Muro 15cm (Azul)": 0}


    msp = doc.modelspace()
    for entity in msp.query('*[layer=="Muros"]'):
        if entity.dxftype() == 'LWPOLYLINE':
            nombre_entidad = entity.get_dxf_attrib('layer')  # Obtener el nombre de la capa
            color_entidad = entity.dxf.color  # Obtener el color
            if nombre_entidad in cantidades_muros:



                espesor = 10 if color_entidad == 256 else 15  # Asignar espesor en función del color
                longitud_dibujo = entity.length  # Usar .length para obtener la longitud
                longitud_metros = longitud_dibujo * escala_dibujo
                cantidades_muros[nombre_entidad] += longitud_metros

    # Imprimir la tabla de cantidades en metros
    print("Nombre del Muro\tLongitud (m)")
    for nombre_muro, longitud_metros in cantidades_muros.items():
        print(f"{nombre_muro}\t{longitud_metros:.2f}")



Main()