from Raton import Raton
from Monitor import Monitor
from Teclado import Teclado



class Computadora:
    contadorComputadoras=0
    def __init__(self,idComputadora,nombre,monitor,teclado,raton):
        self._idComputadora = idComputadora
        self._Nombre=nombre
        self._Monitor=monitor
        self._Teclado=teclado
        self._Raton=raton
        self.contadorComputadoras+=1
    def obtId(self):
        return self._idComputadora    
    def obtNombre(self):
        return self._Nombre
    
    def __str__(self):
        return (
            f"id computadora: {self._idComputadora}\n"\
            f"nombre: {self._Nombre}\n"            
        )