'''
Faça um algoritmo que leia o preço de um
produto e mostre seu novo preço, com 5% de
desconto.
'''
preco = float(input('Digite o preço: '))
porcen = preco*5/100
desc = porcen-preco
print('Seu produto de: R${:.2f} com desconto de {:.2f} tem o valor final de: R${:.2f}'.formart(preco,porcen,desc))
