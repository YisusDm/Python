import ezdxf
import math


def longitud(punto1, punto2):
    # Sirve para obtener la longitud de una línea con solo dos decimales
    return round(math.dist(punto1, punto2), 2)

# Helper Functions
def print_entity(e):
    print("Entity Type:", e.dxftype())
    print("Layer:", e.dxf.layer)
    print("Color:", e.dxf.color)
    print("Linetype:", e.dxf.linetype)
    print("Handle:", e.dxf.handle)

    primera_dimension_procesad = False
    primera_dimension_procesada = False

    if e.dxftype() == 'LWPOLYLINE': 
        for e in msp.query('LWPOLYLINE'):
            if not primera_dimension_procesad:
                print(f"LWPOLYLINE Type: {e.dxftype()}")
                # Imprime todos los atributos disponibles
                for attrib_name in e.dxfattribs():
                    print(f"{attrib_name}: {e.get_dxf_attrib(attrib_name, default=None)}")
                print("\n")
                
                # Cambia la bandera para indicar que la primera dimensión ha sido procesada
                primera_dimension_procesad = True
    elif e.dxftype() == 'DIMENSION':
        for e in msp.query('DIMENSION'):
            if not primera_dimension_procesada:
                print(f"Dimension Type: {e.dxftype()}")
                # Imprime todos los atributos disponibles
                for attrib_name in e.dxfattribs():
                    print(f"{attrib_name}: {e.get_dxf_attrib(attrib_name, default=None)}")
                print("\n")
                
                # Cambia la bandera para indicar que la primera dimensión ha sido procesada
                primera_dimension_procesada = True


    print("\n")

if __name__ == "__main__":
    archivo_dxf = "REFPA.dxf"  # Nombre de archivo específico

    try:
        doc = ezdxf.readfile(archivo_dxf)
        msp = doc.modelspace()

        for e in msp:
            print (e)
            print_entity(e)

    except Exception as e:
        print("Error:", str(e))
