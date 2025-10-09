# Grafo no ponderado
# BFS Usando Cola (queue.Queue)
# Importa la clase deque desde el módulo collections de Python
from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])  # Cola FIFO
    
    #print("cola: ", cola)

    while cola:
        nodo = cola.popleft()  # Extraemos el primer nodo
        if nodo not in visitados:
            print(nodo, end=" → ")  # Procesamos el nodo
            visitados.add(nodo)
            cola.extend(grafo[nodo])  # Agregamos vecinos a la cola
            #extend() agrega nodos a la cola para ser procesados en el futuro.
            
            #print("\nvisitados: ", visitados)
            #print("cola: ", cola)

# Definimos un grafo no dirigido
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

print("Recorrido BFS:")
bfs(grafo, "A")