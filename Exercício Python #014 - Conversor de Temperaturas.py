"""Desafio 014"""
"""
Escreva um programa que converta uma temperatura digitada em graus celsius para graus farenheit.
"""

exercicio = 'Exercício #014'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

celso = float(input('Informe a temperatura em graus celsius (ºC): '))
print(' \n'
      'Temperatura:\n'
      f'{celso}ºC    =     {celso*1.8+32}ºF.\n'
      f'Celsius         Farenheit')
