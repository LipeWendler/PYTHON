import time
import os
time_duration = 3

#1. Crie um dicionário vazio e adicione duas chaves e valores a ele.

dicionario = {}

dicionario['marca'] = 'GM'
dicionario['modelo'] = 'Astra'

print(dicionario)

time.sleep(time_duration)
os.system("clear")

#2. Crie um dicionário com as chaves nome, idade e cidade; e preencha com seus dados. Imprima o dicionário.

dados_pessoais = {
    'Nome' : {},
    'Idade' : {},
    'Cidade' : {}
}

nome = input("Qual seu nome? ")
dados_pessoais['Nome'] = nome

idade = input("Qual sua idade? ")
dados_pessoais['Idade'] = idade

cidade = input("Qual cidade mora? ")
dados_pessoais['Cidade'] = cidade

print(dados_pessoais)

time.sleep(time_duration)
os.system("clear")


#3. Crie um dicionário com o nome e o preço de três produtos diferentes. Imprima o dicionário.

mercado = {
    'Coca-cola 2.5L' : 'R$11.00',
    'Alcatra Kg' : 'R$40.00',
    'Carvão' : 'R$14.50' 

}

print(mercado)

time.sleep(time_duration)
os.system("clear")

#4. Crie um dicionário com o nome de três estados e suas respectivas capitais.
#Peça ao usuário para digitar um estado e imprima a capital correspondente.

estados = {
    'PR' : 'Curitiba',
    'SC' : 'Florianopolis',
    'RS' : 'Porto Alegre'
}

estado_digitado = input("Escolha PR, SC ou RS: ")

print('A capital de',estado_digitado, ' é ', estados[estado_digitado])

time.sleep(time_duration)
os.system("clear")


#5. Crie um dicionário com o nome de cinco cidades e suas respectivas
#populações. Imprima a cidade com a maior população.

cidades = {
    'Guarapuava' : 182.644,
    'Irati' : 59.250,
    'Pinhão' : 32.559,
    'Foz do Iguaçu' : 258.248,
    'Turvo' : 13.095 
}

print(cidades)
populosa = max(cidades, key=cidades.get) #Pega chave de maior valor
print(populosa, ' é a mais populosa')

time.sleep(time_duration)
os.system("clear")


#6. Crie um dicionário com o nome de três alimentos e suas respectivas calorias.
#Peça ao usuário para digitar um alimento e imprima a quantidade de calorias
#correspondente.

alimento = {
    'Banana' : 122,
    'Feijão' : 70,
    'Macarrão' : 131
}

escolha = input("Escolha entre Banana, Feijão e Macarrão, e veja suas kcal: ")
print(alimento[escolha], 'kcal')

time.sleep(time_duration)
os.system("clear")


#7. Crie um dicionário com o nome de cinco animais e suas respectivas
#classificações (mamífero, ave, réptil, etc.). Imprima apenas os nomes dos
#animais.

animais = {
    'cachorro' : 'mamifero',
    'lagarto' : 'reptil',
    'passaro' : 'ave',
    'gato' : 'mamifero',
    'galinha' : 'ave'
}

animal = animais.keys()

print(animal)

time.sleep(time_duration)
os.system("clear")


#8. Crie um dicionário com o nome de cinco países e suas respectivas bandeiras.
#Imprima apenas os nomes dos países.

paises = {
    'alemanha' : 'alemã',
    'brasil' : 'brasileira',
    'chile' : 'chilena',
    'russia' :'russa',
    'italia' : 'italiana'
}

pais = paises.keys()

print(pais)

time.sleep(time_duration)
os.system("clear")


#9. Crie um dicionário com o nome de cinco frutas e suas respectivas cores.
#Imprima o nome de cada fruta seguido de sua cor.

frutas = {
    'maça' : 'vermelho',
    'banana' : 'amarelo',
    'laranja' : 'laranja',
    'uva' : 'roxo',
    'mirtilo' : 'azul'
}

print(frutas)

time.sleep(time_duration)
os.system("clear")

#10. Crie um dicionário com o nome de três jogos e a quantidade de jogadores
#necessária. Peça ao usuário para digitar um jogo e imprima a quantidade de
#jogadores correspondente.


jogos = {
    'CS' : 10,
    'Rocket_League' : 4,
    'Minecraft' : 3
}

jogo = input("Escolha entre CS, Rocket_League, Minecraft: ")

print(jogos[jogo], ' jogadores necessários')
