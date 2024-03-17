'''
Classe Básica com Encapsulamento:
Crie uma classe chamada Carro com atributos encapsulados (_modelo e _ano) 
e métodos para obter e definir esses atributos.
'''

class Carro:
    def __init__(self, modelo, ano):
        self._modelo = modelo
        self._ano = ano

    #GET modelo
    @property
    def modelo(self):
        return self._modelo
    
    #SET modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    #GET ano
    @property
    def ano(self):
        return self._ano
    
    #SET ano
    @ano.setter
    def ano(self, ano):
        self._ano = ano


    def ligar(self):
        print(f'O {self._modelo} ano {self._ano} foi ligado')




        
    

