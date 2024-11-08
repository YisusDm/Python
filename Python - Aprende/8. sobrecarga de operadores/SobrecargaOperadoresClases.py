class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, otro):
        #return self.nombre + otro.nombre esto en equivalente con cadena f es:
        return f'{self.nombre} {otro.nombre}' #retornamos la concatenacion o suma de los nombres, en este caso del primer nombre dle primer objeto con el del segundo objeto

    def __sub__(self, otro):#otro es el otro objeto que se recibe como parametro
        return self.edad - otro.edad


persona1 = Persona('Juan', 28)
persona2 = Persona('Carlos', 20)
print(persona1 + persona2)
print(persona1 - persona2)

# obj1 + obj2
# obj1.__add__(obj2)