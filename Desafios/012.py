'''
Faça um algoritmo que leia o preço de um
produto e mostre seu novo preço, com 5% de
desconto.
'''

#Primeiro método para resolução.
'''
preco = float(input('Digite o preço: '))
porcen = preco*5/100
desc = preco-porcen
print('Seu produto de R${:.2f} com desconto: R${:.2f} fica com valor final: R${:.2f}'.format(preco, porcen, desc))
'''

#Segundo Método para resolução:
preco = float(input('Digite o preço do produto: '))
print('Seu produto de R${:.2f} com desconto de 5% R${:.2f} produto com desconto final {:.2f}'.format(preco, preco*5/100, preco-preco*5/100))