"""Desafio 016"""
from math import trunc
"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
Exemplo:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""

# Usando o trunc()

exercicio = 'Exercício #016'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30)

num = float(input('Digite um número: '))
part_int_num = trunc(num)
print(f'O valor digitado foi {num}, sua parte inteira é {part_int_num}.')

# Usando o int()

exercicio = 'Exercício #016'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30)

num = float(input('Digite um número: '))
part_int_num = int(num)
print(f'O valor digitado foi {num}, sua parte é {part_int_num}.')
