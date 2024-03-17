'''
Notas em valores reais de 0.0 a 10.0
Devolve média
Quantidade >= de 6.0
Quantida >= média
Devolve maior e menor nota
'''

qntd_notas = []
nota = 0
i = 0

while len(qntd_notas) < 10: #Define a capacidade máxima de notas validadas a serem armazenadas
    print("====================================================")
    print("                 SISTEMA DE NOTAS")
    print("----------------------------------------------------")
    print("Informe o nota do aluno: ")
    nota = float(input()) #Captação da nota inserida
    
    if nota >= 0 and nota <= 10: #Verificação se nota está dentro do limite de 0.0 à 10.0
        if len(qntd_notas) == 0:
            nota_maior = nota
            nota_menor = nota
            qntd_notas.append(nota) #Adiciona a nota inserida na lista "qntd_notas"
            print("----------------------------------------------------")
            print("Notas validadas: ", len(qntd_notas)) #Contagem de notas dentro do padrão estabelecido
            

        elif nota > nota_maior: #Classifica qual a maior nota se verdade
            nota_maior = nota
            qntd_notas.append(nota)
            print("----------------------------------------------------")
            print("Notas validadas: ", len(qntd_notas))
            

        elif nota < nota_menor: #Classifica qual a menor nota se verdade
            nota_menor = nota
            qntd_notas.append(nota)
            print("----------------------------------------------------")
            print("Notas validadas: ", len(qntd_notas))
            

        else:
            qntd_notas.append(nota)
            print("----------------------------------------------------")
            print("Notas validadas: ", len(qntd_notas))  
    
    else:
        print("====================================================") 
        print("Nota Invalida, digite novamente.")
        
        
print("====================================================")   
print("             ESTATISTICAS DAS NOTAS")
print("----------------------------------------------------")

soma_notas = sum(qntd_notas) #Soma as notas dentro da lista "qntd_notas"
media = soma_notas / len(qntd_notas) #Calcula a media
print("Média das notas: {0:.1f}".format(media)) #Printa a média
print("----------------------------------------------------")

print("Menor nota: {0:.1f}".format(nota_menor))
print("Maior nota: {0:.1f}".format(nota_maior))
print("----------------------------------------------------")

qntd_notas = list(filter(lambda x: x >= 6, qntd_notas)) #Filtro para notas >= 6
print("Quantidade de notas acima ou igual a 6.0: ", len(qntd_notas)) #Printar quantidade de notas dentro do filtro

qntd_notas = list(filter(lambda x: x >= 7, qntd_notas)) #Filtro para notas >= 7
print("Quantidade notas acima ou igual a média (7.0): ", len(qntd_notas))#Printar quantidade de notas dentro do filtro
print("====================================================")   

    

            
    

 


