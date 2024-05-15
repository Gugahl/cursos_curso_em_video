"""Desafio 018"""
from math import radians, sin, cos, tan
"""
Faça um programa que leia uma ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

exercicio = 'Exercício #018'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

valor = float(input('Me forneça um valor e eu o direi seu seno, cosseno e tangente(0 a 180): '))
angu = radians(valor)
seno = sin(angu)
coss = cos(angu)
tang = tan(angu)
print(f'O ângulo de {valor}º tem: \n'
      f'O seno de: {seno:.2f};\n'
      f'O cosseno de: {coss:.2f};\n'
      f'E a tangente de: {tang:.2f}.')
