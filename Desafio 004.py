"""DESAFIO 004"""
"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis.
"""

desafio = ' DESAFIO 04 '
print(f'{desafio:=^30}')
alg = input('Digite algo: ')
print(f'{type(alg)}')
print(f'{alg} só tem números? {alg.isnumeric()}.')
print(f'{alg} só tem letras? {alg.isalpha()}.')
print(f'{alg} tem algum número ou alguma letra? {alg.isalnum()}.')
print(f'{alg} só tem letras minúsculas? {alg.islower()}.')
print(f'{alg} só tem letras maiúsculas? {alg.isupper()}.')
print(f'{alg} tem números após o ponto? {alg.isdecimal()}.')
print(f'{alg} tem letras maiúsculas só no começo? {alg.istitle()}.')
print(f'{alg} só tem espaços? {alg.isspace()}.')
