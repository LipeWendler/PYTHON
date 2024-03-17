'''
EXERCICIO 08
Implementação de Interface:
Crie uma interface chamada Imprimivel com um método imprimir(). 
Faça com que as classes Carro e Moto implementem essa interface e 
forneçam uma implementação para o método imprimir() que imprima 
informações sobre o veículo.
'''

class Veiculos:
    def __init__(self, modelo, tipo):
        self._modelo = modelo
        self._tipo = tipo

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

