'''
EXERCICIO 07
Classe Abstrata:
Crie uma classe abstrata chamada Forma com um método abstrato calcular_area().
Em seguida, crie classes Retangulo e Circulo que herdem de Forma e implementem 
o método calcular_area() para calcular a área do retângulo e do círculo, respectivamente.
'''

from abc import ABC, abstractmethod

class Forma (ABC):
    def __init__(self, nome, tipo):
        self._nome = nome
        self._tipo = tipo
        

    @abstractmethod
    def calcularArea(self):
        pass