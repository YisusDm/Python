# diccionario de lista con grafos no dirigidos
grafo = {
    "A" : ["B", "C"],
    "B" : ["A", "C"],
    "C" : ["A", "B"]
}
print(grafo)

# diccionario de listas con grafos dirigidos
grafo2 = {
    "A" : ["B"],
    "B" : ["C"],
    "C" : []
}
print(grafo2)

# diccionario de tuplas con grafos ponderados
grafo3 = {
    "A" : [("B", 5)],
    "B" : [("C", 10)],
    "C" : []
}
print(grafo3)

# matriz de adyacencia
grafo4 = [
    [0,1,0],
    [0,0,1],
    [0,0,0]
]

for fila in range(len(grafo4)):
    print(grafo4[fila])
