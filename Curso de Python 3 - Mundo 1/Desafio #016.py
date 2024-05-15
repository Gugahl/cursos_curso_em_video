"""DESAFIO 016"""
from math import trunc
"""
Crie um programa que leia um número real qualquer no teclado e mostre na tela a sua parte inteira.
"""

desafio = ' DESAFIO 016 '
print(f'{desafio:=^30}\n')

numero = float(input('Me forneça um número real: '))
part_num_int = trunc(numero)
print(f'A parte inteira do número {numero} é {part_num_int}.')
