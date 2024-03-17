from Forma import Forma

class Circulo(Forma):
    def __init__(self, nome, diametro):
        super().__init__(nome, tipo="Circulo")
        self._diametro = diametro

    def calcularArea(self):
        raio = self._diametro/2
        area = round(3.1415*(raio**2), 2)
        print(f'A área do Circulo é {area}')