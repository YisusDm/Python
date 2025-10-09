# grafo dirigido y ponderado
grafo = {
    "A" : [("B", 5)],
    "B" : [("C", 10)],
    "C" : []
}
print(grafo)

# Cambiar el peso de A → B de 5 a 8
grafo['A'].remove(('B', 5))  # Se elimina la arista antigua
grafo['A'].append(('B', 8))  # Se Agrega la nueva arista

print(grafo)