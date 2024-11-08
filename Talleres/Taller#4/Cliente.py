#se importa ABC debido a que Cliente hereda de la clas ABC que hace alusion a la clase abstracta
from abc import ABC, abstractmethod

class Cliente(ABC):
    #se define su constructor y se inicializa el atributo
    def __init__(self,nombre):
        self._nombre=nombre
    #el respectivo get de _nombre
    def obtNombre(self):
        return self._nombre
    #el decoradorador abstractmethod  implica que el siguiente metodo debe de estar definido en las clase hijas (que heredan de cliente)
    @abstractmethod
    def obtIdentificacion(self):
        pass            
