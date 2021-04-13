'''
    Escreva um programa que leia um valor em 
    metros e o exiba convertido em centímetros 
    e milímitros.
'''
valor = float(input('Digite um valor em metros:'))
cent = valor*100
mili = valor*1000 
print('o valor em metros é {}m\nem centímetros {:.0f}cm\ne em milímetros {:.0f}cm'.format(valor, cent, mili))