"""Desafio #060"""
"""
Faça um programa que leia um número
qualquer e mostre o seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120
"""

exercicio = 'Exercício #060'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30 + f'\n')

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f'x' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
