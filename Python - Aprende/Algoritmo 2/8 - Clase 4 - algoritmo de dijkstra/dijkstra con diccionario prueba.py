import heapq  # Para usar una cola de prioridad eficiente

def dijkstra(grafo, inicio):
    # Inicializar distancias infinitas y distancia al nodo inicial = 0
    print("nodo desde el cual queremos calcular las distancias mas cortas")
    print(inicio)
    distancias = {nodo: float('inf') for nodo in grafo}
    print("\nse crea dicc distancias se inicializan las dist en inf")
    print(f"distancias = {distancias}")
    distancias[inicio] = 0
    print("\nla distancia del nodo de inicio a si mismo es 0")
    print(f"distancias = {distancias}")
    
    # Cola de prioridad con tupla para almacenar los nodos por menor distancia
    cola_prioridad = [(0, inicio)] # (distancia, nodo)
    print("\ncola de prioridad con tuplas")
    print(f"cola_prioridad = {cola_prioridad}")

    i=1
    while cola_prioridad:
        print(f"\niteracion {i} del while:")
        i=i+1
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad) # Extrae de la cola el nodo con la menor distancia conocida
        print("\nextrae la cola del nodo con la menor distancia conocida")
        print("distancia_actual ", distancia_actual)
        print("nodo_actual ", nodo_actual)

        print(f"si {distancia_actual} > {distancias[nodo_actual]}")
        if distancia_actual > distancias[nodo_actual]:
            print("     continua a la siguiente iteracion")
            print("------------------------------------------------------")
            continue  # Ya encontramos un camino más corto, continua con la siguiente iteracion
        else:
            print("     no salta a la siguiente iter porque no es mayor")
        
        print(f"para cada vecino, peso que esta en {nodo_actual}: {grafo[nodo_actual]}")
        j = 1
        for vecino, peso in grafo[nodo_actual]: # Itera sobre todos los vecinos del nodo actual
            print(f"iteracion {j} del ciclo for")
            print(f"hallar la distancia entre {nodo_actual} y {vecino}")
            j=j+1
            distancia = distancia_actual + peso
            print(f"    distancia = {distancia}")
            print(f"    si {distancia} < {distancias[vecino]}")
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                print(f"        actualizo el dicc distancias")
                print(f"        {distancias}")
                heapq.heappush(cola_prioridad, (distancia, vecino))
                print("         agregamos el vecino a la cola de prioridad")
                print("         para que sus vecino sean explorados")
                print(f"         cola_prioridad = {cola_prioridad}")
        print("------------------------------------------------------")

    print("\nla cola_prioridad esta vacia, sale del while")
    return distancias

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

resultado = dijkstra(grafo, 'A')
print("Distancias más cortas desde A:")
for nodo, distancia in resultado.items():
    print(f"{nodo}: {distancia}")