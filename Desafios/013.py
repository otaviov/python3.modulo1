'''
Faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário, com
15% de aumento.
'''

#Primeiro método de resolução
'''
sal = float(input('Digite o seu sálario atual:'))
porcen = sal*15/100
desc = porcen+sal
print('Seu salário de R${:.2f} com aumento de 15% R${:.2f}. Valor final do salário: {:.2f}'.format(sal,porcen, desc))
'''

#Segundo método de resolução

sal = float(input('Digite o seu sálario atual:'))
print('Seu salário de R${:.2f} com aumento de 15% R${:.2f}. Valor final do salário: {:.2f}'.format(sal,sal*15/100, sal+sal*15/100))

