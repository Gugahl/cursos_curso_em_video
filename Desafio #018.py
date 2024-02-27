"""DESAFIO 018"""
from math import sin, cos, tan, radians
"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

desafio = ' DESAFIO 018 '
print(f'{desafio:=^30}\n')

n = float(input('Me forneça um ângulo em graus (º): '))
num = radians(n)/180
sen = sin(num)
cossen = cos(num)
tang = tan(num)
print(' ')

print('=' * 30)
tab = 'Razões Trigonométricas'
print(f'{tab:^30}')
print('=' * 30)
print(f'O ângulo fornecido foi: {n};\n'
      f'O seno desse número é: {sen};\n'
      f'O cosseno desse número é: {cossen};\n'
      f'A tangente desse número é: {tang}.')
