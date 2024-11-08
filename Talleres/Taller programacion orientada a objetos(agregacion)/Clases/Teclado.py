from Dispositivo import Dispositivo


class Teclado(Dispositivo):
    contadorTeclado=0
    def __init__(self , IdTeclado,tipoEntrada,marca):
        super().__init__(tipoEntrada,marca)
        
        self._idTeclado=IdTeclado
        Teclado.contadorTeclado+=1
    def __str__(self):
        return(
            f"Datos-teclado:\n"\
            f"Tipo de entrada: {self._TipoEntrada}\n"\
            f"Marca: {self._Marca}\n"            
        )