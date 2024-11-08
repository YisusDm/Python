# class Cita():
    
#     def __init__(self,tipo):
#         # self._numero=numero
#         self._tipo=tipo
#         # self._tarifa=tarifa
#         # self._valorFinal=valorFinal
#     @property
#     def getTipo(self):
#         print("Metodo get ejecutando")
#         return self._tipo

#     @getTipo.setter 
#     def getTipo(self,strTipo): 
#         print("metodo set ejecutando")   
#         if (self.tipo>=1 and self.tipo<=3):
#             strTipo="General"
#         elif(self.tipo>=4 and self.tipo<=5):
#             strTipo="Especialista" 
#         return strTipo      

# cita=Cita()
# cita.getTipo=4
# print(cita.getTipo)

   
class Cita():
    
    def __init__(self,numero,tipo,tarifa,valorFinal):
        super.__init__(self,numero,tipo,tarifa)
        self.valorFinal=valorFinal

    def getNumero(self):
        return self.numero

    def getTipo(self):
        if (self.tipo<=3):
            return "general"
        else:
            return "Especialista"

    def getTarifa(self):
        return self.tarifa

    def CalcularValorFinal(self,tarifa,valorFinal):
        porcentaje=tarifa*0.5
        if(self.tipo<=3):
            valorFinal=tarifa-porcentaje
        else:
            valorFinal=tarifa+porcentaje
        return valorFinal

class PrincipalCita:
    def __init__(self,numero,tipo,tarifa):
        self.numero=numero
        self.tipo=tipo
        self.tarifa=tarifa

    def imprimir(self):
        print(f"El numero de la cita es: {Cita.getNumero()}")
        print(f"El tipo de cita es: {Cita.getTipo()}")
        print(f"Su tarifa noraml es: {Cita.getTarifa()}")
        print(f"por ser de tipo {Cita.getTipo()} su valor neto a pagar es de: {Cita.CalcularValorFinal()}")    

    numero=int(input("Introduzca el numero de la cita: "))
    tipo=int(input("Introduzca el tipo de cita:\n para general: 1,2 y 3\n y para especialista: 4 y 5 "))
    tarifa=float(input("Introduzca la tarifa: "))
    
    cita=Cita(numero,tipo,tarifa)
    cita.imprimir()
