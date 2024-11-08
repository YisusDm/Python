class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona): #subclase o clase hija
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)#mandamos a llamar el constructor de la clase padre para acceder
        self.sueldo = sueldo

empleado1 = Empleado('Oscar', 52, 500000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)