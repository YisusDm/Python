# Grafo no ponderado
# BFS Usando Cola (queue.Queue)
# Importa la clase deque desde el módulo collections de Python
from collections import deque

def bfs_camino_corto(grafo, inicio, objetivo):
    visitados = set()
    cola = deque([(inicio, [inicio])])  # (Nodo actual, Ruta hasta el nodo)

    while cola:
        nodo, camino = cola.popleft()
        if nodo == objetivo:
            return camino  # Devuelve el camino más corto encontrado

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo[nodo]:
                cola.append((vecino, camino + [vecino]))  # Agrega el nuevo camino

    return None  # No hay camino

# Grafo no dirigido
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

print("Camino más corto de A a F:", bfs_camino_corto(grafo, "A", "F"))