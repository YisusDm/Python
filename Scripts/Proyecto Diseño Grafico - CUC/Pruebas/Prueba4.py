from shapely.geometry import LineString
import ezdxf

# Longitudes esperadas
longitud_muro_15cm_esperada = 45.1  # metros
longitud_muro_10cm_esperada = 19.61  # metros

# Calcular la escala de dibujo
escala_muro_15cm = longitud_muro_15cm_esperada / 45.1  # Ajusta el valor de 45.1 a tus resultados reales
escala_muro_10cm = longitud_muro_10cm_esperada / 19.61  # Ajusta el valor de 19.61 a tus resultados reales

def calcular_longitud_entidades(entidades):
    longitud_total = 0
    for entidad in entidades:
        if entidad.dxftype() == 'LWPOLYLINE':
            vertices = [(p[0], p[1]) for p in entidad.get_points()]
            line = LineString(vertices)
            longitud_total += line.length
    return longitud_total

def analizar_dibujo(dxf_file_path):
    doc = ezdxf.readfile(dxf_file_path)
    msp = doc.modelspace()
    longitudes_muros = {"Muro10cm": 0, "Muro15cm": 0}

    for entidad in msp.query('*[layer=="Muro10cm" | layer=="Muro15cm"]'):
        nombre_capa = entidad.get_dxf_attrib('layer')
        longitud_real = calcular_longitud_entidades([entidad])

        if nombre_capa == "Muro10cm":
            longitud_metros = longitud_real * escala_muro_10cm
            longitudes_muros["Muro10cm"] += longitud_metros
        elif nombre_capa == "Muro15cm":
            longitud_metros = longitud_real * escala_muro_15cm
            longitudes_muros["Muro15cm"] += longitud_metros

    return longitudes_muros

if __name__ == "__main__":
    archivo_dxf = r"REF_PA.dxf"  # Ruta completa de tu archivo DXF
    resultados = analizar_dibujo(archivo_dxf)

    # Imprimir las longitudes en metros por espesor de muros
    print("Espesor de muro\tLongitud en planta")
    for espesor, longitud in resultados.items():
        longitud_metros = round(longitud, 2)  # Redondear a dos decimales
        print(f"{espesor}\t{longitud_metros}m")