""""Desafio #028"""
from random import randint
from time import sleep
"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
perdeu.
"""

exercicio = ' Exercício #028 '
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

msg = 'Vou pensar em um número entre 0 e 5. Tente adivinhar...'
computador = randint(0, 5)
print('-=-' * 30)
print(f'{msg:^90}')
print('-=-' * 30, '\n')

jogador = int(input('Ok, em que número pensei? '))

if jogador == computador:
    print('PROCESSANDO...')
    sleep(3)
    print('PARABÉNS!!! Você conseguiu me vencer!')

else:
    print('PROCESSANDO...')
    sleep(3)
    print(f'EU GANHEI!!! Pensei no número {computador} não no número {jogador}.')
