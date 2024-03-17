from Veiculos import Veiculos
from Imprimivel import Imprimivel

class Moto(Veiculos):
    def __init__(self, modelo, marca):
        super().__init__(modelo, tipo="Moto")
        self._marca = marca

#Exercicio 08 -------------------------------------------------------

    def imprimir(self):
        return f'Tipo: {self._tipo}\nModelo: {self._modelo}\nMarca: {self._marca}'