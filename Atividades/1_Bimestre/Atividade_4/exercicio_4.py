import random
'''
4. Faça um programa contendo uma função que recebe como
argumentos os nomes de dois arquivos. O primeiro arquivo
contém nomes de alunos e o segundo arquivo contém as
notas dos alunos. No primeiro arquivo, cada linha
corresponde ao nome de um aluno e no segundo arquivo,
cada linha corresponde às notas dos alunos (uma ou mais).
Assuma que as notas foram armazenadas como strings, e
estão separadas umas das outras por espaços em branco.
Leia os dois arquivos e gere um terceiro arquivo que contém o
nome do aluno seguido da média de suas notas.
'''

#FUNÇÃO PARA EXTRAI DADOS DE UMA LINHA DO ARQUIVO.txt
def extrai_linhas_txt (nome_arquivo, numero_linha):
    extrai = open(nome_arquivo, 'r')
    linhas = extrai.read().splitlines()
    return linhas[numero_linha].split()

#FUNÇÃO PARA ESCREVER NÚMEROS ALEATÓRIOS EM UM ARQUIVO
def escreverNumerosAleatorios(qtdNumeros, nomeArquivo):
    arquivoNumeros = open(nomeArquivo, 'w')
    for i in range(qtdNumeros):
        arquivoNumeros.write(str(random.randint(0,10)))
        arquivoNumeros.write("\n")
    arquivoNumeros.close()

escreverNumerosAleatorios(10, 'notas.txt')


#FUNÇÃO PARA CALCULAR A MEDIA DOS ALUNOS E CRIAR UM ARQUIVO COM OS RESULTADOS
def calcularMedia (arquivoNotas, arquivoAlunos):
    notasAlunos = open(arquivoNotas, 'r')
    nomesAlunos = open(arquivoAlunos, 'r')
    notas = []
    #TRANSFORMANDO STRING EM FLOAT
    for i in notasAlunos.readlines(): #FOR para ler as linhas do arquivo.txt
        i = i.rstrip('\n') #RSTRIP para remover as quebra de linhas
        notas.append(float(i)) #APPEND para tranformar as strings em float e armazanar em lista
    
    #CONTAGEM DE ALUNOS/LINHAS
    qntdAlunos = 0
    alunos = nomesAlunos.read() 
    nomes = []
    nomes.append(alunos)
    linhas = alunos.split('\n') #Identifica a quebra de linha 
    for i in linhas: #FOR para contar a quantidade de linhas no arquivo.txt
        if i:
            qntdAlunos += 1

    #VERIFICAÇÃO E QUANTIDADE DE NOTAS POR ALUNO
    verificador = len(notas) % qntdAlunos #Verifica se o numero de notas é compativel com o numero de alunos
    notasAluno = int(len(notas) / qntdAlunos) #Vê a quantidade de notas por aluno
    medias = []
    indice = int(0)

    if verificador == 0:
        while indice < len(notas): #WHILE para calculo de média de cada aluno
            soma = 0
            soma = notas[indice] + notas[indice+1]
            indice += notasAluno
            media = soma/notasAluno
            medias.append(media)
        
    else: 
        return 'Quantidade de notas incompativel com a quantidade de alunos!'

    arquivoResultados = open('resultados.txt', 'w')
    for i in range(qntdAlunos):
        resultado = medias[i]
        nome = extrai_linhas_txt('alunos.txt', i)
        arquivoResultados.write(str(f'ALUNO: {nome} | MEDIA: {resultado}'))
        arquivoResultados.write(str('\n'))
        arquivoResultados.write(str(70*'-'))
        arquivoResultados.write(str('\n'))

    arquivoResultados.close()
    
calcularMedia('notas.txt', 'alunos.txt')

'''
5.Faça um programa para alterar uma das notas de
um aluno (usando os arquivos do exercício anterior).
O programa deve ter uma função que recebe o nome
do aluno, a nota velha e a nova nota. A função deve
fazer a alteração no arquivo.
'''

    
    


