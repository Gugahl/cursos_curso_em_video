"""Desafio 004"""
"""
Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre
ele.
"""

exercicio = 'Exercício #004'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

alg = input('Digite algo: ')
print(f'O tipo primitivo de {alg} é: {type(alg)}')
print(f'{alg} só tem espaços? {alg.isspace()}')
print(f'{alg} só tem números? {alg.isnumeric()}')
print(f'{alg} só tem letras? {alg.isalpha()}')
print(f'{alg} tem letras e/ou números? {alg.isalnum()}')
print(f'{alg} está em letras maiúsculas? {alg.isupper()}')
print(f'{alg} está em letras minúsculas? {alg.islower()}')
print(f'{alg} está capitalizado? {alg.istitle()}')
