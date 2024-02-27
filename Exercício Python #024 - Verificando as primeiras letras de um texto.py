"""Desafio 024"""
"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""

exercicio = 'Exercício #024'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

cidade = input('Digite o nome de uma cidade: ').title()
primeiro_nome_cidade = (cidade.split())[0]

if 'Santo' in primeiro_nome_cidade:
    print(f'A cidade {cidade} começa com Santo.')

else:
    print(f'A cidade {cidade} NÂO começa com Santo.')
