class Dispositivo:
    def __init__(self,tipoEntrada,marca):
        self._TipoEntrada = tipoEntrada
        self._Marca =marca                
    def obtTipoEntrada(self):
        return self._TipoEntrada
    def obtMarca(self):
        return self._Marca
    def __str__(self):
        return (
            f"{self._TipoEntrada}\n"\
            f"{self._marca}\n"
        )