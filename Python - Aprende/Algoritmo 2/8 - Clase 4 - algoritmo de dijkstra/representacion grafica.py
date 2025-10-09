import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido y ponderado
G = nx.DiGraph()
#G = nx.Graph() #para grafos no dirigidos

# Agregar nodos (opcionalmente, NetworkX los crea al agregar aristas)
nodos = ['A', 'B', 'C', 'D']
G.add_nodes_from(nodos)

# Agregar aristas con pesos (nodo_origen, nodo_destino, peso)
G.add_edge('A', 'B', weight=3)
G.add_edge('A', 'C', weight=1)
G.add_edge('B', 'C', weight=7)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=2)

# Posiciones de los nodos (para que se vea bonito)
# calcula las posiciones de los nodos del grafo G para que puedan ser dibujados visualmente de forma estética
pos = nx.spring_layout(G)

# Dibujar nodos y aristas
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=14, font_weight='bold', arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

# Mostrar el grafo
plt.title("Grafo Dirigido Ponderado")
plt.axis('off')
plt.show()