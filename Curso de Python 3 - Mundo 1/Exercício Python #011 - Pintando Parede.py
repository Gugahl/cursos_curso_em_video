"""Desafio 011"""
"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
"""

exercicio = 'Exercício #011'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

larg = float(input('Qual a largura dessa parede em metros? '))
alt = float(input('Qual a altura dessa parede em metros? '))
print(' ')
print(f'Área da parede: {alt*larg} metros quadrados;\n'
      f'Para pintar essa parede serão necessários: {(alt*larg)/2} litros de tinta, ou seja,\n'
      f'mais ou menos {((alt*larg)/2)//3.6+1} latas de tinta de 3.6 litros.')
