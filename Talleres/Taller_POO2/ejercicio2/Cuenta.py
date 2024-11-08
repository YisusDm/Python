class Cuenta:
    
    saldoMinimo = 0
    
    def __init__(self):
        self.numero = int(input('Digite el numero: '))
        self.tipo= input('Digite el tipo ("Ahorro" o "Credito"): ')
        self.saldoActual = float(input('Digite el saldo inicial: '))
        self.saldoMinimo= self.saldoActual *0.1
    
    def consignar(self,monto):
        self.monto = monto
        self.saldoActual += self.monto
    
    def retirar(self,monto):
        self.monto = monto
        if self.saldoActual > self.saldoMinimo:
            if (self.saldoActual - self.monto) < self.saldoMinimo:
                self.monto -= self.saldoMinimo
                print('No se ha podido retirar el monto deseado.')
            else:
                pass
            self.saldoActual -= self.monto
            print(f'Usted ha retirado {self.monto}')
        else:
            print('No cuenta con la cantidad requerida para retirar.') 
            
    def getSaldoActual(self):
        print(f'El saldo actual es: {self.saldoActual}')   
        
    def getSaldoMinimo(self):
        print(f'El saldo minimo es: {self.saldoMinimo}') 
        
    def getCapacidadCredito(self):
        self.cCredito= 0
        if self.tipo == 'Ahorro':
            self.cCredito = self.saldoActual - self.saldoMinimo
        else:
            self.cCredito = self.saldoActual * 3
        print (f'Su capacidad crediticia es: {self.cCredito}')