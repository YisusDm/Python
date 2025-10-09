# definicion de clases, con listas de adyacencia
class Grafo:
    def __init__(self):
        self.grafo = {}

    # agregamos nuevo nodo (clave del diccionario) con lista adyacente vacia
    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []
        else:
            print("nodo existente")
 
    # agregamos enlaces entre nodos existentes
    def agregar_enlace(self, origen, destino):
        if origen in self.grafo and destino in self.grafo:
            self.grafo[origen].append(destino)
            
    # eliminamos una arista entre dos nodos
    def eliminar_arista(self, nodo1, nodo2):
        if nodo1 in self.grafo and nodo2 in self.grafo:
            self.grafo[nodo1].remove(nodo2)
 
    # muestra el grafo
    def mostrar_grafo(self):
        for nodo in self.grafo:
            print(nodo, ":", self.grafo[nodo])
            
mi_grafo = Grafo()
mi_grafo.agregar_nodo("A")
mi_grafo.agregar_nodo("B")
mi_grafo.agregar_nodo("C")
mi_grafo.agregar_nodo("D")

mi_grafo.agregar_enlace("A", "B")
mi_grafo.agregar_enlace("B", "C")
mi_grafo.agregar_enlace("A", "C")
mi_grafo.agregar_enlace("B", "D")
mi_grafo.mostrar_grafo()

mi_grafo.eliminar_arista("B", "D")
mi_grafo.mostrar_grafo()