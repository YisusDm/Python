import ezdxf

# Nombre del archivo DXF
archivo_dxf = "REFPA.dxf"

# Abre el archivo DXF
doc = ezdxf.readfile(archivo_dxf)

# Accede a la sección ENTITIES
entities_section = doc.modelspace()

# Función para obtener las coordenadas de una entidad LWPOLYLINE
def obtener_coordenadas(entidad):
    #coordenadas = [(p.x, p.y) for path in entidad.paths for p in path]
    coordenadas = [(p[0], p[1]) for p in entidad.get_points()]
    return coordenadas


# Función para obtener la propiedad de la capa como string
def obtener_propiedad_capa(entidad):
    capa = entidad.get_dxf_attrib("layer", default=None)
    if isinstance(capa, str):
        return capa.strip()  # Elimina espacios en blanco alrededor del nombre
    return "SinCapaDefinida"




# Diccionario para almacenar la relación de cotas con los muros
relacion_cotas_muros = {}


# Lista para almacenar las capas
Capas = []
Cotas = []
CoordenadasMuros10 = []
CoordenadasMuros15 = []

for entidad in entities_section:
    # Verifica el tipo de entidad
    if entidad.dxftype() == 'LWPOLYLINE':
        capa = obtener_propiedad_capa(entidad)
        Capas.append(capa)
        #print(f"Capa: {capa}")
    elif entidad.dxftype() == 'DIMENSION':
        Cota = obtener_propiedad_capa(entidad)
        Cotas.append(Cota)
        
        
    

# Itera a través de las capas "Muros 10cm" y "Muros 15cm"
for capa_muro in Capas:
    muros = doc.modelspace().query(f'LWPOLYLINE[layer=="{capa_muro}"]')
    for muro in muros:
        # Obtiene las coordenadas del muro
        coordenadas = obtener_coordenadas(muro)
        #print(f"Capa: {capa_muro}- Muro: {muro} - Coordenadas: {coordenadas}")
        
        # Almacena las coordenadas en el diccionario correspondiente
        if capa_muro == "Muro 10cm":
            print(f"Capa: {capa_muro} - Coordenadas: {coordenadas}")
            
        elif capa_muro == "Muro 15cm":
            print(f"Capa: {capa_muro} - Coordenadas: {coordenadas}")
            



# Muestra la relación de cotas con los muros
print("\nRelación de cotas con los muros:")
for nombre_muro, valor_cota in relacion_cotas_muros.items():
    print(f"{nombre_muro}: {valor_cota}")

# Cierra el archivo DXF
#doc.close()
