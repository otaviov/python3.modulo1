#Escrevendo Olá mundo na tela e me apresentando.
print ('Olá, mundo!')
#perguntando ao usuário o nome: 
nome = input('Como você se chama?')
print ('Olá,', nome, 'Prazer em conhece-lo(ª). Eu me chamo Otávio')

#Variáveis 

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um outro valor: '))
#Somando os dois números digitados pelo usuário, (input). 
soma = (n1+n2)
#Imprimido a soma.
#print('A soma dos números digitados é: ', soma) ou
#print('A soma entre', n1, 'e', n2, 'vale:', soma)
#Mundando o formato do print:
print ('A soma entre {} e {} vale {}' .format(n1, n2, soma))


