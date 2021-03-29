'''
    Faça um programa que leia algo pelo
    teclado e mostre na tela e seu tipo
    primitivo e todos as informações 
    possíveis sobre ele.
'''

#criando uma variável para guardar valor do usuário.
valor = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(valor))
print('Só tem espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabético?', valor.isalpha())
print('Está em maiúsculas?',valor.isupper())
print('Está em minúsculas?', valor.islower())
print('Está capitalizada?', valor.istitle())
