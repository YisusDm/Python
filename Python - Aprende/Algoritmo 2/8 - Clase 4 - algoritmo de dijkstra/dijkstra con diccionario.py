import heapq  # Para usar una cola de prioridad eficiente

def dijkstra(grafo, inicio):
    # Inicializar distancias infinitas y distancia al nodo inicial = 0
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    
    # Cola de prioridad con tupla para almacenar los nodos por menor distancia
    cola_prioridad = [(0, inicio)] # (distancia, nodo)

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad) # Extrae de la cola el nodo con la menor distancia conocida

        if distancia_actual > distancias[nodo_actual]:
            continue  # Ya encontramos un camino más corto, continua con la siguiente iteracion

        for vecino, peso in grafo[nodo_actual]: # Itera sobre todos los vecinos del nodo actual
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))

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