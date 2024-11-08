from Empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)#inicializamos el metodo __init__ del objeto de la clase padre
        self.departamento = departamento #terminamos de inicializar los atributos de la clase hija

    def __str__(self):#sobreescritura de este metodo __str__ de la clase padre
        return f'Gerente [Departamento: {self.departamento}] {super().__str__()}'#mandamos a llamar el metodo super de la clase padre

    # def mostrar_detalles(self):#sobre escritura de este metodo que es de la clase padre
    #     return self.__str__()