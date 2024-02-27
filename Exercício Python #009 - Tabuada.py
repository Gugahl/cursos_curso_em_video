"""Desafio 009"""
"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""

exercicio = 'Exercício #009'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

n = int(input('Digite um número inteiro para ver sua tabuada: '))
t = ' Tabuada '
print(f'{t:=^19}')
print(f'-'*12)

print(f'{n} x  1 = {n};\n'
      f'{n} x  2 = {2*n};\n'
      f'{n} x  3 = {3*n};\n'
      f'{n} x  4 = {4*n};\n'
      f'{n} x  5 = {5*n};\n'
      f'{n} x  6 = {6*n};\n'
      f'{n} x  7 = {7*n};\n'
      f'{n} x  8 = {8*n};\n'
      f'{n} x  9 = {9*n};\n'
      f'{n} x 10 = {10*n}.')

print(f'-'*12)
