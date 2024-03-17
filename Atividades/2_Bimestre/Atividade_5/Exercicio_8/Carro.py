from Veiculos import Veiculos
from Imprimivel import Imprimivel

class Carro(Veiculos, Imprimivel):
    def __init__(self, modelo, ano):
        super().__init__(modelo, tipo="Carro")
        self._ano = ano

#Exercicio 08 -------------------------------------------------------
    def imprimir(self):
        return f'Tipo: {self._tipo}\nModelo: {self._modelo}\nAno: {self._ano}'


    