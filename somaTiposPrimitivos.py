n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
#print('A soma de', n1, 'e', n2, 'é igual a', s) || esse era a sintaxe aceita no python 2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))   # Essa é a sintaxe do Python 3 