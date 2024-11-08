opcion = int
producto = []
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
	if opcion <= 5:
		if opcion==1:
			print("")
			nuevoproducto = input("Ingresa el nuevo producto: ")
			producto.append(nuevoproducto)
			cant = cant + 1
		elif opcion==2:
			if cant>0:
				print("")
				print("Lista de productos")
				for i in range(1,cant+1):
					print(str(i)+".",producto[i-1])
				print("")
			input("Presiona ENTER para volver al menu")
		elif opcion==3:
			print("")
			idproducto = int(input("Ingresa el numero del producto a actulizar: "))
			if idproducto>0 and idproducto<=cant:
				print("El producto a actualiza es: ",producto[idproducto-1])
				continuar = input("Escriba SI si es el producto, si no lo es, escriba NO: ")
				if continuar=="SI":
					nuevonombre = input("Ingrese el nuevo nombre: ")
					producto[idproducto-1] = nuevonombre
		elif opcion==4:
			print("")
			idproducto = int(input("Ingresa el numero del producto a eliminar: "))
			if idproducto>0 and idproducto<=cant:
				print("El producto a eliminar es: ",producto[idproducto-1])
				continuar = input("Escriba SI si esta seguro, de lo contrario, escriba NO: ")
				if continuar=="SI":
					del producto[idproducto-1]
					cant = cant - 1
		else:
			print()
			input("Presione ENTER para salir") 
	else:
		print('''
¡Las opciones a escoger es entre 1 y 5! ''')