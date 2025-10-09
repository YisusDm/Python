# Creamos grafo, diccionario de listas
grafo = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': ['C']
}

# Mostramos el grafo
print("grafo original:", end = "\n")
print(grafo)

# Agregamos nodo y arista
print("\nagregando nodo E y conexion con A")
grafo['E'] = [] # Agregamos el nodo E sin aristas (clave del diccionario)
grafo['E'].append('A') # Agregando la arista de E a A, (lista de adyacencia)
print(grafo)

# Modificamos una arista
print("\nModificando conexion del nodo A")
if 'B' in grafo['A']: # Si el valor B esta dentro de la lista de adyacencia de A
    grafo['A'].remove('B') # Eliminamos el enlace actual
grafo['A'].append('D') # Agregamos el nuevo enlace hacia otro nodo
print(grafo)

# Eliminando un nodo, quitamos la clave del diccionario
# Y eliminamos todas las referencias a ese nodo en las listas de adyacencia
print("\neliminando el nodo D")
if 'D' in grafo: # Si la clave D esta dentro del grafo
    del grafo['D'] # Eliminamos el nodo
for nodo in grafo: # Para cada nodo (clave) que esta dentro del grafo, recorre todos los nodos
    if 'D' in grafo[nodo]: # Si D esta dentro de la lista de adyacencia de cada nodo
        grafo[nodo].remove('D') # Elimino el elemento de la lista
print(grafo)

# Eliminamos una arista entre dos nodos
print("\neliminando conexion entre A y C")
if 'C' in grafo['A']: # si la valor C esta dentro de la clave A
    grafo['A'].remove('C')
print(grafo)

# Asi buscamos si existe una arista o un nodo

# Verificamos si existe el nodo 'B'
print('B' in grafo)  # Devuelve True

# Verificamos si existe una arista entre 'A' y 'D'
print('D' in grafo['A'])  # Devuelve False