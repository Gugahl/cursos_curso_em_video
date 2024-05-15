"""Desafio 010"""
"""
Crie um programa que leia quantos reais uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere U$1.00 = R$4,89
"""

exercicio = 'Exercício #010'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

re = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${re}, você pode comprar U${(re/4.89):.2f}')
