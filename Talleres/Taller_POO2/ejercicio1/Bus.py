class Bus:
    pasajerosActuales = 0
    pasajerosTotales= 0
    
    def __init__(self, placa= (''),capacidad= 30,prPasaje=2500.0):
        self.placa= placa
        self.capacidad= capacidad
        self.prPasaje= prPasaje
    
    def getPlaca(self):
        print(f'La placa es: {self.placa}')
        
    def getCapacidad(self):
        print(f'La capacidad es: {self.capacidad}')
        
    def getPrPasaje(self):
        print(f'El precio del pasaje es: {self.prPasaje}')
        
    def getPasajerosTotales(self):
        print(f'Los pasajeros totales son: {self.pasajerosTotales}')
        
    def getPasajerosActuales(self):
        print(f'Los pasajerosActuales son: {self.pasajerosActuales}')
        
    def subirPasajeros(self,pasajeros=1):
        self.pasajeros = pasajeros
        disp= self.capacidad - self.pasajerosActuales
        if disp == 0:
            print('No hay cupo disponible.')
        else:
            contador= 0
            for i in range (self.pasajeros):
                if self.pasajerosActuales < 30:
                    self.pasajerosActuales +=1
                    self.pasajerosTotales +=1
                else:
                    contador += 1
            if contador != 0:
                print(f'{contador} no han podido subirse.')
            else:
               print('Pasajeros subidos con exito.')
               
    def bajarPasajeros(self,pasajeros=1):
        self.pasajeros = pasajeros
        if self.pasajerosActuales == 0:
            print('No hay ningun pasajero.')   
        else:
            cont= 0
            for i in range (self.pasajeros):
                if self.pasajerosActuales > 0:
                    self.pasajerosActuales -= 1
                else:
                    cont +=1
            if cont != 0:
                print(f'{cont} no han podido ser bajados ya que no hay más pasajeros.')
            else:
                print('Pasajeros bajados con exito.')
                
    def getDineroAcumulado(self):
        dineroT= self.prPasaje * self.pasajerosTotales
        print(f'El dinero acumulado es: {dineroT}')
                 