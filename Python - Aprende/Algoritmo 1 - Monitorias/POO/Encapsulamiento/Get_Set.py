class Restaurante:

    def __init__(self, nombre, categoria, localidad):
        self.nombre = nombre # Public
        self._categoria = categoria # Protec
        self.__localidad = localidad # Private

    def mostrar_datos(self):
        print(f"Restaurante: {self.nombre}")
        print(f"Categoría: {self._categoria}")
        print(f"Localidad: {self.__localidad}")    

    # Get - Obtener, Set - asignar
    def get_localidad(self):
        return self.__localidad
    
    def set_localidad(self, localidad):
        self.__localidad = localidad

r1 = Restaurante('Software Cuc','Comida Fast', 'Barranquilla')
#obtener localidad
# localidad = r1.get_localidad()
print(r1.nombre)
print(r1._categoria)
print(r1.get_localidad())

# #Cambiar Localidad
r1.set_localidad('venezuela')
r1.mostrar_datos()