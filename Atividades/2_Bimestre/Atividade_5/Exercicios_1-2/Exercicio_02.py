'''
Protegendo Dados com Encapsulamento:
Modifique a classe Carro do exercício anterior para usar 
atributos privados (__modelo e __ano) e métodos de acesso 
para obter e definir esses atributos.
'''

class CarroPrivado:
    def __init__(self, modelo, ano):
        self.__modelo = modelo
        self.__ano = ano

    #GET modelo
    @property
    def modelo(self):
        return self.__modelo
    
    #SET modelo
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    #GET ano
    @property
    def ano(self):
        return self.__ano
    
    #SET ano
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    
    def popsAndBangs (self):
        print(f'{self.__modelo} ano {self.__ano} está fazendo Braaahhh! Pah! Pah! Pah!')
    