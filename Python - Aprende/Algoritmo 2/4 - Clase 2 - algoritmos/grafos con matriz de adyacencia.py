# Funcion mostrar matriz
def mostrarMatriz():
    for fila in grafo:
        print(fila)

# Lista de nodos = A, B, C, D
nodos = ['A', 'B', 'C', 'D']

# Se Crea la matriz de adyacencia inicial (sin conexiones, es decir todas la celdas en 0)
n = len(nodos) # n es la cantidad de nodos que estan en la lista llamada nodos
grafo = [[0] * n for _ in range(n)] # Crea una nueva matriz cuadrada de tamaño n x n, inicializada con ceros

# Define conexiones iniciales:
# Como la matriz se inicializa en 0, solo se establecen las conexiones existentes
# A → B, B → C, C → A, D → C
grafo[0][1] = 1  # A → B
grafo[1][2] = 1  # B → C
grafo[2][0] = 1  # C → A
grafo[3][2] = 1  # D → C

# Muestra la matriz de adyacencia
mostrarMatriz()

# Agrega una arista de A → D
grafo[0][3] = 1

# Muestra la matriz de adyacencia
print("\n modificando conexion de A -> D")
mostrarMatriz()

# Eliminamos la arista de A → B
grafo[0][1] = 0

# Muestra la matriz de adyacencia
print("\n modificando conexion de A -> B")
mostrarMatriz()

# Agregamos un nodo nuevo, se redimensiona la matriz
nodos.append('E') # Agregamos nodo E, agregando elemento E en la lista nodos

# Ampliamos la matriz, aumento n en 1 porque es un solo nodo el que voy a crear
# Tambien podria volver a calcular el tamaño de la lista nodo asi: n = len(nodos)
n += 1
for fila in grafo: # Ciclo que recorre cada fila de la matriz del grafo y agrega la nueva columna "E"
    fila.append(0)  # Agrega la celda de la nueva columna

# Agrega nueva fila con todas sus columnas en 0
grafo.append([0] * n)

# Muestra la matriz actualizada
print("\n agregando nodo a matriz")
for fila in grafo:
    print(fila)