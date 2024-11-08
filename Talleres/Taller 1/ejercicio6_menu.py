productos = [1,"2",3,4]
print(productos[1])
print(productos[3])
suma=productos[1]+productos[3]
print(suma)

opcion=0



while (opcion!=5):
    print ('''  Menu de la tienda:   
            1) Insertar
            2) Ver todos
            3) Actualizar
            4) Eliminar
            5) Salir  ''' )
    opcion=int(input("Selecione su opcion: "))
    if (opcion==1):
        n=int(input("Cuantos productos desea agregar: "))
        for i in range (n):
            nprod=input("Inserte el nombre del producto a agregar: ")
            productos.append(nprod)
    elif (opcion==2):
        print(f"Los productos de su lista son: {productos}")
    elif (opcion==3):
         print(f"La lista actualizada es {productos}")
    elif (opcion==4):
        eliminar=input("Indique el producto a eliminar: ")
        productos.remove(eliminar)
        print(f"Se ha elminado '{eliminar}' de su lista")
    elif (opcion==5):
        print ("Gracias por usar el programa")