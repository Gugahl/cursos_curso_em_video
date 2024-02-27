"""Desafio 007"""
"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média. OBS: A média só poderá ter uma
casa decimal após o ponto.
"""

exercicio = 'Exercício #007'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

be = ' Boletim Eletrônico '
print(f'{be:=^30}\n')

n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota? '))
print(f' \n'
      f'A média entre {n1} e {n2} é igual a {((n1+n2)/2):.1f}')
