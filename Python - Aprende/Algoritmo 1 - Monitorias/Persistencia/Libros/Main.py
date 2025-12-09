import os
import json

class Libros:
    def __init__(self, titulo, autor, año):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = año

    def to_dict(self):
        """Convierte la instancia de libros a un diccionario."""
        return {
            "titulo": self.__titulo,
            "autor": self.__autor,
            "anio": self.__año
        }
    
class GestorBiblioteca:

    def __init__(self, archivo='biblioteca.json'):
        self.archivo = archivo
        self.libros = self.cargar_Libros()

    def cargar_Libros(self): # Reader
        """Carga los libros desde el archivo si existe, de lo contrario retorna una lista vacía."""
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            print(f"Nota: El archivo '{self.archivo}' no existe. Retornando lista vacía.")
        return []

    def agregar_libros(self, libro): # Create
        """Agrega un nuevo libro y guarda los cambios en el archivo."""
        self.libros.append(libro.to_dict()) 
        self.guardar_libros()

    def guardar_libros(self):
        """Guarda la lista de libros en el archivo."""
        with open(self.archivo, 'w', encoding='utf-8') as file:
            json.dump(self.libros, file)

    def mostrar_libros(self):# Reader
        """Muestra todos los libros almacenados."""
        if self.libros == [] or len(self.libros) == 0:
            print("No hay informacion de libros disponible.")
        else:     
            for libro in self.libros:
                print(f"Titulo: {libro['titulo']}, Autor: {libro['autor']}, "
                    f"Año: {libro['anio']}")    

    def obtener_libros(self):
        list = []
        for libro in self.libros:
            titulo = libro['titulo']   
            list.append(titulo)
        
        return list



# Uso del script
if __name__ == "__main__":

    gestor = GestorBiblioteca()

    while True:
        print("\n--- Gestión de libros ---")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            swich = True
            while swich == True:
                lsLibros = gestor.obtener_libros()
                out_titulo = input("titulo: ")
                if out_titulo in lsLibros:
                    print("El libro ya se encuentra en la biblioteca. \nIntente con otro libro")
                else:  
                    titulo = out_titulo 
                    swich = False   

            autor = input("autor: ")
            año = int(input("año: "))

            libros = Libros(titulo, autor, año)
            gestor.agregar_libros(libros)

            print("libro agregado exitosamente.")

        elif opcion == "2":
            print("\nlibros registrados:")
            gestor.mostrar_libros()

        elif opcion == "3":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")



