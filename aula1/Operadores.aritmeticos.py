n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um outro valor: '))
soma = n1 + n2 #soma
mult = n1 * n2 # multiplicação
div = n1 / n2 #divisão
divin = n1 // n2 #divisão inteira
p = n1 ** n2 #potência

print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(soma, mult, div), '\n')
print('Divisão inteira {} e a potência {}'.format(divin, p))
