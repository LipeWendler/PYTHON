
#Exercicio 08 -------------------------------------------------------

from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass
