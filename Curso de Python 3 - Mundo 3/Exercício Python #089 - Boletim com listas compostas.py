"""Exercício Python #089 - Boletim com listas compostas"""
"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

exercicio = f'Exercício Python #089'
print(f'=~' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'~=' * 15 + f'\n')

ficha = list()
while True:
    nome = str(input(f'Nome: '))
    nota1 = float(input(f'Nota 1: '))
    nota2 = float(input(f'Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input(f'Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'~=' * 30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print(f'~=' * 13)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    print(f'-' * 35)
    opc = int(input(f'Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print(f'FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print(f'<<< VOLTE SEMPRE >>>')
