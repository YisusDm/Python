
# from Dispositivo import Dispositivo


class Monitor:
    contadorMonitor=0
    def __init__(self,idMonitor,dispositivo,tamaño):
        self._idMonitor=idMonitor
        self._marca=dispositivo.obtMarca()
        self._tamaño =tamaño
        self._TipoEntrada =dispositivo.obtTipoEntrada()
        Monitor.contadorMonitor+=1  
    def obtIdMonitor(self):
        return self._idMonitor
    def obtTamaño(self):
        return self._tamaño 
    def __str__(self):
        return (
            f"Datos-monitor\n"\
            f"marca: {self._marca}\n"\
            f"tamaño: {self._tamaño}\n"\
            f"tipo de entrada: {self._TipoEntrada}\n"                
        )

# dispositivoSalida=Dispositivo("salida","hp")
# monitor1=Monitor(12,dispositivoSalida,25)
# monitor2=Monitor(12,dispositivoSalida,25)
# monitor3=Monitor(12,dispositivoSalida,25)
# monitor4=Monitor(12,dispositivoSalida,25)
# print(monitor1)
# print(monitor2)
# print(monitor3)
# print(monitor4)




