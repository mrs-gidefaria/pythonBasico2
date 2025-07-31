# DESAFIO 004 (parte 2) - Faça um program que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

#======================================

#TIPO 1
tipo = input('Digite algo: ')
print(' ')
print('Okay, você digitou {}'.format(tipo))
print(' ')
print('O que você digitou é um número inteiro? -->',(tipo.isnumeric()))
print('O que você digitou é um número decimal? -->',(tipo.isdecimal()))
print('O que você digitou são dígitos? -->',(tipo.isdigit()))
print('O que você digitou são caracteres? -->',(tipo.isalpha()))
print('O que você digitou é alphanumérico? -->',(tipo.isalnum()))
print('O que você digitou está todo em maiúsculas? -->',(tipo.isupper()))
print('O que você digitou está todo em minúsculas? -->',(tipo.islower()))
print('O que você digitou é um título? -->',(tipo.istitle()))
print('O que você digitou é um espaço? -->',(tipo.isspace()))
print(' ')

#========================================

#TIPO 2
tipo = input('Digite um número: ')
print(' ')
print('Okay, você digitou {}'.format(tipo))
print(' ')
print('O que você digitou é um número inteiro? -->',(tipo.isnumeric()))
print('O que você digitou é um número decimal? -->',(tipo.isdecimal()))
print('O que você digitou são dígitos? -->',(tipo.isdigit()))
print('O que você digitou são caracteres? -->',(tipo.isalpha()))
print('O que você digitou é alphanumérico? -->',(tipo.isalnum()))
print('O que você digitou está todo em maiúsculas? -->',(tipo.isupper()))
print('O que você digitou está todo em minúsculas? -->',(tipo.islower()))
print('O que você digitou é um título? -->',(tipo.istitle()))
print('O que você digitou é um espaço? -->',(tipo.isspace()))
print('Você digitou {} que é da'.format(tipo), type(tipo))
print(' ')

#Esse é um código bem básico, sem interações condicionais, apenas inserções de dados e análise de suas classes. Nos próximos códigos, faremos coisas mais legais :D 