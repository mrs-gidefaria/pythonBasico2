# DESAFIO 003 - Criar um programa que leia dois números e mostre a soma entre eles

#======================================

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
#print('A soma de', n1, 'e', n2, 'é igual a', s) || essa era a sintaxe aceita no Python 2, que apesar de funcionar, está caindo em desuso.
print('A soma entre {} e {} vale {}'.format(n1, n2, s))   # Essa é a sintaxe do Python 3 