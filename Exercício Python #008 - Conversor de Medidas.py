"""Desafio 008"""
"""
Escreva um programa que leia um valor em metros e o exiba em convertido quilômetros, metros, centímetros e milímetros.
"""

exercicio = 'Exercício #008'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

n = float(input('Me forneça uma distância em metros: '))
print(f'Ok, você me forneceu uma distância de {n} metros;\n'
      f'Essa distância convertida em quilômetros fica: {n/1000}km;\n'
      f'Essa distância convertida em hectômetros fica: {n/100}hm;\n'
      f'Essa distância convertida em decâmetros fica: {n/10}dam;\n'
      f'Essa distância convertida em decímetros fica: {n*10}dm;\n'
      f'Essa distância convertida em centímetros fica: {n*100}cm;\n'
      f'Essa distância convertida em milímetros fica: {n*1000}mm.')
