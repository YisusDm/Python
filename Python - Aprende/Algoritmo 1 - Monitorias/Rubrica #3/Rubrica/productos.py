
def to_dict(id, nombre, cantidad, precio_unitario): # funcion para setear variables en el diccionario
    return {
        "Id":id,
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio_unitario
    }    


def ingresar_producto(productos): # Función para ingresar productos al inventario
    id = len(productos)+1    
    while True:
        nombre = input(f"Ingrese el nombre del producto ID ({id}): ")
        if nombre ==  "" or nombre == None:
            print("Ingrese un nombre de producto valido.")
        else:
            break
    
    while True:
        cantidad = int(input(f"Digite la cantidad de {nombre}: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
        else:
            break

    while True:
        precio_unitario = float(input(f"Ingrese el precio de {nombre} ($): "))
        if precio_unitario < 0:
            print("El precio unitario no puede ser negativo.")
        else:
            break

    # se arma la estructura del diccionario y agrega el producto
    producto = to_dict(id, nombre, cantidad, precio_unitario)

    print(f"Producto {nombre} registrado con éxito.")

    return producto

def mostrar_inventario(inventario): # Función para mostrar el inventario
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario de productos:")
        for producto in inventario:
            total = producto["cantidad"]*producto["precio"]
            print(f"ID: {producto["Id"]}, Nombre: {producto["nombre"]}, "
                  f"Cantidad: {producto["cantidad"]}, Precio Unitario: {producto["precio"]:.2f}, "
                  f"Valor Total: {total:.2f}")

def buscar_producto_por_id(inventario): # Función para buscar un producto por su ID
    id_buscar = int(input("Introduce el ID del producto a buscar: "))
    n=0
    for producto in inventario:
        if producto["Id"] == id_buscar:
            total = producto["cantidad"]*producto["precio"]
            print(f"ID: {producto["Id"]}, Nombre: {producto["nombre"]}, "
                f"Cantidad: {producto["cantidad"]}, Precio Unitario: {producto["precio"]:.2f}, "
                f"Valor Total: {total:.2f}")
        else:
            n += 1
    if n != 0:
        print(f"No se encontró un producto con el ID {id_buscar} en la bodega.")        

# Función principal para manejar el menú de opciones
def menu():
    Bodega = [{'Id': 1, 'nombre': 'alcohol', 'cantidad': 10, 'precio': 2800.0}, {'Id': 2, 'nombre': 'galletas', 'cantidad': 18, 'precio': 800.0}] 

    while True:
        print("\nMenú de opciones:")
        print("1. Ingresar productos.")
        print("2. Mostrar inventario.")
        print("3. Buscar producto por ID.")
        print("4. Salir.")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            Producto = ingresar_producto(Bodega)
            Bodega.append(Producto)
        elif opcion == '2':
            mostrar_inventario(Bodega)
        elif opcion == '3':
            buscar_producto_por_id(Bodega)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor selecciona una opción entre 1 y 4.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()