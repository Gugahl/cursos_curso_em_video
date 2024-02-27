"""Desafio 005"""
"""
Faça um programa que leia um número inteiro e mostre na tela seu antecessor e seu sucessor.
"""

exercicio = 'Exercício #005'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

n = int(input('Digite um número inteiro: '))
print(f'Analisando o valor {n}, seu antecessor é {n-1} e seu sucessor é {n+1}.')
