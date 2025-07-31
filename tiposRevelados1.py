# DESAFIO 004 (parte 1) - Faça um program que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

#======================================

tipo1 = input('Digite um texto --> ')
tipo2 = bool(input('Digite outro texto --> '))
tipo3 = int(input('Digite um número --> '))
tipo4 = float(input('Digite outro número --> '))
print('A 1ª informação que você digitou foi {}, que é da' .format(tipo1), type(tipo1))
print('A 2ª informação que você digitou foi {}, que é da' .format(tipo2), type(tipo2))
print('A 3ª informação que você digitou foi {}, que é da' .format(tipo3), type(tipo3))
print('A 4ª informação que você digitou foi {}, que é da' .format(tipo4), type(tipo4))

#Esse é um código bem básico, sem interações condicionais, apenas inserções de dados e análise de suas classes. Nos próximos códigos, faremos coisas mais legais :D 