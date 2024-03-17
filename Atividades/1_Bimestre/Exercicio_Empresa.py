'''
10 primeiros ganham desconto de acordo com o valor da compra
    20% se compra >= R$1.500,00
    15% se compra < R$1.500,00
'''

total_descontos = 0
total_compras = 0

for i in range(10):

    print("================================================")
    print("           BEM VINDO A NOSSA LOJA")
    print("------------------------------------------------")
    print("Qual o seu nome? ")
    nome = input()
    print("Qual o valor da sua compra? ")
    valor_compra = float(input())
    print("================================================")

    if valor_compra < 1500:
        desconto = valor_compra*0.10
        print(nome, "sua compra deu um total de R${0:.2f}".format(valor_compra))
        valor_final = valor_compra - desconto
        print("Porém com o desconto de R${0:.2f}".format(desconto))
        print("Sua compra finalizou em R${0:.2f}".format(valor_final))

    else:
        desconto = valor_compra*0.20
        print(nome, "sua compra deu um total de R${0:.2f}".format(valor_compra))
        valor_final = valor_compra - desconto
        print("Porém com o desconto de R${0:.2f}".format(desconto))
        print("Sua compra finalizou em R${0:.2f}".format(valor_final))

    total_descontos = total_descontos + desconto
    total_compras = total_compras + valor_compra

print("================================================")
print("                RESUMO DO DIA")
print("Total em vendas R${0:.2f}".format(total_compras))
print("Total em descontos R${0:.2f}".format(total_descontos))
print("------------------------------------------------")
lucro = total_compras - total_descontos
print("Lucro do dia R${0:.2f}".format(lucro))
print("================================================")
