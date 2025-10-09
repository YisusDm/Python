import json
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class BaseDatosConexiones:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def cargar_conexiones(self):
        with open(self.ruta_archivo, 'r', encoding='utf-8') as f:
            return json.load(f)

class Ciudad:
    def __init__(self, conexiones):
        self.grafo = {}
        self._crear_grafo(conexiones)

    def _agregar_conexion(self, origen, destino, distancia):
        self.grafo.setdefault(origen, []).append((destino, distancia))
        self.grafo.setdefault(destino, []).append((origen, distancia))  # No dirigido

    def _crear_grafo(self, conexiones):
        for conexion in conexiones:
            self._agregar_conexion(conexion["origen"], conexion["destino"], conexion["distancia"])

    def obtener_vecinos(self, nodo):
        return self.grafo.get(nodo, [])

    def obtener_nodos(self):
        return list(self.grafo.keys())

    def obtener_lugares_interes(self):
        return [n for n in self.grafo if "Calle" not in n and "Carrera" not in n]

class RutaOptima:
    def __init__(self, ciudad):
        self.ciudad = ciudad

    def dijkstra(self, inicio, destino):
        distancias = {nodo: float('inf') for nodo in self.ciudad.obtener_nodos()}
        anteriores = {}
        distancias[inicio] = 0
        cola = [(0, inicio)]

        while cola:
            distancia_actual, nodo_actual = heapq.heappop(cola)

            if nodo_actual == destino:
                break

            for vecino, peso in self.ciudad.obtener_vecinos(nodo_actual):
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = nodo_actual
                    heapq.heappush(cola, (nueva_distancia, vecino))

        return self._reconstruir_camino(anteriores, inicio, destino), distancias[destino]

    def _reconstruir_camino(self, anteriores, inicio, destino):
        camino = []
        actual = destino
        while actual != inicio:
            camino.append(actual)
            actual = anteriores.get(actual)
            if actual is None:
                return []  # No se encontró camino
        camino.append(inicio)
        return camino[::-1]

class InterfazConsola:
    def __init__(self, ruta_json):
        self.basedatos = BaseDatosConexiones(ruta_json)
        conexiones = self.basedatos.cargar_conexiones()
        self.ciudad = Ciudad(conexiones)
        self.ruta = RutaOptima(self.ciudad)
        self.conexiones = conexiones

    def iniciar(self):
        print("🧭 Bienvenido al sistema de rutas óptimas en la ciudad inteligente 🏙️\n")
        print("📍 Sitios de interés disponibles:")
        for lugar in sorted(self.ciudad.obtener_lugares_interes()):
            print(f"- {lugar}")

        inicio = self._leer_ubicacion("Ingrese ubicación de partida: ")
        destino = self._leer_ubicacion("Ingrese destino: ")

        if inicio == destino:
            print("⚠️ La ubicación de partida y destino no pueden ser iguales.")
            return

        camino, distancia = self.ruta.dijkstra(inicio, destino)

        if not camino:
            print("❌ No se encontró una ruta entre los puntos ingresados.")
            return

        print("\n✅ Ruta más corta:")
        print(" → ".join(camino))
        print(f"📏 Distancia total: {distancia} km")

        self._graficar(camino)

    def _leer_ubicacion(self, mensaje):
        lugares = self.ciudad.obtener_lugares_interes()
        while True:
            entrada = input(mensaje).strip()
            if entrada in lugares:
                return entrada
            print("⚠️ Ubicación inválida. Por favor seleccione una de la lista.")

    def _graficar(self, ruta_destacada):
        G = nx.Graph()
        pos = {}
        lugares_reales = set()

        for conexion in self.conexiones:
            G.add_edge(conexion["origen"], conexion["destino"], weight=conexion["distancia"])

        for nodo in G.nodes():
            if "Calle" in nodo and "Carrera" in nodo:
                partes = nodo.replace("Calle ", "").replace("Carrera ", "").split(" con ")
                calle = int(partes[0])
                carrera = int(partes[1])
                pos[nodo] = (carrera, 9 - calle)
            else:
                lugares_reales.add(nodo)
                for conexion in self.conexiones:
                    if conexion["destino"] == nodo:
                        base = conexion["origen"]
                        if base in pos:
                            x, y = pos[base]
                            pos[nodo] = (x + 0.3, y + 0.3)

        colores = []
        for nodo in G.nodes():
            if nodo in ruta_destacada:
                colores.append("red")
            elif nodo in lugares_reales:
                colores.append("orange")
            else:
                colores.append("skyblue")

        tamaños = [1000 if nodo in lugares_reales else 500 for nodo in G.nodes()]

        plt.figure(figsize=(16, 12))
        nx.draw(G, pos, with_labels=True, node_size=tamaños, node_color=colores, font_size=8)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"))

        if ruta_destacada:
            edges_en_ruta = list(zip(ruta_destacada, ruta_destacada[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=edges_en_ruta, edge_color='red', width=4)

        # Añadir nombres de calles y carreras como ejes
        ax = plt.gca()
        ax.set_xticks(range(1, 9))
        ax.set_yticks(range(1, 9))
        ax.set_xticklabels([f"Carrera {i}" for i in range(1, 9)])
        ax.set_yticklabels([f"Calle {9 - i}" for i in range(1, 9)])
        ax.tick_params(axis='both', which='both', length=0)

        plt.title("🗺️ Ciudad inteligente con lugares destacados y ruta óptima", fontsize=16)
        plt.grid(True, linestyle="--", linewidth=0.5)
        plt.show()

if __name__ == "__main__":
    try:
        ruta_json = "conexiones.json"
        app = InterfazConsola(ruta_json)
        app.iniciar()
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
