"""Desafio 032"""
"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""

desafio = ' Desafio #032 '
print(f'{desafio:=^30}', '\n')

msg = 'Ano Bissexto'

print('=' * 30)
print(f'{msg:^30}')
print('=' * 30, '\n')

ano = int(input('Me foneça um ano: '))

divisao = ano / 4

print(f'O ano {ano} é BISSEXTO e terá 366 dias!' if divisao == int(divisao) else f'O ano {ano} não é BISSEXTO e não'
                                                                                 f' terá 366 dias, e sim 365 dias!')
