'''
Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos
dólares ea pode comprar.
considere US$1,00 = 3,27.
'''

print('{:*^20}'.format(' CONVERTENDO REAIS EM DÓLAR '))
real = float(input('Quanto você tem na carteira? '))
dolar = real / 3,27
print('Com R${} você pode comprar U${:.2f}'.format(real, dolar))