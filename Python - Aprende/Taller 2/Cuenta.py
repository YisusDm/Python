class Cuenta():
    def __init__(self,numero,tipo,valorInicial):
        self.numero=numero
        self.tipo=tipo
        self.SaldoActual=valorInicial
        self.valorInicial=valorInicial

    def consignar(self,monto):
        self.SaldoActual+=monto

    def getSaldoMinimo(self):
        saldoMinimo=self.valorInicial*0.1  
        return saldoMinimo

    def retirar(self,montoR):
        
        if(self.SaldoActual<self.getSaldoMinimo()):
            self.SaldoActual+=montoR
            autorizado=self.SaldoActual-self.getSaldoMinimo()
            print(f"No se puede retirar esta cantidad de dinero por que su saldo actual es inferior a su salfo minimo \npor lo tanto solo puede retirar: {autorizado}")
            self.SaldoActual-=autorizado
        else: 
            self.SaldoActual-=montoR  
            print(f"Retiro exitosamenete: ${montoR}")


    def getSaldo(self):
        return self.SaldoActual

    def getCapacidadCredito(self):
        if(self.tipo=="ahorro"):
            capacidadCredito=self.SaldoActual-self.getSaldoMinimo()

        elif(self.tipo=="credito"):
            capacidadCredito=self.SaldoActual*3

        return capacidadCredito

class PrincipalCuenta:
    numero=int(input("Digite el numero de cuenta: "))
    tipo=input("Digite el tipo de cuenta, ahorro o credito: ")
    valorInicial=float(input("Digite el valor que va a consignar inicialmente: "))
    cuenta=Cuenta(numero,tipo,valorInicial)

    monto=float(input("Digite la cantidad de dinero a consignar: "))
    cuenta.consignar(monto)
    print(f"Su saldo actual es: ${cuenta.getSaldo()}")

    montoR=float(input("Digite la cantidad de dinero a retirar: "))
    cuenta.retirar(montoR)

    print(f"Su saldo actual es: ${cuenta.getSaldo()}")
    print(f"El saldo minimo de su cuenta es: ${cuenta.getSaldoMinimo()}")
    print(f"Su capacidad de credito es: ${cuenta.getCapacidadCredito()}")                                         

        