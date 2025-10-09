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
        print("nodo desde el cual queremos calcular las distancias mas cortas")
        print(inicio)
        distancias = {nodo: float('inf') for nodo in self.grafo}
        print("\nse crea dicc distancias se inicializan las dist en inf")
        print(f"distancias = {distancias}")
        distancias[inicio] = 0
        print("\nla distancia del nodo de inicio a si mismo es 0")
        print(f"distancias = {distancias}")

        caminos = {nodo: [] for nodo in self.grafo}
        caminos[inicio] = [inicio]
        print("\ninicializamos caminos")
        print(f"caminos = {caminos}")

        cola_prioridad = [(0, inicio)]
        print("\ncola de prioridad con tuplas")
        print(f"cola_prioridad = {cola_prioridad}")

        i=1
        while cola_prioridad:
            print(f"\niteracion {i} del while:")
            i=i+1
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
            print("\nextrae la cola del nodo con la menor distancia conocida")
            print("distancia_actual ", distancia_actual)
            print("nodo_actual ", nodo_actual)

            print(f"para cada vecino, peso que esta en {nodo_actual}: {self.grafo[nodo_actual]}")
            j = 1
            for vecino, peso in self.grafo[nodo_actual]:
                print(f"iteracion {j} del ciclo for")
                print(f"hallar la distancia entre {nodo_actual} y {vecino}")
                j=j+1
                nueva_distancia = distancia_actual + peso
                print(f"    nueva_distancia = {nueva_distancia}")
                print(f"    si {nueva_distancia} < {distancias[vecino]}")
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    print(f"         actualizo el dicc distancias")
                    print(f"         {distancias}")
                    caminos[vecino] = caminos[nodo_actual] + [vecino]
                    print("         actualizamos caminos")
                    print(f"         vecino = {vecino}")
                    print(f"         caminos[{vecino}] = {caminos[nodo_actual]} + {[vecino]}")
                    print(f"         caminos = {caminos}")
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
                    print("         agregamos el vecino a la cola de prioridad")
                    print("         para que sus vecinos sean explorados")
                    print(f"         cola_prioridad = {cola_prioridad}")
            print("------------------------------------------------------")

        print("\nla cola_prioridad esta vacia, sale del while")
        return distancias, caminos

g = Grafo()
g.agregar_arista('A', 'B', 2)
g.agregar_arista('A', 'C', 5)
g.agregar_arista('B', 'C', 1)
g.agregar_arista('B', 'D', 3)
g.agregar_arista('C', 'D', 2)
g.agregar_arista('D', 'E', 1)

distancias, caminos = g.dijkstra('A')

print("\nDistancias mínimas desde A:")
for nodo, distancia in distancias.items():
    print(f"{nodo}: {distancia}")

print("\nCaminos desde A:")
for nodo, camino in caminos.items():
    print(f"{nodo}: {' → '.join(camino)}")