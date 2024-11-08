#se importa Cliente ya que  persona hereda de la clase abs cliente
from Cliente import Cliente

class Persona (Cliente):
    #creo el constructor e inicializo los atributos , nombre se inicializa llamando el metodo constructor de cliente (super().__init__(nombre))
    def __init__(self,cedula,edad,nombre):        
        super().__init__(nombre)
        self._cedula = cedula
        self._edad = edad 
    #se crea el metodo  obtIdentificacion debido a que la clase padre lo tiene como abs y debe estar definido en las clases hijas    
    def obtIdentificacion(self):
        return self._cedula
    #el respectivos get  edad
    def obtEdad(self):
        return self._edad
    #se crea el metodo para incrementar la edad de la persona
    def cumplirAños(self):
        self._edad+=1
