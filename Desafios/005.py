'''
    Faça um programa que leia um número
    inteiro e mostre na tela o seu sucessor e 
    eu antecessor.
'''
print('{:*^30}'.format('DESAFIO 5'))
num = int(input('Digite um número: '))
print('O sucessor do número {} é {}'.format(num,num+1))
print('O antecessor do número {} é {}'.format(num, num-1))