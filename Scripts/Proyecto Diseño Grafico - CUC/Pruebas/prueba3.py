import ezdxf

archivo_dxf = "REFPA.dxf"
doc = ezdxf.readfile(archivo_dxf)

capas = doc.layers
nombres_capas = ["Muro 10cm", "Muro 15cm", "Cotas"]

for capa in capas:
    if capa.dxf.name in nombres_capas:
        # Imprime el nombre de la capa
        print("Nombre de la capa:", capa.dxf.name)
        
        # Imprime las propiedades de la capa
        print("Color de la capa:", capa.get_color())
        print("Visibilidad de la capa:", capa.is_on())
        
        print() 

