"""Desafio 025"""
"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

desafio = ' Desafio #025 '
print(f'{desafio:=^30}', '\n')

nome = input('Qual é seu nome? ').title()

if 'Silva' in nome:
    print(f'Seu nome é {nome} e você tem Silva no nome.')
else:
    print(f'Seu nome é {nome} e você não tem Silva no nome.')
