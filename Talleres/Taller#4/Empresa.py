#se importa Cliente ya que  Empresa hereda de la clase abs Cliente
from Cliente import Cliente

class Empresa(Cliente):
    #creo el constructor e inicializo los atributos , nombre se inicializa llamando el metodo constructor de cliente (super().__init__(nombre))    
    def __init__(self,nit ,nombre,representante):
        super().__init__(nombre)
        self._nit = nit
        self._representante = representante
    #se crea el metodo  obtIdentificacion debido a que la clase padre lo tiene como abs y debe estar definido en las clases hijas
    def obtIdentificacion(self):
        return self._nit
    #el respectivo get de _representante         
    def obtRepresentante(self):
        return self._representante
    #se crea el metodo cambiarRepresentante para actualizar el valor de _representante 
    def cambiarRepresentante(self,representante):
        self._representante =representante
    
              