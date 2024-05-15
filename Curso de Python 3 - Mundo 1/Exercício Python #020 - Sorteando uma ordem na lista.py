"""Desafio 020"""
from random import shuffle
from random import sample
"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

# Utilizando o shuffle

exercicio = 'Exercício #020'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

print('Programa: Escolha um grupo e digite seus quatro integrantes para que eu possa '
      '\nsortear a ordem de apresentação.\n')
primeiro_aluno = input('Qual é o nome do primeiro aluno? ').title()
segundo_aluno = input('Qual é o nome do segundo aluno? ').title()
terceiro_aluno = input('Qual é o nome do terceiro aluno? ').title()
quarto_aluno = input('Qual é o nome do quarto aluno? ').title()
grupo = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
shuffle(grupo)
print(' ')
print(f'Programa: A ordem de apresentação desse grupo ficou: {grupo}.')

# Utilizando o sample

desafio = 'DESAFIO 020'
print('=' * 30, '\n', f'{desafio:^30}')
print('=' * 30, '\n')

print('Programa: Escolha um grupo e digite seus quatro integrantes para que eu possa\n'
      'sortear a ordem de apresentação.\n')

primeiro_aluno = input('Qual é o nome do primeiro aluno? ').title()
segundo_aluno = input('Qual é o nome do segundo aluno? ').title()
terceiro_aluno = input('Qual é o nome do terceiro aluno? ').title()
quarto_aluno = input('Qual é o nome do quarto aluno? ').title()
grupo = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]

lista_sorteada = sample(grupo, k=len(grupo))

print(' ')
print(f'Programa: A ordem de apresentação desse grupo ficou: {lista_sorteada}.')
