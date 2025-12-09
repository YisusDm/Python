import os
import json

class Usuario:
    def __init__(self, nombre, correo, telefono, edad):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.edad = edad

    def to_dict(self):
        """Convierte la instancia de Usuario a un diccionario."""
        return {
            "nombre": self.nombre,
            "correo": self.correo,
            "telefono": self.telefono,
            "edad": self.edad
        }

#*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/* /*/**/*/*/*/*/*/*/*/*/*/*/**/*/*/  #


class GestorUsuarios:
    def __init__(self, archivo='usuarios.json'):
        self.archivo = archivo
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self): # Reader
        """Carga los usuarios desde el archivo si existe, de lo contrario retorna una lista vacía."""
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    def agregar_usuario(self, usuario): # Create
        """Agrega un nuevo usuario y guarda los cambios en el archivo."""
        self.usuarios.append(usuario.to_dict())
        self.guardar_usuarios()

    def guardar_usuarios(self):
        """Guarda la lista de usuarios en el archivo."""
        with open(self.archivo, 'w', encoding='utf-8') as file:
            json.dump(self.usuarios, file, indent=4, ensure_ascii=False)

    def mostrar_usuarios(self):# Reader
        """Muestra todos los usuarios almacenados."""
        for usuario in self.usuarios:
            print(f"Nombre: {usuario['nombre']}, Correo: {usuario['correo']}, "
                  f"Teléfono: {usuario['telefono']}, Edad: {usuario['edad']}")

# Uso del script
if __name__ == "__main__":
    gestor = GestorUsuarios()

    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Agregar usuario")
        print("2. Mostrar usuarios")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            edad = input("Edad: ")

            usuario = Usuario(nombre, correo, telefono, edad)
            gestor.agregar_usuario(usuario)
            print("Usuario agregado exitosamente.")
        elif opcion == "2":
            print("\nUsuarios registrados:")
            gestor.mostrar_usuarios()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
