from Dispositivo import Dispositivo
from Computadora import Computadora
from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Orden:
    contadorOrdenes=0
    _Computadoras=[]
    def __init__(self,idOrden):
        self._idOrden=idOrden
        Orden.contadorOrdenes+=1        
    def agregarComputadora(self,computadora):
        self._Computadoras.append(computadora)
    def obtComputadora(self):
        return self._Computadoras
    def __str__(self):
        return (
            f"id orden : {self._idOrden}\n"           
        )


orden1=Orden(1)
listaComputadores=[]
dispositivo1=Dispositivo("salida","dell")
monitor1=Monitor(1,dispositivo1,100)
teclado1=Teclado(101,"entrada","dell")
raton1=Raton(102,"entrada","dell")

computador1=Computadora(11111,"dell-01",monitor1,teclado1,raton1)
orden1.agregarComputadora(computador1)
print(orden1)
print(computador1)
print(monitor1)
print(teclado1)
print(raton1)
print("computadora -------2-------")
orden2=Orden(2)
listaComputadores=[]
dispositivo2=Dispositivo("salida","dell")
monitor2=Monitor(2,dispositivo1,100)
teclado2=Teclado(202,"entrada","dell")
raton2=Raton(202,"entrada","dell")

computador2=Computadora(2222,"dell-02",monitor2,teclado2,raton2)
orden2.agregarComputadora(computador2)

print(orden2)
print(computador2)
print(monitor2)
print(teclado2)
print(raton2)
