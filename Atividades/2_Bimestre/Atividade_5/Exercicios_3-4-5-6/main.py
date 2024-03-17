from Carro import Carro
from Moto import Moto

Mazda = Carro("RX7", 2002)
Motoca = Moto("MT07", "Yamaha")

lista_veiculos = []

lista_veiculos.append(Mazda)
lista_veiculos.append(Motoca)

Mazda.ligar()
Motoca.ligar()

Mazda.descrever()
Motoca.descrever()

Mazda.acelerar()
Motoca.acelerar()

Mazda.acelerar()

#Exercicio 06 --------------------------------------------

for i in lista_veiculos:
    i.descrever()