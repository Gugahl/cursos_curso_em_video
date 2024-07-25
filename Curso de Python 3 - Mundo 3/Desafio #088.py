"""Desafio #088"""
from random import randint
"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

desafio = f'Desafio #088'
print(f'=~' * 15 + f'\n' + f'{desafio:^30}' + f'\n' + f'~=' * 15 + f'\n')

matriz = list()
palpite = list()
contagem = 0
jogos = int(input(f'Quantos jogos você quer que eu gere? '))
while True:
    contagem += 1
    for c in range(6):
        palpite.append(randint(1, 60))
    matriz.append(palpite[:])
    palpite.clear()
    if contagem == jogos:
        break

print(f'\n{matriz}')
