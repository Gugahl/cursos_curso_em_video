"""Desafio #045"""
from random import choice
from time import sleep
"""
Crie um programa que faça o computador jogar Jokenpô
com você.
"""

exercicio = 'Exercício #045'
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

pc = choice(['Pedra', 'Papel', 'Tesoura'])
print('Computador: Vamos jogar Pedra, Papel e Tesoura')
sleep(2)
print('Computador: Será que você consegue me vencer?')
sleep(2)
print(' ')
print('JOOO')
sleep(2)
print('KEEEN')
escolha = input('Qual é a sua escolha(Pedra, Papel ou Tesoura)? ').lower().title().strip()
sleep(2)
print('PÔOO!!!')
print(' ')
escolha_pc = f'O computador escolheu {pc}.'
escolha_user = f'O usuário escolheu {escolha}.'
print('-=' * 15)
print(f'{escolha_pc:^30}')
print(f'{escolha_user:^30}')
print('-=' * 15, '\n')

if escolha == 'Pedra':
    if pc == 'Pedra':
        print('Computador: \033[33mEmpatamos\033[m!')
        print('Jogador empata com a máquina!')

    elif pc == 'Papel':
        print('Computador: \033[32mGanhei\033[m!')
        print('Jogador perde!')

    elif pc == 'Tesoura':
        print('Computador: \033[31mPerdi\033[m!')
        print('Jogador vence!')

elif escolha == 'Papel':
    if pc == 'Papel':
        print('Computador: \033[33mEmpatamos\033[m!')
        print('Jogador empata com a máquina!')

    elif pc == 'Tesoura':
        print('Computador: \033[32mGanhei\033[m!')
        print('Jogador perde!')

    elif pc == 'Pedra':
        print('Computador: \033[31mPerdi\033[m!')
        print('Jogador vence!')

elif escolha == 'Tesoura':
    if pc == 'Tesoura':
        print('Computador: \033[33mEmpatamos\033[m!')
        print('Jogador empata com a máquina!')

    elif pc == 'Pedra':
        print('Computador: \033[32mGanhei\033[m!')
        print('Jogador perde!')

    elif pc == 'Papel':
        print('Computador: \033[31mPerdi\033[m!')
        print('Jogador vence!')

else:
    print('Computador: \033[31mJogada inválida!\033[m Escolha entre (Pedra, Papel ou Tesoura)')
