from Veiculos import Veiculos

#Exercicio 03 --------------------------------------------

class Moto(Veiculos):
    def __init__(self, modelo, marca):
        super().__init__(modelo, tipo="Moto")
        self._marca = marca

#Exercicio 04 --------------------------------------------

    def Descrever(self):
        print(40*"=")
        print(f'Tipo: {self._tipo}')
        print(f'Modelo: {self._modelo}')
        print(f'Marca: {self._marca}')
        print(40*"=")