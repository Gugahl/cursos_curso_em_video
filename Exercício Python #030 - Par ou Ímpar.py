"""Desafio #030"""
"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR
"""

exercicio = ' Exercício #030 '
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

num = int(input(f'Escolha um número inteiro: '))
divisao = num / 2

print(f'O número {num} é PAR!' if divisao == int(divisao) else f'O número {num} é ÍMPAR!')
