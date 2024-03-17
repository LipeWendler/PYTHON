from Forma import Forma

class Retangulo(Forma):
    def __init__(self, nome, comprimento, largura):
        super().__init__(nome, tipo="Retangulo")
        self._comprimento = comprimento
        self._largura = largura

    def calcularArea(self):
        area = round(self._comprimento*self._largura, 2)
        print(f'A área do retângulo é {area}')