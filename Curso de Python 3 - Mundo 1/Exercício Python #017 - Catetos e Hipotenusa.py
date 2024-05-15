"""Desafio 017"""
from math import hypot
"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa.
"""

# Por meio da função hypot da biblioteca math
exercicio = 'Exercício #017'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

print('Bom dia! Sou Pitágoras e acabei de desenvolver um meio de calcular a hipotenusa de um triângulo, necessito '
      'somente de algumas informações.\n'
      ' ')
cat_oposto = float(input('Me forneça o comprimento do cateto oposto desse triângulo, em metros: '))
cat_adjacente = float(input('Me forneça o comprimento do cateto adjacente desse triângulo, em metros: '))
hipot = hypot(cat_oposto, cat_adjacente)
print(f'Ok, a hipotenusa desse triângulo equivale a {hipot:.2f} metros quadrados.')

# Por meio do Teorema de Pitágoras
exercicio = 'Exercício #017'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

print('Bom dia! Sou Pitágoras e acabei de desenvolver um meio de calcular a hipotenusa de um triângulo, necessito '
      'somente de algumas informações.\n'
      ' ')
cat_oposto = float(input('Me forneça o comprimento do cateto oposto desse triângulo, em metros: '))
cat_adjacente = float(input('Me forneça o comprimento do cateto adjacente desse triângulo, em metros: '))
hipot = (cat_oposto**2 + cat_adjacente**2)**(1/2)
print(f'Ok, a hipotenusa desse triângulo equivale a {hipot:.2f} metros quadrados.')
