
class Nodo:
    """Nodo de la pila que almacena cada palabra del texto."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    """Implementación de una pila dinámica."""
    def __init__(self):
        self.tope = None

    def push(self, dato):
        """Inserta un elemento en la pila."""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def pop(self):
        """Elimina y retorna el elemento en el tope de la pila."""
        if self.esta_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return self.tope is None

    def mostrar_pila(self):
        """Muestra el contenido actual de la pila."""
        actual = self.tope
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        print("Texto actual: " + " ".join(reversed(elementos)))

class EditorTexto:
    """Simula un editor de texto con funcionalidades de deshacer y rehacer."""
    def __init__(self):
        self.texto = Pila()  # Pila principal
        self.historial = Pila()  # Pila auxiliar para rehacer

    def escribir(self, frase):
        """Divide la frase en palabras y las agrega a la pila."""
        for palabra in frase.split():
            self.texto.push(palabra)
        self.historial = Pila()  # Se reinicia el historial al escribir
        self.texto.mostrar_pila()

    def deshacer(self):
        """Mueve la última palabra escrita a la pila de historial."""
        palabra = self.texto.pop()
        if palabra:
            self.historial.push(palabra)
            print(f"🔙 Deshacer: '{palabra}'")
        else:
            print("⚠ No hay más palabras para deshacer.")
        self.texto.mostrar_pila()

    def rehacer(self):
        """Mueve la última palabra eliminada de nuevo al texto."""
        palabra = self.historial.pop()
        if palabra:
            self.texto.push(palabra)
            print(f"↩ Rehacer: '{palabra}'")
        else:
            print("⚠ No hay más palabras para rehacer.")
        self.texto.mostrar_pila()

# Interfaz en consola
editor = EditorTexto()
while True:
    print("\n📌 Editor de Texto - Opciones:")
    print("1. Escribir una frase")
    print("2. Deshacer")
    print("3. Rehacer")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        frase = input("Escribe tu frase: ")
        editor.escribir(frase)
    elif opcion == "2":
        editor.deshacer()
    elif opcion == "3":
        editor.rehacer()
    elif opcion == "4":
        print("👋 Saliendo...")
        break
    else:
        print("⚠ Opción inválida, intenta nuevamente.")
