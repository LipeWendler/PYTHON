import time
import os
time_duration = 3

#1. Crie uma tupla com os números de 1 a 5 e imprima a tupla.

numeros = (1, 2, 3, 4, 5)

print(numeros)

time.sleep(time_duration)
os.system("clear")

#2. Crie uma tupla com os nomes de três países e imprima o segundo elemento
#da tupla.

paises = ('Alemanha', 'Brasil', 'Canada')

print(paises[1])

time.sleep(time_duration)
os.system("clear")

#3. Crie uma tupla com os valores de uma conta de restaurante (valor da
#refeição, taxa de serviço e valor total). Imprima a tupla.

conta = (150, 10, 150+10)

print(conta)

time.sleep(time_duration)
os.system("clear")

#4. Crie uma tupla com os nomes de cinco pessoas e peça ao usuário para
#digitar um número entre 1 e 5. Imprima o nome correspondente ao número
#digitado.

nomes = ('Felipe', 'Isabely', 'Alvino', 'Daniela', 'Maggie')

nome = int(input("Digite um numero entre 1 e 5: "))

print(nomes[nome])

time.sleep(time_duration)
os.system("clear")

#5. Crie uma tupla com as notas de um aluno em uma disciplina e imprima a
#média das notas.

notas = (70, 80, 93, 57, 68, 60, 98)

soma = sum(notas)

print("Média das notas é {0:.2f}".format(soma/len(notas)))

time.sleep(time_duration)
os.system("clear")

#6. Crie uma tupla com as cores do arco-íris (vermelho, laranja, amarelo, verde,
#azul, anil, violeta) e peça ao usuário para digitar uma cor. Verifique se a cor
#digitada está na tupla e imprima uma mensagem correspondente.

arco_iris = ('vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'anil', 'violeta')

cor = input("Informe uma cor: ")

if cor in arco_iris:
    print(cor, ' esta presente no arco iris')

else:
    print(cor, ' não esta presente no arco iris')

time.sleep(time_duration)
os.system("clear")


#7. Crie uma tupla com as temperaturas de uma semana (sete dias) e imprima a
#temperatura máxima e mínima da semana.

temperaturas = (22, 27, 18, 30, 29, 7, 12)

print('Temperaturas da semana: ', temperaturas)
print('Menor temperatura: ', min(temperaturas))
print('Maior temperatura: ', max(temperaturas))

time.sleep(time_duration)
os.system("clear")


#8. Crie uma tupla com os nomes de cinco frutas e suas respectivas cores.
#Imprima o nome de cada fruta seguido de sua cor.

frutas = ('Maça', 'vermelho', 
          'Banana', 'amarelo', 
          'Laranja', 'laranja', 
          'Uva', 'roxo', 
          'Mirtilo', 'azul')

print(frutas)

time.sleep(time_duration)
os.system("clear")


#9. Crie uma tupla com os números de 1 a 10 e outra tupla com os números de 5
#a 15. Imprima a interseção entre as duas tuplas.

tupla_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
tupla_2 = {5, 6, 7 , 8, 9, 10, 11, 12, 13, 14, 15}

intersecao = tupla_1.intersection(tupla_2)
print(intersecao)

time.sleep(time_duration)
os.system("clear")


#10. Crie uma tupla com as letras do alfabeto e uma segunda tupla com as vogais.
#Imprima a diferença entre as duas tuplas.

alfabeto = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

vogais = {'a', 'e', 'i', 'o', 'u'}

diferença = alfabeto.difference(vogais)

print(diferença)