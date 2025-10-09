import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}  # Diccionario: nodo -> lista de (vecino, peso)

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, origen, destino, peso):
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        self.grafo[origen].append((destino, peso))

    def dijkstra(self, inicio):
        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[inicio] = 0

        caminos = {nodo: [] for nodo in self.grafo}
        caminos[inicio] = [inicio]

        cola_prioridad = [(0, inicio)]

        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            for vecino, peso in self.grafo[nodo_actual]:
                nueva_distancia = distancia_actual + peso

                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    caminos[vecino] = caminos[nodo_actual] + [vecino]
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        return distancias, caminos

g = Grafo()
g.agregar_arista('A', 'B', 2)
g.agregar_arista('A', 'C', 5)
g.agregar_arista('B', 'C', 1)
g.agregar_arista('B', 'D', 3)
g.agregar_arista('C', 'D', 2)
g.agregar_arista('D', 'E', 1)

distancias, caminos = g.dijkstra('A')

print("Distancias mínimas desde A:")
for nodo, distancia in distancias.items():
    print(f"{nodo}: {distancia}")

print("\nCaminos desde A:")
for nodo, camino in caminos.items():
    print(f"{nodo}: {' → '.join(camino)}")