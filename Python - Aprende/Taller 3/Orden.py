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
dispositivo1=Dispositivo("salida","Samsung")
monitor1=Monitor(1,dispositivo1,19)
teclado1=Teclado(101,"entrada","Redragon 7096")
raton1=Raton(102,"entrada","GamePack")

computador1=Computadora(94244412348,"Asus Gaming",monitor1,teclado1,raton1)
orden1.agregarComputadora(computador1)
print(orden1)
print(computador1)
print(monitor1)
print(teclado1)
print(raton1)
print("computadora -------2-------")
orden2=Orden(2)
listaComputadores=[]
dispositivo2=Dispositivo("salida","Apple visual")
monitor2=Monitor(2,dispositivo1,15)
teclado2=Teclado(202,"entrada","Apple touch")
raton2=Raton(202,"entrada","Apple Serie5")

computador2=Computadora(4798654551,"MacBook Pro",monitor2,teclado2,raton2)
orden2.agregarComputadora(computador2)

print(orden2)
print(computador2)
print(monitor2)
print(teclado2)
print(raton2)
