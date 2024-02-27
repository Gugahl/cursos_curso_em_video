"""Curso Python #07 - Operadores Aritméticos"""
"""
# Operadores aritméticos
# + = soma
# - = subtração
# * = multiplicação
# / = divisão completa
# // = divisão inteira
# % = resto da divisão
# ** = potenciação

# Bizú: Para o cálculo da raiz quadrada eleve o número que você quer saber a raiz quadrada a meio = (1/2)
# Bizú: Para o cálculo da raiz cúbica eleve o número que você quer saber a raiz quadrada a um terço = (1/3)

# (print(5 + 2, 5 - 2, 5 * 2, 5 / 2, 5 ** 2, 5 // 2, 5 % 2, 25**(1/2), 125**(1/3)))

# Ordem de precedência:
# 1º ()
# 2º **
# 3º *, /, // e %
# 4º + e -

# print(5+3*2, 3*5+4**2, 3*(5+4)**2)

# Operações com strings:
# print('Oi' + 'Olá',
# 'Oi' * 5,
# '=' * 20)

# Alinhamentos:
# nome = (input('Qual é o seu nome? ').lower()).title()
# A esquerda:
# print(f'Prazer em te conhecer {nome:>20}!')
# A direita:
# print(f'Prazer em te conhecer {nome:<20}!')
# Meio
# print(f'Prazer em te conhecer {nome:^20}!')
# Alinhamento com strings (Meio, (=)):
# print(f'Prazer em te conhecer {nome:=^20}!')

# Operações sem precisar de variáveis:
n1 = float(input('Me forneça um número: '))
n2 = float(input('Me forneça outro número: '))
print(f'A soma: {n1} + {n2} é igual a: \n {n1+n2:.3f}')
print(f'A subtração: {n1} - {n2} é igual a: \n {n1-n2:.3f}', end=', ')
print(f'\n já a subtração: {n2} - {n1} é igual a: \n {n2-n1:.3f}')
print(f'A multiplicação: {n1} x {n2} é igual a: \n {n1*n2:.3f}')
print(f'A divisão: {n1} : {n2} é igual a: \n {n1/n2:.3f}', end=', ')
print(f'\n já a divisão: {n2} : {n1} é igual a: \n {n2/n1:.3f}')
print(f'O número {n1} elevado a {n2} é igual a: \n {n1**n2:.3f}', end=', ')
print(f'\n já o número {n2} elevado a {n1} é igual a: \n {n2**n1:.3f}')
"""
