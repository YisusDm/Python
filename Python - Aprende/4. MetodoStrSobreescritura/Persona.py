class Persona:
    def __init__(self, nombre, edad):#este metodo esta siendo sobreescrito por la clase hija
        self.nombre = nombre
        self.edad = edad

    def __str__(self):#sobreescribimos la clase Persona de la clase object
        return f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):#sobrescritura pues la clase padre no tiene acceso al 
                      #atributo de sueldo de la clase hija
        return f'Empleado[Sueldo: {self.sueldo}] {super().__str__()} '
       #super().__str__() llama al metodo __str__ de la clase padre de esta forma ya no es necesario volver a
       #escribir la cadena de salida:f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]'
       # y le concateno el valor del atributo de sueldo
       
       
       
       