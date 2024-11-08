import ezdxf
import math


# Helper Functions
def print_entity(e):
    print("Entity Type:", e.dxftype())
    print("Layer:", e.dxf.layer)
    print("Color:", e.dxf.color)
    print("Linetype:", e.dxf.linetype)
    print("Handle:", e.dxf.handle)

    if e.dxftype() == 'DIMENSION':
        print("Insert Point:", e.get_dxf_attrib("insert", default=None))
        print("Text Midpoint:", e.get_dxf_attrib("text_midpoint", default=None))
        print("defpoint:", e.get_dxf_attrib("defpoint", default=None))
        print("Actual Measurement:", e.get_dxf_attrib("actual_measurement", default=None))
        print("defpoint2:", e.get_dxf_attrib("defpoint2", default=None))
        print("defpoint3:", e.get_dxf_attrib("defpoint3", default=None))


    print("\n")

if __name__ == "__main__":
    archivo_dxf = "REFPA.dxf"  # Nombre de archivo específico

    try:
        doc = ezdxf.readfile(archivo_dxf)
        msp = doc.modelspace()

        for e in msp:
            print_entity(e)

    except Exception as e:
        print("Error:", str(e))
