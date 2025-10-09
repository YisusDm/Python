# Diccionario de tuplas, grafo dirigido y ponderado
# DFS Iterativo (usando Pila)
class Grafo:
    def __init__(self):
        self.grafo = {}  # Diccionario donde las claves son los nodos y los valores son listas de tuplas (nodo, peso)

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, origen, destino, peso):
        if origen in self.grafo and destino in self.grafo:
            self.grafo[origen].append((destino, peso))  # Solo dirección origen -> destino

    def mostrar_grafo(self):
        for nodo in self.grafo:
            print(f"{nodo} : {self.grafo[nodo]}")

    def dfs(self, inicio):
        visitados = set()  # Conjunto de nodos visitados
        pila = [inicio]    # Pila para almacenar los nodos por visitar

        print("\nRecorrido DFS:")
        while pila:
            nodo = pila.pop()  # Extrae el último nodo agregado
            if nodo not in visitados:
                print(nodo, end=" → ")  # Imprime el nodo visitado
                visitados.add(nodo)
                # Agrega los nodos adyacentes a la pila (sin repetir)
                for vecino, _ in self.grafo[nodo]:
                    if vecino not in visitados:
                        pila.append(vecino)
        print("Fin")

# Crear el grafo dirigido y ponderado
grafo = Grafo()

# Agregar nodos
nodos = ["A", "B", "C", "D", "E"]
for nodo in nodos:
    grafo.agregar_nodo(nodo)

# Agregar aristas con peso
grafo.agregar_arista("A", "B", 2)
grafo.agregar_arista("A", "C", 4)
grafo.agregar_arista("B", "D", 7)
grafo.agregar_arista("C", "D", 1)
grafo.agregar_arista("D", "E", 3)

# Mostrar el grafo
print("Grafo dirigido y ponderado:")
grafo.mostrar_grafo()

# Ejecutar DFS desde el nodo "A"
grafo.dfs("A")