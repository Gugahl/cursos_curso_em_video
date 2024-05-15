"""DESAFIO 019"""
from random import choice
from time import sleep
"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome do escolhido.
"""

desafio = ' Desafio #019 '
print(f'{desafio:=^30}', '\n')

prof = 'Professor Thiago'
on = 'online'
digi = 'digitando...'
print(f'{prof:^30}')
sleep(1)
print(f'{on:^30}')
sleep(1)
print(f'{digi:^30}')
print(' ')

sleep(2)
res = input('Professor Thiago: Boa noite Dev, pode me ajudar(sim/não)?\n'
            'Dev: ').lower()

if res == 'sim':

    sleep(2)
    print('Dev: Claro professor!')
    sleep(1)
    print('Professor Thiago: Necessito de um programa que eu forneça o nome de quatro alunos, e ele sorteie um dos')
    print('nomes para limpar um quadro.')
    sleep(1),
    print('Dev: Ok, só um momento')
    sleep(1)
    print('Dev: Aqui está sortudo.exe\n')
    sleep(1)

    sort = 'Sorteio'
    print('=' * 30, '\n', f'{sort:^30}', '\n', '=' * 30)

    aluno1 = input('Qual será o nome do primeiro aluno? ').title()
    aluno2 = input('Qual será o nome do segundo aluno? ').title()
    aluno3 = input('Qual será o nome do terceiro aluno? ').title()
    aluno4 = input('Qual será o nome do quarto aluno? ').title()
    lista_alunos = [f'{aluno1}', f'{aluno2}', f'{aluno3}', f'{aluno4}']
    sorte = choice(lista_alunos)
    print(f'O sortudo que irá limpar o quadro será o {sorte}')

elif res == 'não':
    sleep(2)
    print('Dev: Eita prof, vai dar não estou cheio de trabalho')
    sleep(1)
    print('Professor Thiago: Tudo certinho cara, muito obrigado e até a próxima!!')

else:
    print(f'Professor Thiago: Irrelevante, responda da maneira desejada.')
