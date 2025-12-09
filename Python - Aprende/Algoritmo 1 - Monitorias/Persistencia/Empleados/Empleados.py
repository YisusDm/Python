import json
import os
 
# Clase Empleado
class Empleado:
    def __init__(self, nombre, edad, departamento, evaluaciones):
        self.__nombre = nombre
        self.__edad = edad
        self.__departamento = departamento
        self.__evaluaciones = evaluaciones
 
    def obtener_nombre(self):
        return self.__nombre
 
    def obtener_edad(self):
        return self.__edad
 
    def obtener_departamento(self):
        return self.__departamento
 
    def obtener_evaluaciones(self):
        return self.__evaluaciones
 
    def calcular_promedio(self):
        return sum(self.__evaluaciones) / len(self.__evaluaciones)
 
# Funciones para el menú
def agregar_empleado(empleados, archivo):
    nombre = input("Nombre del empleado: ")  # Solicita el nombre
    edad = int(input("Edad del empleado: "))  # Solicita la edad
    departamento = input("Departamento del empleado: ")  # Solicita el departamento
    evaluaciones = []  
 
    for i in range(3):  # Solicita tres evaluaciones de desempeño
        evaluacion = float(input(f"Evaluación {i + 1}: "))
        evaluaciones.append(evaluacion)
 
    # Crea un nuevo objeto Empleado con los datos ingresados
    nuevo_empleado = Empleado(nombre, edad, departamento, evaluaciones)
   
    # Agrega el empleado a la lista
    empleados.append(nuevo_empleado)
   
    # Guarda la lista actualizada en el archivo JSON
    guardar_empleados(archivo, empleados)
    print("Empleado agregado exitosamente.")
 
def guardar_empleados(archivo, empleados):
    with open(archivo, 'w') as archivo:
        json.dump([empleado.__dict__ for empleado in empleados], archivo)
 
# Funciones para la persistencia con JSON
def cargar_empleados(archivo):

    if os.path.exists(archivo):
        # Abre el archivo y carga los datos JSON
        with open(archivo, 'r') as archivo:
            empleados_json = json.load(archivo)  # Carga el JSON como una lista de diccionarios
    
        empleados = []
        for empleado in empleados_json:
            # Crear la instancia de la clase Empleado utilizando los datos
            nombre = empleado["nombre"]
            edad = empleado["edad"]
            departamento = empleado["departamento"]
            evaluaciones = empleado["evaluaciones"]
        
            # Crear un nuevo objeto Empleado
            nuevo_empleado = Empleado(nombre, edad, departamento, evaluaciones)
        
            # Agregar el nuevo empleado a la lista
            empleados.append(nuevo_empleado)
    else: 
        empleados = []        
   
    return empleados
 
def consultar_empleados(empleados):
    if not empleados:
        print("No hay empleados registrados.")
    else:
        for empleado in empleados:
            print("\n--- Empleado ---")
            print(f"Nombre: {empleado.obtener_nombre()}")
            print(f"Edad: {empleado.obtener_edad()}")
            print(f"Departamento: {empleado.obtener_departamento()}")
            print(f"Evaluaciones: {empleado.obtener_evaluaciones()}")
            print(f"Promedio de Desempeño: {empleado.calcular_promedio()}")

 
# Menú interactivo
def menu():
    archivo = "empleados.json"
    empleados = cargar_empleados(archivo)  # Recupera los empleados desde el archivo JSON
 
    while True:
        print("\n--- Gestión de Empleados ---")
        print("1. Agregar Empleado")
        print("2. Consultar Empleados")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
 
        if opcion == "1":
            agregar_empleado(empleados, archivo)
        elif opcion == "2":
            consultar_empleados(empleados)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
 
# Ejecución del programa
menu()