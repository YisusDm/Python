from Dispositivo import Dispositivo


class Raton(Dispositivo):
    contadorRatones=0
    def __init__(self,idRaton,tipoEntrada,marca):
        super().__init__(tipoEntrada,marca)
        self._idRaton = idRaton
        Raton.contadorRatones+=1
    def __str__(self):
        return(
            f"Datos-Raton:\n"\
            f"Tipo de entrada: {self._TipoEntrada}\n"\
            f"Marca: {self._Marca}\n"
        )