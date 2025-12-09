# Lista inicial con los elementos desordenados
lista = [5, 2, 8, 4, 9, 1, 3, 6]
print("Lista original:", lista)

def ordenar_burbuja(lista): # Definición de la función de ordenamiento Burbuja

    for i in range(len(lista)): # Primer bucle recorre cada elemento de la lista
        for j in range(len(lista) - 1): # Segundo bucle compara elementos adyacentes         
            if lista[j] > lista[j + 1]:  # Si el elemento actual es mayor que el siguiente, intercambiamos
                print("Elemento mayor encontrado:", lista[j])
        
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Intercambiamos los elementos si están en el orden incorrecto
                
                print("Elemento después del intercambio:", lista[j]) # Mostramos el valor que fue intercambiado

ordenar_burbuja(lista) # Llamamos a la función para ordenar la lista

print("Lista ordenada:", lista) # Imprimimos la lista ordenada



# Parte izquierda (lista[j], lista[j + 1]): 
# Esta es la lista de variables que recibirán los nuevos valores después del intercambio.

# Parte derecha (lista[j + 1], lista[j]): 
# Son los valores que se intercambian. Primero toma el valor de lista[j + 1] y lo asigna a lista[j], luego toma el valor de lista[j] y lo asigna a lista[j + 1].
