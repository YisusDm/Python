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
        lugares = self.ciudad.obtener_lugares_interes()
        print("📍 Sitios de interés disponibles:")
        for i, lugar in enumerate(lugares):
            print(f"{i}. {lugar}")

        inicio = self._leer_indice("Seleccione el número del lugar de partida: ", lugares)
        destino = self._leer_indice("Seleccione el número del lugar de destino: ", lugares)

        if inicio == destino:
            print("⚠️ La ubicación de partida y destino no pueden ser iguales.")
            return

        origen = lugares[inicio]
        destino = lugares[destino]
        camino, distancia = self.ruta.dijkstra(origen, destino)

        if not camino:
            print("❌ No se encontró una ruta entre los puntos ingresados.")
            return

        self._mostrar_direccion(camino)
        print(f"📏 Distancia total: {distancia} km")
        self._graficar(camino)

    def _leer_indice(self, mensaje, lista):
        while True:
            try:
                entrada = int(input(mensaje).strip())
                if 0 <= entrada < len(lista):
                    return entrada
                else:
                    print("⚠️ Índice fuera de rango.")
            except ValueError:
                print("⚠️ Entrada inválida. Debe ser un número entero.")

    def _mostrar_direccion(self, camino):
        print(f"\n🚩 {camino[0]}")
        pasos = camino[1:-1]
        actual_direccion = ""
        acumulado = []
        for i in range(1, len(camino) - 1):
            ant = camino[i - 1]
            act = camino[i]
            sig = camino[i + 1]

            dir_ant = self._direccion(ant, act)
            dir_sig = self._direccion(act, sig)

            if dir_ant == dir_sig:
                acumulado.append(act)
            else:
                acumulado.append(act)
                self._imprimir_segmento(dir_ant, acumulado)
                acumulado = []

        if acumulado:
            self._imprimir_segmento(self._direccion(camino[-3], camino[-2]), acumulado)

        print(f"🏁 Ha llegado a su destino: {camino[-1]}\n")

    def _direccion(self, origen, destino):
        if "Calle" in origen and "Carrera" in origen and "Calle" in destino and "Carrera" in destino:
            c1, r1 = [int(x) for x in origen.replace("Calle ", "").replace("Carrera ", "").split(" con ")]
            c2, r2 = [int(x) for x in destino.replace("Calle ", "").replace("Carrera ", "").split(" con ")]
            if c1 == c2 and r2 > r1:
                return "→ derecha"
            elif c1 == c2 and r2 < r1:
                return "← izquierda"
            elif r1 == r2 and c2 > c1:
                return "↓ bajando"
            elif r1 == r2 and c2 < c1:
                return "↑ subiendo"
        return "desconocido"

    def _imprimir_segmento(self, direccion, pasos):
        flecha = {
            "→ derecha": "🔁  Gire a la derecha",
            "← izquierda": "↩️  Gire a la izquierda",
            "↓ bajando": "🛣️  Tome la calle hacia el sur",
            "↑ subiendo": "🛣️  Tome la calle hacia el norte",
            "desconocido": "➤  Continúe"
        }
        print(f"   {flecha.get(direccion, '➤  Continúe')} por {len(pasos)} km:")
        for p in pasos:
            print(f"      → {p}")

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

        colores = ["red" if nodo in ruta_destacada else
                   "orange" if nodo in lugares_reales else "skyblue" for nodo in G.nodes()]
        tamaños = [1000 if nodo in lugares_reales else 500 for nodo in G.nodes()]

        plt.figure(figsize=(16, 12))
        nx.draw(G, pos, with_labels=False, node_size=tamaños, node_color=colores)
        for nodo in lugares_reales:
            x, y = pos[nodo]
            plt.text(x + 0.1, y + 0.1, nodo, fontsize=9, color='black', weight='bold')

        if ruta_destacada:
            edges_en_ruta = list(zip(ruta_destacada, ruta_destacada[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=edges_en_ruta, edge_color='red', width=4)

        ax = plt.gca()
        ax.set_xticks(range(1, 9))
        ax.set_yticks(range(1, 9))
        ax.set_xticklabels([f"Carrera {i}" for i in range(1, 9)])
        ax.set_yticklabels([f"Calle {9 - i}" for i in range(1, 9)])
        ax.tick_params(axis='both', which='both', length=0)

        plt.grid(True, linestyle="--", linewidth=0.5)
        plt.title("🗺️ Ciudad con navegación paso a paso", fontsize=16)
        plt.axis("on")
        plt.show()

if __name__ == "__main__":
    try:
        ruta_json = "conexiones.json"
        app = InterfazConsola(ruta_json)
        app.iniciar()
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
