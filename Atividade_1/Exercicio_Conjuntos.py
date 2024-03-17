import time
import os
time_duration = 3

#Exercicio 1 - Cria conjunto de 1 a 10 e imprime

conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
for i in conjunto:
    print(i)

time.sleep(time_duration)
os.system("clear")

#Exercicio 2 - Crie 2 conjunto 1 a 5 e outro 3 a 7 (união, interseção, diferença simétrica)

conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {3, 4, 5, 6, 7}

união = conjunto_1.union(conjunto_2) #Faz união dos conjuntos
print(união) 

interseção = conjunto_1.intersection(conjunto_2) #Faz interseção dos conjuntos
print(interseção)

diferença_simétrica = conjunto_1.difference(conjunto_2) #Faz diferença simétrica dos conjuntos
print(diferença_simétrica)

time.sleep(time_duration)
os.system("clear")

#Exercicio 3 - Criar conjunto vogais, pedir palavra, imprimir vogais da palavra

vogais = {'a','e', 'i', 'o', 'u'}

palavra = input("Digite uma palavra: ")
print("Palavra digitada: ", palavra)
print("============================================")

vogais_presentes =  vogais.intersection(palavra) #Apresenta como conjunto
print("Atraves de interseção: ", vogais_presentes)
print("--------------------------------------------")

print("Através de FOR: ")
for i in palavra: #Apresenta como elementos
    if i in vogais:
        print(i)

time.sleep(time_duration)
os.system("clear")


#Exercicio 4 - criar 2 conjuntos de frutas, e conparar as iguais

fruteira_1 = {'maça', 'abacate'}
fruteira_2 = {'abacaxi', 'abacate'}

frutas_iguais = fruteira_1.intersection(fruteira_2)
print(frutas_iguais)

time.sleep(time_duration)
os.system("clear")


#Exercicio 5 - Criar conjunto n° inteiros aleatorios, e printar maior e menor

inteiros = {12, 54, 34, 76, 72, 6, 12, 7, 98}
maior = 0
menor = 100

for i in inteiros:

    if i < menor:
        menor = i
    
    if i > maior:
        maior = i

print(inteiros)
print("------------------------------")
print("Maior numero:", maior)
print("Menor numero: ", menor)

time.sleep(time_duration)
os.system("clear")


#Exercicio 6 - Conjunto cores arco-iris, digitar cor, ver se cor esta em arco-iris

arco_iris = {'vermelho', 'laranja', 'amarelo', 'verde',
'azul', 'anil', 'violeta'}

cor_digitada = input("Digite uma cor: ")

if cor_digitada in arco_iris :
    print(cor_digitada, " faz parte do arco-iris")

else: 
    print(cor_digitada, " não faz parte do arco-iris")

time.sleep(time_duration)
os.system("clear")


#Exercicio 7 - Criar conjunto com dias semana, remova dias uteis, printar resultado

semana = {'segunda', 'terça', 'quarta', 'quinta',
'sexta', 'sábado', 'domingo'}

dias_uteis = {'segunda', 'terça', 'quarta', 'quinta',
'sexta'}

final_de_semana = semana.difference(dias_uteis)
print(final_de_semana)

time.sleep(time_duration)
os.system("clear")


#Execicio 8 - Criar conjunto 1 a 20, e outro de pares de 1 a 10. Imprimir diferença

conjunto_1_a_20 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
pares_1_a_10 = {2, 4, 6, 8, 10}

exercicio_8 = conjunto_1_a_20.difference(pares_1_a_10)
print(exercicio_8)

time.sleep(time_duration)
os.system("clear")

#Exercicio 9 - Ciar conjunto com notas de um aluno , verificar aprovado ou não (média 7.0)

notas = set()
soma = 0

for i in range(7):
    nota = float(input("Informe a nota do aluno: "))
    notas.add(nota)
    soma = soma + nota

media = soma/7

if media < 7:
    print("Aluno reprovado, nota final: ", media)

else:
    print("Aluno aprovado, nota final: ", media)


time.sleep(time_duration)
os.system("clear")

#Exercicio 10 -Criar conjunto com numeros primos (1 a 20), verificar se digitado esta em conjunto

primos = {2, 3, 5, 7, 11, 13, 17, 19}

numero_digitado = int(input("Digite um numero (1 a 20): "))

if numero_digitado in primos:
    print(numero_digitado, " é primo")

else:
    print(numero_digitado, " não é primo")
