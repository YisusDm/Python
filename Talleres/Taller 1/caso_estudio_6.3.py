opcion = int
num = [str() for ind0 in range(1000)]
cant = 0
while opcion != 5:
	print("")
	print("Bienvenido a la tienda.")
	print("1. Insetar Producto")
	print("2. Ver Todos")
	print("3. Actualizar")
	print("4. Eliminar")
	print("5. Salir")
	opcion = int(input("Elige: "))
	if opcion==1:
		cant = cant+1
		print("")
		nuevoproducto = input("Ingresa el nuevo producto: ")
		num[cant-1] = nuevoproducto
	elif opcion==2:
		if cant>0:
			print("")
			print("Lista de productos")
			for i in range(1,cant+1):
				print(str(i)+".",num[i-1])
			print("")
		input("Presiona ENTER para volver al menu")
	elif opcion==3:
		print("")
		idproducto = int(input("Ingresa el numero del producto a actulizar: "))
		if idproducto>0 and idproducto<=cant:
			print("El producto a actualiza es: ",num[idproducto-1])
			continuar = input("Escriba SI si es el producto, si no lo es, escriba NO: ")
			if continuar=="SI":
				nuevonombre = input("Ingrese el nuevo nombre: ")
				num[idproducto-1] = nuevonombre
	elif opcion==4:
		print("")
		idproducto = int(input("Ingresa el numero del producto a eliminar: "))
		#np.delete(num, (idproducto))
		del num[idproducto-1]
		cant = cant - 1
	else:
		print()
		input("Presione ENTER para salir") 