# JHINET ALEJANDRA BOHORQUEZ SARMIENTO
"""Diseña un programa en Python que gestione información sobre una biblioteca utilizando
persistencia en formato JSON. La aplicación debe ofrecer al usuario un menú interactivo con las
siguientes opciones:

1. Agregar Libro:
- Solicita al usuario ingresar el título, autor y año de publicación del libro.
- Verifica si el libro ya existe en la lista antes de agregarlo para evitar duplicados.
- Si no existe, crea un objeto de la clase Libro con esta información y lo agrega a la
lista de libros.
- Guarda la lista actualizada de libros en un archivo JSON llamado biblioteca.json.

2. Consultar Libros:
- Recupera la información desde el archivo JSON.
- Muestra detalles de todos los libros acumulados, incluyendo su título, autor y año
de publicación.
- Si no hay libros registrados, muestra un mensaje indicando que no hay información disponible.

3. Salir:
- Finaliza el programa.
   La clase Libro debe tener los siguientes métodos y atributos:
• Método __init__: Inicializa los atributos encapsulados __titulo, __autor y __anio.
• Método obtener_titulo: Retorna el título del libro.
• Método obtener_autor: Retorna el autor del libro.
• Método obtener_anio: Retorna el año de publicación del libro.

El archivo JSON debe contener una lista de diccionarios, donde cada diccionario representa la
información de un libro.
El programa debe utilizar un bucle que permita al usuario realizar múltiples operaciones hasta que
decida salir del programa."""

import json
import os

class Libro:
    def __init__(self, titulo, autor, año):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = año

    def obtener_titulo(self):
        return self.__titulo

    def obtener_autor(self):
        return self.__autor

    def obtener_año(self):
        return self.__año

    def convertir_a_diccionario(self):
        return {"titulo": self.obtener_titulo(),
            "autor": self.obtener_autor(),
            "anio": self.obtener_año()}

class Biblioteca:
    def __init__(self):
        self.__libros = []  
        # Recuperar libros desde el archivo JSON
        if os.path.exists("biblioteca.json"):
            with open("biblioteca.json", "r", encoding='utf-8') as archivo: # 'utf-8' Formato para lenguaje Latinoamerica 
                self.__libros = json.load(archivo)
        else:
            with open("biblioteca.json", "w") as archivo:
                json.dump([], archivo)
       
    def agregar_libro(self):
        print("📚 Agregar un nuevo libro a la biblioteca 📚")
        titulo = input("✏️ 📖 Ingrese el título del libro: ").title()
        autor = input("👨🏻‍💼 ✏️Ingrese el autor del libro: ").title()

        año = input("📅 Ingrese el año de publicación del libro: ")
        while not año.isdigit():
            print("⚠️ El año de publicación debe ser un número entero")
            año = input("📅 Ingrese el año de publicación del libro: ")
   
        for libroexisente in self.__libros:
            if libroexisente["titulo"].title() == titulo and libroexisente["autor"].title() == autor and libroexisente["año"] == año:
                print("⚠️ El libro ya existe en la biblioteca.")
                return

        nuevo_libro = Libro(titulo, autor, año)
        self.__libros.append(nuevo_libro.convertir_a_diccionario())
        print("Libro agregado con éxito ✅")

        with open("biblioteca.json", "w", encoding='utf-8') as archivo:
            json.dump(self.__libros, archivo)

    def consultar_libros(self):
        if not self.__libros:
            print("No hay libros registrados en la biblioteca.")
            return
        contador = 1
        print("🔍📚 Libros en la biblioteca:")
        for libro in self.__libros:
            print(f"{contador}. Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['anio']}")
            contador += 1
    
    def menu(self):
        salir = False
        while not salir:
            print("MENÚ DE LA BIBLIOTECA: 🏛️")
            print("-"*25)
            print("1️⃣. Agregar Libro 📥📚")
            print("2️⃣. Consultar Libros 🔍📚 ")
            print("3️⃣. Salir ✔")
            print("-"*25)

            opcion = input("📌 Seleccione una opción (1-3): ")
            while opcion not in ["1","2","3"]:
                print(" ⚠️ Opción no válida.")
                print("-"*25)
                opcion = input("📌🔢 Seleccione una opción (1-3): ")

            if opcion == "1":
                self.agregar_libro()
            elif opcion == "2":
                self.consultar_libros()
            elif opcion == "3":
                print("Programa finalizado ✅👋")
                salir = True

biblioteca = Biblioteca()
biblioteca.menu()