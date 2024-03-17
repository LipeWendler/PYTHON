import os
import time

#Criando pilha

def criar_pilha():
    pilha = []
    return pilha

def verificar_vazio(pilha):
    return len(pilha) == 0

#Empilhar

def push(pilha, item):
    pilha.append(item)

#Desempilhar

def pop(pilha):
    if not verificar_vazio(pilha):
        return pilha.pop()

    else:
        return "A pilha está vazia"

#Topo da piilha

def peek(pilha):
    if not verificar_vazio(pilha):
        return pilha[-1]

    else:
        return "Pilha está vazia"


#Tamanho da pilha

def size(pilha):
    return len(pilha)



'''
1. Escreva uma função recursiva em Python que calcule a soma dos primeiros N
números inteiros positivos.
'''
os.system("clear")

numeros_inteiros = criar_pilha()
soma = 0

quantidade_numeros = int(input("Quantos números deseja somar: "))

for i in range(quantidade_numeros): 
    numero_digitado = int(input("Digite um número: "))
    push(numeros_inteiros, numero_digitado)

os.system("clear")
print(40*"=")
print("Numeros digitados: ", numeros_inteiros)

for i in range(len(numeros_inteiros)):
    soma += peek(numeros_inteiros)
    pop(numeros_inteiros)
print(40*"-")
print("A soma dos números é igual a: ", soma)

print("\n")
print(40*"-")
input("Pressione ENTER para continuar")
os.system("clear")


'''
2. Escreva uma função recursiva para calcular o número fatorial de um número inteiro
positivo.
'''

def fatorial(numero):
  if numero==1: #Caso Base
    return 1
  return numero*fatorial(numero-1) #Chamada recursiva

numero = int(input("Digite um número inteiro positivo: "))

while numero < 0:
    os.system("clear")
    print(40*"=")
    print("Número invalido!")
    print(40*"-")
    numero = int(input("Digite um número inteiro positivo: "))

os.system("clear")
print(40*"=")
print("Número válido!")
print(40*"-")
print("Fatorial de", numero, "é: ", fatorial(numero))


print("\n")
print(40*"-")
input("Pressione ENTER para continuar")
os.system("clear")

'''
3. Escreva uma função que use uma pilha para inverter uma string.
'''

continuar = True

while continuar:

    #Criando pilhas
    
    palavra_digitada = criar_pilha()
    palavra_reconstruida = criar_pilha()
    palavra_inicial = criar_pilha()
    palavra_com_espaço = criar_pilha()

    palavra = input("Digite uma palavra, e veja se é um palindromo: ").lower()
   
    palavra_sem_espaço = ''.join(palavra.split()) #Remove espaços da string
    tamanho = len(palavra_sem_espaço)
    tamanho_com_espaço = len(palavra)

    for i in range(tamanho_com_espaço): #FOR para fracionar a palavra
        push(palavra_com_espaço, palavra[i])

    for i in range(tamanho): #Fraciona em duas pilhas diferentes
        push(palavra_digitada, palavra_sem_espaço[i])
        push(palavra_inicial, palavra_sem_espaço[i])

    print(51*'=') #Serve para fazer tracinho
    print("             Verificador de Palindromos")
    print(51*'-') #Serve para fazer tracinho
    print("Palavra digitada: \n", palavra_com_espaço)

    print("\nVerificando palavra...")
    time.sleep(1)

    for i in palavra:
        if i == " ":
            print("Removendo espaço...")
            time.sleep(1)

    for i in range(tamanho): #FOR para remontar a palavra de trás para frente
        push(palavra_reconstruida, peek(palavra_digitada))
        pop(palavra_digitada)

    print("\nPalavra invertida sem espaços: \n", palavra_reconstruida)
    print(51*'-') #Serve para fazer tracinho

    if palavra_inicial == palavra_reconstruida:
        print("RESPOSTA: |", palavra, "| é um palindromo")

    else:
        print("RESPOSTA: |", palavra, "| não é um palindromo")

    print(51*'=') #Serve para fazer tracinho

    sair_sistema = input("Deseja sair do sistema: ").lower().startswith("s")
    if sair_sistema == True:
        continuar = False
    
    print("\n")
    print(40*"-")
    input("Pressione ENTER para continuar")
    os.system("clear")

    '''
    4. Escreva uma função que converte um número decimal em sua representação binária
usando uma pilha.
'''

conversor = criar_pilha()
convertida = criar_pilha()

numero = int(input("Digite um numero decimal: "))
inicial = numero

while numero >= 1:
    resto = numero %2
    push(conversor, resto)
    numero = numero // 2
    
  
for i in range(len(conversor)):
        push(convertida, peek(conversor))
        pop(conversor)

print("O numero ", inicial, " em binário é ", convertida)

print("\n")
print(40*"-")
input("Pressione ENTER para continuar")

'''
5. Implemente um histórico de comandos de um editor de texto simples usando uma
pilha. A cada vez que um comando é executado, ele é adicionado à pilha.
Implemente a capacidade de desfazer um comando usando a pilha.
'''

os.system("clear")

texto = criar_pilha()
voltar = criar_pilha()
ultima_acao = 0
continuar = True

print(50*"=")
print("             EDITOR DE TEXTO")
print(50*'-')

informacao= input()
push(texto, informacao)
push(voltar, informacao)

os.system("clear")

while continuar:
    os.system("clear")

    print(50*"=")
    print("             EDITOR DE TEXTO")
    print(50*'-')
    for i in range(len(texto)): #FOR para printar texto fora da pilha
        print(texto[i], end=" ")
    
    print("\n")
    print(50*'-')
    print("[1] Adicionar texto \n[2] Remover ultimo texto \n[3] Voltar ação")
    edicao = int(input("Qual edição deseja: "))

    match edicao:
        case 1: #CASE para adicionar texto
            os.system("clear")
            ultima_acao = 1

            print(50*"=")
            print("             EDITOR DE TEXTO")
            print(50*"-")

            for i in range(len(texto)): #FOR para printar texto fora da pilha
                print(texto[i], end=" ")

            informacao = input()
            push(texto, informacao) #Adiciona o texto digitado na pilha
            os.system("clear")
                
            print(50*"=")
            print("             EDITOR DE TEXTO")
            print(50*"-")

            for i in range(len(texto)): #FOR para printar texto fora da pilha
                print(texto[i], end=" ")

            print("\n")
            print(50*"-")
            input("Pressione ENTER para continuar")

        case 2: #CASE para apagar o ultimo texto inserido               
            os.system("clear")
            ultima_acao = 2

            push(voltar, peek(texto)) #Joga dado para pilha backup antes de apagar
            pop(texto) #Apaga ultimo texto inserido

            print(50*"=")
            print("             EDITOR DE TEXTO")
            print(50*"-")

            for i in range(len(texto)): #FOR para printar texto fora da pilha
                print(texto[i], end=" ")
            
            print("\n")
            print(50*"-")
            input("Pressione ENTER para continuar")

        case 3: #CASE para voltar um passo
            os.system("clear")
            
            if ultima_acao == 1: #Restaura para antes do ultimo texto inserido
                pop(texto) 
        
            if ultima_acao == 2: #Restaura o texto apagado
                push(texto, peek(voltar))
                pop(voltar)

            print(50*"=")
            print("             EDITOR DE TEXTO")
            print(50*"-")

            for i in range(len(texto)): #FOR para printar texto fora da pilha
                print(texto[i], end=" ")

            print("\n")
            print(50*"-")
            input("Pressione ENTER para continuar")