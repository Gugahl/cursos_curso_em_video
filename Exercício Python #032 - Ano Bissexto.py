"""Desafio #032"""
from datetime import date
"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""

exercicio = ' Exercício #032 '
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')

else:
    print(f'O ano {ano} NÃO É BISSEXTO')
