"""Desafio 019"""
from random import choice
"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome do escolhido.
"""

exercicio = 'Exercício #019'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

print('Programa: Digite o número de quatro alunos para que eu possa sortear um deles para limpar o quadro hoje.')
aluno_1 = input('Nome do primeiro aluno: ').title()
aluno_2 = input('Nome do segundo aluno: ').title()
aluno_3 = input('Nome do terceiro aluno: ').title()
aluno_4 = input('Nome do quarto aluno: ').title()
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
sorte = choice(lista)
print(f'A pessoa que irá limpar o quadro será o@: {sorte}')
