#DESARROLLO DE LA RUBRICA 20%

# PRESENTADO POR:
# CHAMORRO HURTADO EDINSON
# RUÍZ CARRASCAL RUBEN
# VERGARA TORRES JERITH

# CODIGO GRUPO: 88685

# CLASE DISPOSITIVO: Representa cada dispositivo IoT.

class Dispositivo:

# 1. Incluye un constructor de la clase que inicializa los atributos respectivos

    def __init__(self,nombre,estado=False,consumo_energia=0.0):
        self._nombre=nombre
        self._estado=estado
        self._consumo_energia=consumo_energia

# 2. Incluye getters para cada uno de los atributos

    def get_nombre(self):
        return self._nombre
    def get_estado(self):
        return "Encendido" if self._estado else "Apagado"
    def get_consumo_energia(self):
        return self._consumo_energia

# 3. Incluye setters para modificar el estado del dispositivo (encender o apagar) y el consumo de energía

    def set_estado(self, estado):
        self._estado=estado
    def set_consumo_energia(self, consumo_energia):
        self._consumo_energia=consumo_energia

# CLASE HOGAR INTELIGENTE: Gestiona los dispositivos.

class HogarInteligente:

# 1. Incluye el constructor de la clase que inicializa el atributo dispositivos como una lista vacía.

    def __init__(self):
        self._dispositivos = []

# 2. Incluye el método agregar_dispositivo: Permite agregar un objeto Dispositivo al hogar inteligente.

    def agregar_dispositivo(self, dispositivo):
        self._dispositivos.append(dispositivo)
        print(f"El dispositivo {dispositivo.get_nombre()} ha sido agregado a la lista.")

# 3. Incluye el método buscar_dispositivo: Permite buscar un dispositivo en la lista por su nombre y mostrar su información

    def buscar_dispositivo(self, nombre):
        for dispositivo in self._dispositivos:
            if dispositivo.get_nombre() == nombre:
                return dispositivo # Retorno del objeto dispositivo
        #return None # No es necesario, se aplica por buena practica, el retorno se esta dando en la linea anterior.

# 4. Incluye el método encender_dispositivo: Permite encender un dispositivo del hogar (modificar su estado a "encendido").

    def encender_dispositivo(self, nombre):
        dispositivo=self.buscar_dispositivo(nombre)
        if dispositivo:
            dispositivo.set_estado(True)
            print(f"El dispositivo {nombre} ha sido encendido.")
        else:
            print(f"El dispositivo {nombre} no fue encontrado en la base de datos.")

# 5. Incluye el método apagar_dispositivo: Permite apagar un dispositivo del hogar (modificar su estado a "apagado").

    def apagar_dispositivo(self, nombre):
        dispositivo=self.buscar_dispositivo(nombre)
        if dispositivo:
            dispositivo.set_estado(False)
            print(f"El dispositivo {nombre} ha sido apagado.")
        else:
            print(f"El dispositivo {nombre} no fue encontrado en la base de datos.")

# 6. Incluye el método listar_dispositivos: Muestra un listado de todos los dispositivos en el hogar, mostrando el nombre, el estado (encendido/apagado), y el consumo de energía.

    def listar_dispositivos(self):
        if not self._dispositivos:
            print("No fue encontrado ningun dispositivos en el hogar.")
        else:
            for dispositivo in self._dispositivos:
                print(f"Dispositivo {dispositivo.get_nombre()} , Estado: {dispositivo.get_estado()}, Consumo: {dispositivo.get_consumo_energia()} kWh")

# 7. Incluye el método calcular_consumo_total: Calcula el consumo total de energía de todos los dispositivos que están encendidos en el hogar.

    def calcular_consumo_total(self):
        consumo_total=sum(dispositivo.get_consumo_energia() for dispositivo in self._dispositivos if dispositivo._estado)
        print(f"El consumo total de los dispositivos que se encuentran encendidos es de {consumo_total} kWh")

# # Menú de opciones donde se listan los métodos de la clase HogarInteligente para administrar los dispositivos inteligentes del hogar.

#def menu():
hogar = HogarInteligente()

while True:
    print("Menú de opciones:")
    print("Opción 1 Agregar un dispositivo")
    print("Opción 2 Buscar un dispositivo")
    print("Opción 3 Encender un dispositivo")
    print("Opción 4 Apagar un dispositivo")
    print("Opción 5 Lista de dispositivos")
    print("Opción 6 Calcular consumo total de energía")
    print("Opción 7 para finalizar el programa.")

    opcion=input("Selecciona la opción que usted desee ejecutar: ")

    if opcion=="1":
        nombre=input("Ingrese el nombre del dispositivo: ")
        consumo=float(input("Ingrese el consumo de energía del dispositivo: "))
        dispositivo = Dispositivo(nombre, False, consumo)
        hogar.agregar_dispositivo(dispositivo)

    elif opcion=="2":
        nombre=input("Ingrese el nombre del dispositivo que desea buscar: ")
        dispositivo = hogar.buscar_dispositivo(nombre)
        if dispositivo:
            print(f"El dispositivo {dispositivo.get_nombre()} se encuentra {dispositivo.get_estado()} y tiene un consumo de {dispositivo.get_consumo_energia()} kWh")
        else:
            print(f"El dispositivo {nombre} no fue encontrado en nuestra base de datos.")

    elif opcion=="3":
        nombre=input("Ingrese el nombre del dispositivo que quiere encender: ")
        hogar.encender_dispositivo(nombre)

    elif opcion=="4":
        nombre=input("Ingrese el nombre del dispositivo que quiere apagar ")
        hogar.apagar_dispositivo(nombre)

    elif opcion=="5":
        hogar.listar_dispositivos()

    elif opcion=="6":
        hogar.calcular_consumo_total()

    elif opcion=="7":
        print("El programa ha sido finalizado correctamente.")
        break

    else:
        print("Se ha encontrado un error al ejecutar su opción intentar de nuevo.")



#menu()