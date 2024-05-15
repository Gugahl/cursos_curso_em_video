"""Desafio #045"""
import random
"""
Crie um programa que faça o computador jogar Jokenpô
com você.
"""

desafio = ' Desafio #045 '
print(f'{desafio:=^30}')
print(' ')

msg = ('Japa: Vamos jogar Jokenpô\n'
       'Japa: Joookeeenp...\n')
jokenpo = ['Pedra', 'Papel', 'Tesoura']
japa = random.choice(jokenpo)
print(f'{msg}')
voce = str(input('(Escolha entre Pedra, Papel e Tesoura)\n'
                 'Você: ')).lower().strip()

if voce == 'pedra':
    if japa == 'Pedra':
        print('Japa: \033[33mDroga!\033[m Empatamos!')

    elif japa == 'Papel':
        print('Japa: \033[32mBoa!\033[m Ganhei!')

    elif japa == 'Tesoura':
        print('Japa: \033[31mAAAA!\033[m Eu perdi, que droga!')

elif voce == 'papel':
    if japa == 'Pedra':
        print('Japa: \033[31mAAAA!\033[m Eu perdi, que droga!')

    elif japa == 'Papel':
        print('Japa: \033[33mDroga!\033[m Empatamos!')

    elif japa == 'Tesoura':
        print('Japa: \033[32mBoa!\033[m Ganhei!')

elif voce == 'tesoura':
    if japa == 'Pedra':
        print('Japa: \033[32mBoa!\033[m Ganhei!')

    elif japa == 'Papel':
        print('Japa: \033[31mAAAA!\033[m Eu perdi, que droga!')

    elif japa == 'Tesoura':
        print('Japa: \033[33mDroga!\033[m Empatamos!')