 
class Cita():
    
    def __init__(self,numero,tipo,tarifa):
        self.numero=numero
        self.tipo=tipo
        self.tarifa=tarifa
        
    def __str__(self):
        print(f"El numero de la cita es: {cita.getNumero()}")
        print(f"El tipo de cita es: {cita.getTipo()}")
        print(f"Su tarifa noraml es: {cita.getTarifa()}")
        print(f"Por ser de tipo {cita.getTipo()} su valor neto a pagar es de: {cita.getValorFinal()}")
        
    def getNumero(self):
        return self.numero
    
    def getTipo(self):
        if (self.tipo<=3):
            return "General"
        else:
            return "Especialista"

    def getTarifa(self):
        return self.tarifa

    def getValorFinal(self):
        porcentaje=self.tarifa*0.5
        if(self.tipo<=3):
            self.valorFinal=self.tarifa-porcentaje
        else:
            self.valorFinal=self.tarifa+porcentaje
        return self.valorFinal


    
cita=Cita(int(input("=>Introduzca el numero de la cita: ")),int(input("+Tipo de cita:\n>>para general: (1,2 y 3)\n>>para especialista: (4 y 5) \n =>Ingrese tipo cita: ")),float(input("=>Introduzca la tarifa: ")))
# cita=Cita(787455,4,80000)
cita.__str__()
  
