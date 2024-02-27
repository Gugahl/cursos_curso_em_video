"""Desafio 002"""
"""
Faça um programa que leia um nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""

exercicio = 'Exercício #002'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

nome = input('Digite seu nome: ').title()
print(f'É um prazer te conhecer, {nome}!')
