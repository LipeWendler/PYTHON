'''
EXERCICIO 03
Herança de Veículos:
Crie uma classe Veiculo com atributos como 
tipo e velocidade e, em seguida, crie classes 
Carro e Moto que herdem de Veiculo.
'''

'''
EXERCICIO 04
Sobrescrevendo Métodos:
Na classe Veiculo, crie um método chamado descricao() 
que imprima uma descrição básica do veículo. Sobrescreva 
esse método nas classes Carro e Moto para fornecer descrições 
specíficas para cada tipo de veículo.
'''

'''
EXERCICIO 05
Polimorfismo com Métodos:
Crie uma função chamada acelerar(veiculo) que aceita qualquer
objeto Veiculo e aumenta sua velocidade. Teste essa função com 
instâncias de Carro e Moto.
'''

'''
EXERCICIO 06
Polimorfismo com Listas:
Crie uma lista de objetos Veiculo contendo instâncias de Carro e Moto. 
Itere sobre a lista e chame o método descricao() para cada objeto.
'''


#Exercicio 03 --------------------------------------------

class Veiculos:
    def __init__(self, modelo, tipo, funcionando = False, velocidade = 0):
        self._modelo = modelo
        self._tipo = tipo
        self._funcionando = funcionando
        self._velocidade = velocidade

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

    @property
    def funcionando(self):
        return self._funcionando
    
    @funcionando.setter
    def funcionando(self, funcionando):
        self._funcionando = funcionando

    @property
    def velocidade(self):
        return self._velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self._velocidade = velocidade


    def ligar(self):
        print(f'O {self._modelo} está ligado!')
        self._funcionando = True

#Exercício 04 --------------------------------------------

    def descrever(self):
        print(40*"=")
        print(f'Tipo: {self._tipo}')
        print(f'Modelo: {self._modelo}')
        print(40*"=")

#Exercicio 05 --------------------------------------------

    def acelerar(self):
        if not self._funcionando:
            print(f'{self.modelo} não está ligado!')
            return
        self._velocidade = self._velocidade + 10
        print(f'{self._modelo} acelerou! e está a {self._velocidade}Km/h!')



        