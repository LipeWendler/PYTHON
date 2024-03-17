from Veiculos import Veiculos

#Exercicio 03 --------------------------------------------

class Carro(Veiculos):
    def __init__(self, modelo, ano):
        super().__init__(modelo, tipo="Carro")
        self._ano = ano

#Exercicio 04 --------------------------------------------

    def Descrever(self):
        print(40*"=")
        print(f'Tipo: {self._tipo}')
        print(f'Modelo: {self._modelo}')
        print(f'Ano: {self._ano}')
        print(40*"=")