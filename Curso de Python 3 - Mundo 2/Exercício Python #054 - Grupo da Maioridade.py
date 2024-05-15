"""Desafio #054"""
from datetime import date
"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.
"""

exercicio = ' Exercício #054 '
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

ano_atual = date.today().year
numero_de_maiores_de_idade = 0
numero_de_menores_de_idade = 0
for pessoa in range(1, 8):
    ano_de_nascimento = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade = ano_atual - ano_de_nascimento
    if idade >= 21:
        numero_de_maiores_de_idade += 1
    else:
        numero_de_menores_de_idade += 1
print(f'\n'
    f'Ao todo tivemos {numero_de_maiores_de_idade} pessoas maiores de idade e\n'
    f'{numero_de_menores_de_idade} pessoas menores de idade.')
