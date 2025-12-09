# Lista de diccionarios
Productos = [
    {"producto": "Producto-A", "Adicional": ["Envase de vidrio", "Etiquetas de advertencia", "Sensor de Temperatura"]},
    {"producto": "Producto-B", "Adicional": ["Barriles de metal", "empaque sellado", "alarma de seguridad"]},
    {"producto": "Producto-C", "Adicional": ["Contenedores plasticos", "control de Humedad", "Camara de Frio"]}
]

def mostrar_productos():
    print("Lista de Productos:")
    for i, producto in enumerate(Productos):
        # Mostrar Producto con letra correspondiente A, B, C...
        print(f"{chr(65 + i)}. {producto['producto']}") #ASCII

    seleccionar_producto()    

def seleccionar_producto():
    while True:
        opcion2 = 0  # Variable para controlar la repetición del segundo menú
        opcion = input("Seleccione un producto (A, B, C): ").upper()

        if opcion in ['A', 'B', 'C']:
            indice = ord(opcion) - 65  # Convierte A=0, B=1, C=2
            producto_seleccionado = Productos[indice]
            
            print(f"\nDetalles del {producto_seleccionado['producto']}:")
            for j,adicional in enumerate(producto_seleccionado["Adicional"]):
                print(f"{j+1} - {adicional}")

            while opcion2 == 0:
                opcion2 = int(input("Selecciona un Adicional (1, 2, 3): "))    

                if opcion2 in [1, 2, 3]: 
                    print(f"\nEl producto seleccionado es {producto_seleccionado['producto']} y el adicional elegido es: {producto_seleccionado['Adicional'][opcion2-1]}")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione un número entre 1 y 3.")
                    opcion2 = 0  # Reinicia el controlador para volver a pedir una opción valida
        else:
            print("Opción no válida. Por favor, seleccione A, B o C.")

# Ejecución del programa
mostrar_productos()

