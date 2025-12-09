import json
import os
 
class Empleado:
    # Constructor de la clase Empleado, que inicializa las propiedades del empleado
    def __init__(self, nombre, edad, departamento, evaluaciones):
        self.__nombre = nombre           # Nombre del empleado
        self.__edad = edad               # Edad del empleado
        self.__departamento = departamento # Departamento del empleado
        self.__evaluaciones = evaluaciones # Evaluaciones del desempeño del empleado
 
    # Métodos para obtener los valores de los atributos privados
    def obtener_nombre(self):
        return self.__nombre
 
    def obtener_edad(self):
        return self.__edad
 
    def obtener_departamento(self):
        return self.__departamento
 
    def obtener_evaluaciones(self):
        return self.__evaluaciones
 
    # Método para calcular el promedio de las evaluaciones
    def calcular_promedio(self):
        return sum(self.__evaluaciones) / len(self.__evaluaciones)

# Función para agregar un nuevo empleado
def agregar_empleado(empleados, archivo):
    # Solicitar datos del nuevo empleado
    nombre = input("Ingresa el nombre del empleado: ")  
    edad = int(input("Ingrese su edad: "))  
    departamento = input("Departamento del empleado: ")  
    evaluaciones = []  # Lista para almacenar las evaluaciones
 
    # Solicitar 3 evaluaciones para el empleado
    for i in range(3):
        evaluacion = float(input(f"Evaluación {i + 1}: "))
        evaluaciones.append(evaluacion)
 
    # Crear el objeto de empleado y agregarlo a la lista
    nuevo_empleado = Empleado(nombre, edad, departamento, evaluaciones)
    empleados.append(nuevo_empleado)
    
    # Guardar los empleados actualizados en el archivo
    guardar_empleados(archivo, empleados)
    print("El empleado fue agregado a la base de datos.")
 
# Función para guardar los empleados en un archivo JSON
def guardar_empleados(archivo, empleados):
    with open(archivo, 'w') as archivo:  # Abrir el archivo en modo escritura
        empleados_json = []  # Lista para almacenar los empleados en formato JSON
        for empleado in empleados:
            # Convertir el objeto empleado en un diccionario
            empleado_dict = {
                "nombre": empleado.obtener_nombre(),
                "edad": empleado.obtener_edad(), 
                "departamento": empleado.obtener_departamento(), 
                "evaluaciones": empleado.obtener_evaluaciones(),
                "promedio": empleado.calcular_promedio()  # Incluir el promedio en los datos guardados
            }
            
            empleados_json.append(empleado_dict)
        # Volcar los datos de los empleados en el archivo JSON
        json.dump(empleados_json, archivo)

# Función para cargar los empleados desde un archivo JSON
def cargar_empleados(archivo):
    if os.path.exists(archivo):  # Verificar si el archivo existe
        with open(archivo, 'r') as archivo:
            empleados_json = json.load(archivo)  # Leer los datos del archivo JSON
   
        empleados = []  # Lista para almacenar los objetos empleados
        for empleado in empleados_json:
            # Crear un objeto Empleado a partir de los datos cargados
            nombre = empleado["nombre"]
            edad = empleado["edad"]
            departamento = empleado["departamento"]
            evaluaciones = empleado["evaluaciones"]
       
            nuevo_empleado = Empleado(nombre, edad, departamento, evaluaciones)
            empleados.append(nuevo_empleado)
    else:
        empleados = []  # Si no existe el archivo, devolver una lista vacía        
   
    return empleados

# Función para consultar todos los empleados almacenados
def consultar_empleados(empleados):
    if not empleados:  # Si no hay empleados registrados
        print("No se encuentra ningun empleado registrado en la base de datos.")
    else:
        for empleado in empleados:
            print("\n╭───────╯ Empleado ╰───────╮")
            print(f"Nombre: {empleado.obtener_nombre()}")
            print(f"Edad: {empleado.obtener_edad()}")
            print(f"Departamento: {empleado.obtener_departamento()}")
            print(f"Evaluaciones: {empleado.obtener_evaluaciones()}")
            print(f"Promedio de Desempeño: {empleado.calcular_promedio()}")

# Función para mostrar el menú de opciones al usuario
def menu():
    archivo = "empleados.json"  # Nombre del archivo donde se guardan los empleados
    empleados = cargar_empleados(archivo)  # Cargar los empleados del archivo al inicio
 
    while True:
        # Mostrar las opciones del menú
        print("\n╭───────╯ Gestión de Empleados ╰───────╮")
        print("1. Agregar un empleado")
        print("2. Consultar empleado")
        print("3. Finalizar programa")
        opcion = input("Seleccione la opción que desea realizar: ")
 
        # Procesar la opción seleccionada
        if opcion == "1":
            agregar_empleado(empleados, archivo)  # Llamar a la función para agregar un empleado
        elif opcion == "2":
            consultar_empleados(empleados)  # Llamar a la función para consultar los empleados
        elif opcion == "3":
            print("Programa finalizado correctamente.")  # Finalizar el programa
            break
        else:
            print("Opción incorrecta por favor intenta de nuevo.")  # Mensaje de error si la opción es inválida

# Llamar a la función menu para iniciar el programa
menu()
