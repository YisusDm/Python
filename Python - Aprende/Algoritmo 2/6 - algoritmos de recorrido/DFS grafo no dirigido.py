# Diccionario de listas (grafo no ponderado)
# DFS Recursivo
def dfs(grafo, nodo, visitados):
    if nodo not in visitados:
        print(nodo, end=" ")  # Mostrar el nodo visitado
        visitados.add(nodo)   # Marcar el nodo como visitado
        for vecino in grafo[nodo]:
            dfs(grafo, vecino, visitados)

# Grafo de ejemplo (diccionario de listas)
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Conjunto para almacenar los nodos visitados
visitados = set()

print("Recorrido en profundidad (DFS):")
dfs(grafo, 'A', visitados)
