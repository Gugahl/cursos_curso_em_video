"""Desafio #027"""
"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Gustavo Henrique Lima Santos
Primeiro nome: Gustavo
Último sobrenome: Santos
"""

exercicio = 'Exercício #027'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

nome_completo = input('Me diga o seu nome completo: ').title()
nome_separado = nome_completo.split()
ultimo_sobrenome = nome_separado[len(nome_separado)-1]
print(f'Seu primeiro nome é {nome_separado[0]};')
print(f'Seu último sobrenome é {ultimo_sobrenome}.')
