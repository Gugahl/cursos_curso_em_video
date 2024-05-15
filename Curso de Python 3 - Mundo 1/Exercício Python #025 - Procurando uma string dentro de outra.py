"""Desafio 025"""
"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.
"""

exercicio = 'Exercício #025'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

nome = str(input('Qual é seu nome? ')).title().strip()

if 'Silva' in nome:
    print(f'Seu nome é {nome} e você tem Silva no nome.')
else:
    print(f'Seu nome é {nome} e você não tem Silva no nome.')
