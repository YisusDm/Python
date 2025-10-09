# Representamos la red de vuelos como un grafo dirigido y ponderado
# Usamos un diccionario de adyacencia para facilitar las operaciones

grafo_vuelos = {
    "Bogotá": {"Medellín": 415, "Cali": 300, "Cartagena": 700},
    "Medellín": {"Cartagena": 600},
    "Cartagena": {"Cali": 800},
    "Cali": {}  # Cali no tiene vuelos salientes en los datos iniciales
}

# Funciones del sistema

def mostrar_conexiones():
    # Recorre el grafo y muestra las conexiones directas
    print("\nConexiones directas entre ciudades:")
    for origen in grafo_vuelos:
        for destino in grafo_vuelos[origen]:
            print(f"{origen} → {destino} ({grafo_vuelos[origen][destino]} km)")

def distancia_directa(origen, destino):
    # Muestra la distancia entre dos ciudades si hay una ruta directa
    if origen in grafo_vuelos and destino in grafo_vuelos[origen]:
        print(f"\nDistancia entre {origen} y {destino}: {grafo_vuelos[origen][destino]} km")
    else:
        print(f"\nNo hay vuelo directo entre {origen} y {destino}.")

def agregar_ruta(origen, destino, distancia):
    # Añade una nueva ruta entre ciudades existentes
    if origen in grafo_vuelos:
        grafo_vuelos[origen][destino] = distancia
    else:
        grafo_vuelos[origen] = {destino: distancia}
    print(f"\nRuta agregada: {origen} → {destino} ({distancia} km)")

def eliminar_ruta(origen, destino):
    # Elimina una ruta si existe
    if origen in grafo_vuelos and destino in grafo_vuelos[origen]:
        del grafo_vuelos[origen][destino]
        print(f"\nRuta eliminada: {origen} → {destino}")
    else:
        print(f"\nNo existe una ruta directa entre {origen} y {destino} para eliminar.")

# Pruebas del sistema
mostrar_conexiones()
distancia_directa("Bogotá", "Medellín")
agregar_ruta("Medellín", "Barranquilla", 750)
mostrar_conexiones()
eliminar_ruta("Bogotá", "Cali")
mostrar_conexiones()

# Comentario final:
# Escogí la representación de diccionario de adyacencia porque permite:
# - Fácil acceso a vecinos (conexiones directas)
# - Operaciones de agregar/eliminar rutas eficientes
# - Almacenar pesos directamente (distancias)
