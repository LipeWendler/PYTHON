import random

nomes = list()
nomes.append("Felipe")
nomes.append("Alvino")
nomes.append("Daniela")
nomes.append("Isabely")
nomes.append("Danilo")
nomes.append("Cassiano")
nomes.append("Andreia")
nomes.append("Aldir")
nomes.append("Leandro")
nomes.append("Liandra")
nomes.append("Carla")
nomes.append("Bianca")
nomes.append("Laura")
nomes.append("Fabiane")
nomes.append("Thalita")
nomes.append("Carlos")
nomes.append("Lucas")
nomes.append("Leonardo")
nomes.append("João")
nomes.append("Gabriel")

sobrenomes = list()
sobrenomes.append("Wendler")
sobrenomes.append("Souza")
sobrenomes.append("Palanicki")
sobrenomes.append("Nascimento")
sobrenomes.append("Von")
sobrenomes.append("Andrade")
sobrenomes.append("Loss")
sobrenomes.append("Ribas")
sobrenomes.append("Alves")
sobrenomes.append("Lustosa")
sobrenomes.append("Araujo")
sobrenomes.append("Rosdaibda")
sobrenomes.append("Silva")
sobrenomes.append("Coradassi")
sobrenomes.append("Camargo")
sobrenomes.append("Ortolani")
sobrenomes.append("Dias")
sobrenomes.append("Budel")
sobrenomes.append("Padilha")
sobrenomes.append("Auriente")

altura = list()
for i in range(20):
  altura.append(round(random.uniform(1.50, 1.95), 2))

'''
1.Faça um programa que leia um número N e gere
um arquivo com N nomes e idades aleatórios
⦁ Faça uso de duas listas criadas na mão: uma que
contenha 20 nomes e outra que contenha 20 sobrenomes
⦁ Cada linha do arquivo resultante deve conter um nome
completo e a sua idade
'''

'''
2.Estenda o exemplo do cadastro para considerar
também a altura da pessoa
'''

def dados_random(quant, nomeArquivo):
  arquivoDados = open(nomeArquivo, 'w')
  for i in range(quant):
    arquivoDados.write("NOME COMPLETO: ")
    arquivoDados.write(str(random.choice(nomes)))
    arquivoDados.write(" ")
    arquivoDados.write(str(random.choice(sobrenomes)))
    arquivoDados.write(" | IDADE:")
    arquivoDados.write(str(random.randint(18, 50)))
    arquivoDados.write(" | ALTURA: ")
    arquivoDados.write(str(random.choice(altura)))
    arquivoDados.write("\n")
    arquivoDados.write(80*"-")
    arquivoDados.write("\n")
  arquivoDados.close()


arquivo = open("dados_pessoas.txt", "a")
dados_random(len(nomes), "dados_pessoas.txt")

'''
3. Escreva uma função que recebe dois nomes de arquivos e
copia o conteúdo do primeiro arquivo para o segundo arquivo.
Considere que o conteúdo do arquivo de origem é um texto.
Sua função não deve copiar linhas comentadas (que
começam com //)
'''

def copiar_dados(nomeArquivo_principal, nomeArquivo_backup):
  arquivo_principal = open(nomeArquivo_principal, 'r')
  arquivo_backup = open(nomeArquivo_backup, 'a')
  for i in arquivo_principal:
    arquivo_backup.write(i)
  
  arquivo_principal.close()
  arquivo_backup.close()


copiar_dados("dados_pessoas.txt", "backup_dados.txt")


