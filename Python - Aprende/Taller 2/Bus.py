class Bus():
    def __init__(self,placa,capacidad,pasaje,actuales,dineroAcumulado=None):
        self.placa=placa
        self.capacidadPasajeros=capacidad
        self.precioPasaje=pasaje
        self.pasajerosActuales=actuales
        self.totalPasajeros=actuales
        self.dineroAcumulado=dineroAcumulado

    def getPlaca(self):
        return self.placa
        
    def getCapacidad(self):
        return self.capacidadPasajeros

    def getPrecioPasaje(self):
        return self.precioPasaje

    def getPasajeroTotales(self):
        return self.totalPasajeros

    def getPasajerosActuales(self):
        return self.pasajerosActuales 

    def subirPasajero(self,pasajeros):
        if(pasajeros>self.capacidadPasajeros):
            print(f"No se puede subir {pasajeros} por que es SOBRECUPO ")
        else:
            if ((self.pasajerosActuales + pasajeros)>self.capacidadPasajeros):
                capacidadActual=self.capacidadPasajeros-self.pasajerosActuales
                print(f"No se puede subir {pasajeros} por que es SOBRECUPO \nEl maximo de pasajeros que pueden abordar en este momento es: {capacidadActual}")
            else:
                self.totalPasajeros+=pasajeros
                self.pasajerosActuales+=pasajeros
                print("Los pasajeros han abordado exitosamente")
                
    
    def totalDineroAcumulado(self):
        self.dineroAcumulado=(self.precioPasaje*self.totalPasajeros)
        return self.dineroAcumulado  

    def bajarPasajeros(self,pasajero1):    
        if(pasajero1>self.pasajerosActuales):
            return "La cantidad de pasajeros que desea bajar es mayor al numero de pasajeros que actualmente hay en el bus!!!"
        else:
            self.pasajerosActuales-=pasajero1

class principalBus:
    while True:
        placa=input("Digite la placa del bus: ")
        pasaje=float(input("Digite el valor del pasaje: "))
        capacidad=int(input("Ingrese la capacidad del bus: "))
        actuales=int(input("Ingrese el numero de pasajeros que estan en el bus:"))
        
        if(actuales>capacidad):
            print("Error!!! El numero actual de pasajeros sobrepasa la capacidad del bus")
        else:
            bus=Bus(placa,capacidad,pasaje,actuales,actuales)
            while True:
                pasajeros=int(input("ingrese la cantidad de pasajeros a subir al bus: "))
                bus.subirPasajero(pasajeros)
                print(f"El numero actual de pasajeros es: {bus.getPasajerosActuales()}")
                print(f"El bus tiene una capacidad maxima de: {bus.getCapacidad()}")
                print(f"La placa del bus es: {bus.getPlaca()}")
                print(f"EL total de dinero acumulado es: ${bus.totalDineroAcumulado()}")
                print(f"El numero de pasajeros que se han subido es: {bus.getPasajeroTotales()}")
                x=input("para bajar pasajeros digite (1) \npara terminar la ruta marque (2) \npara continuar subiendo pasajeros presione (enter) \nSeleccione: ")
                if (x=="1"):
                    pasajero1=int(input("Ingrese el numero de pasajeros que va abajar del bus: "))
                    bus.bajarPasajeros(pasajero1)
                elif(x=="2"):
                    print(f"El dinero acumulado es: ${bus.totalDineroAcumulado()}")
                    break
                else:
                    continue        



            



          
    
                