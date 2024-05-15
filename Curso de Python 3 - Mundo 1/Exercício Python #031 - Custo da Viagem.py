"""Desafio #031"""
"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.

Calcule o preço da passagem cobrando R$0.50 por Km para viagens até 200Km
e R$0.45 para viagens mais longas.
"""

exercicio = ' Exercício #031 '
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

distancia = float(input(f'Olá senhor bom dia! Qual a distância em km que o senhor deseja viajar hoje? '))
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print(f'Ok! O senhor vai viajar por {distancia} quilômetros, sua passagem custará R${preco:.2f}.')
