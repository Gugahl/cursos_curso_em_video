"""Desafio #089"""
"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

desafio = f'Desafio #089'
print(f'=~' * 15 + f'\n' + f'{desafio:^30}' + f'\n' + f'~=' * 15 + f'\n')

matriz_media = list()
matriz_notas = list()
aluno = list()
nota = list()
contagem = 0
while True:
    contagem += 1
    if contagem > 1:
        print(' ')

    aluno.append(str(input(f'Digite o nome do {contagem}º aluno: ')).capitalize())
    nota.append(int(input(f'Digite a primeira nota do {contagem}º aluno: ')))
    nota.append(int(input(f'Digite a segunda nota do {contagem}º aluno: ')))

    aluno.append(nota[:])
    matriz_notas.append(aluno[:])

    del(aluno[1])
    media = (nota[0] + nota[1])/2
    aluno.append(media)
    matriz_media.append(aluno[:])

    nota.clear()
    aluno.clear()

    pergunta = input(f'Deseja adicionar mais um aluno? ')[0].upper()
    while pergunta != 'S' and pergunta != 'N':
        pergunta = input(f'ERRO! Deseja adicionar mais um aluno? ')[0].upper()
    if pergunta == 'N':
        break

print(f'\n' + f'=~' * 15 + f'\n' f'{'Boletim':^30}' + f'\n' + f'~=' * 15)

print(f'\n{"Aluno":<10}{"Média":>10}')
for aluno in matriz_media:
    print(f'{aluno[0]:<10}{aluno[1]:>10.2f}')


print(f'\n{"Aluno":<10}{"Notas":>10}')
for aluno in matriz_notas:
    print(f'{aluno[0]:<10}{aluno[1][0]:>5.2f}, {aluno[1][1]:>5.2f}')