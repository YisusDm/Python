class Cita:
    
    def __init__(self,numero,tipo,tarifa):
        self.numero = numero
        self.tipo = tipo
        self.tarifa= tarifa
    
    def getNumero(self):
        print(f'El numero de la cita es: {self.numero}')
    
    def getTipo(self):
        if self.tipo >= 1 and self.tipo <= 3:
            self.ti=('General')
        elif self.tipo == 4 or self.tipo == 5:
            self.ti=('Especialista') 
        else:
            self.ti= ('El valor ingresado no esta permitido')
        print(f'El tipo de la cita es: {self.ti}')
        
    def getTarifa(self):
        print(f'Su tarifa normal es: {self.tarifa}')
    
    def calcularValorFinal(self):
        if self.ti == 'General':
            self.valorT= self.tarifa * 0.5
        if self.ti == 'Especialista':
            self.valorT= self.tarifa * 1.5
        print(f'Pero por ser tipo {self.ti} queda con un valor final de: {self.valorT}')


a= Cita(int(input('Digite el numero: ')),int(input('Digite el tipo: ')),float(input('Digite la tarifa: ')))
a.getNumero()
a.getTipo()
a.getTarifa()
a.calcularValorFinal()        