'''
Unit Pão = R$0,80
Unit broa = R$2,50
Custos Fabricação = 43%
Restante = 15% poupança, 15% Euros
Unit Euro = R$4,60
'''



print("=====Bem-vindo a Padaria SóPão=====")
print("Pães = R$0,80")
print("Broas = R$2,50")
print("-----------------------------------")
print("Informe a quantidade de Pães: ")
pao = int(input())
print("Anotado!")
print("Informe a quantidade de Broas: ")
broa = int(input())
print("Anotado!")

venda_pao = pao * 0.80
venda_broa = broa * 2.50
print("===================================")
print("        FECHAMENTO DO DIA")
print("Unidades de Pão vendida: ", pao)
print("Valor vendas Pães: R${0:.2f}".format(venda_pao))
print("Unidades de broa vendidas: ", broa)
print("Valor vendas Broas: R${0:.2f}".format(venda_broa))
print("-----------------------------------")
renda_bruta = venda_broa + venda_pao
print("Renda Bruta: R${0:.2f}".format(renda_bruta))
print("-----------------------------------")

print("          DESPESAS")
fabricacao = renda_bruta*0.43
print("Custos Fabricação = R${0:.2f}".format(fabricacao))
print("-----------------------------------")

print("         APLICAÇÕES")
poupanca = renda_bruta*0.15
print("Poupança = R$", poupanca)
euro = renda_bruta*0.15
unit_euro = euro//4.60
print("Valor aplicado em Euros: R${0:.2f}".format(euro))
print("Euros adquiridos: ", unit_euro)
print("-----------------------------------")

print("        LUCRO LÍQUIDO")
lucro = renda_bruta - poupanca - euro
print("Lucro Líquido = R${0:.2f}".format(lucro))



