# 🧠 Exercícios com Tipos Primitivos — Aprendendo na Prática

Este módulo reúne três scripts simples, porém fundamentais, para entender os tipos primitivos no Python — como strings, inteiros, booleanos e números de ponto flutuante. Eles fazem parte dos primeiros passos na jornada de qualquer programador iniciante.

---

## ➕ 1. `somaTiposPrimitivos.py`

Neste desafio, o programa solicita dois números inteiros ao usuário e exibe o resultado da soma utilizando a formatação com `.format()`.

```python
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
```

📌 **Destaques:**

* Utilização da função `input()` para entrada de dados
* Conversão de dados de `str` para `int` com `int()`
* Uso de `print()` com formatação para exibir resultados

🎯 **Objetivo do exercício:**

* Compreender como capturar valores numéricos do usuário
* Praticar operações aritméticas básicas
* Aplicar formatação moderna com `.format()`

---

## 🔍 2. `tiposRevelados1.py`

Este script solicita quatro entradas do usuário: uma string, um valor booleano, um número inteiro e um número decimal. Em seguida, ele revela o **tipo primitivo** de cada valor utilizando a função `type()`.

```python
tipo1 = input('Digite um texto --> ')
tipo2 = bool(input('Digite outro texto --> '))
tipo3 = int(input('Digite um número --> '))
tipo4 = float(input('Digite outro número --> '))
print('A 1ª informação que você digitou foi {}, que é da', type(tipo1))
...
```

📌 **Destaques:**

* Coleta de múltiplos tipos de dados
* Conversão explícita com `int()`, `float()` e `bool()`
* Impressão do tipo de dado com `type()`

💡 **Nota:** A conversão direta para `bool` a partir de `input()` sempre retorna `True`, exceto quando a string for vazia. Isso é uma particularidade importante a se observar durante o aprendizado.

🎯 **Objetivo do exercício:**

* Conhecer e praticar os tipos primitivos em Python
* Aprender a usar `type()` para identificação de tipos
* Aplicar múltiplas conversões de entrada de dados

---

## 🔎 3. `tiposRevelados2.py`

Neste script expandido, o usuário digita textos ou números e o programa utiliza **métodos embutidos** das strings para revelar características sobre o que foi digitado.

### Primeira parte:

```python
tipo = input('Digite algo: ')
print(tipo.isnumeric())
print(tipo.isalpha())
print(tipo.isalnum())
...
```

### Segunda parte:

```python
tipo = input('Digite um número: ')
print(tipo.isnumeric())
print(tipo.isdecimal())
print(tipo.isupper())
...
```

📌 **Destaques:**

* Uso intensivo de métodos como `.isnumeric()`, `.isalpha()`, `.isalnum()`, `.isspace()`, `.istitle()` e outros
* Aplicação prática para análise e validação de dados inseridos

🧠 **Conceito-chave:** Cada método verifica uma propriedade específica da string. Isso é útil para validar entradas antes de processá-las, evitando erros e melhorando a experiência do usuário.

🎯 **Objetivo do exercício:**

* Explorar as diversas verificações possíveis em strings
* Praticar a análise de conteúdo textual
* Entender como métodos embutidos facilitam validações

---

## 📝 Conclusão

Esses três scripts são excelentes para fixar a base da linguagem Python. Com eles, aprendemos a:

* Capturar e processar entradas do usuário
* Converter entre tipos primitivos
* Avaliar e validar as características dos dados

📌 *Estes exercícios são essenciais para dominar a manipulação de dados em Python. Reforce-os, experimente alterações e teste os limites da linguagem!*

---
