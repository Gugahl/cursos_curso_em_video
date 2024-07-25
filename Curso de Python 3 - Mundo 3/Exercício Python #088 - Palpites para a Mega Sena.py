"""Exercício Python #088 - Palpites para a Mega Sena"""
from random import randint
from time import sleep
"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

exercicio = f'Exercício Python #088'
print(f'=~' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'~=' * 15 + f'\n')

lista = list()
jogos = list()
print(f'~=' * 15)
print(f'{'JOGA NA MEGA SENA':^30}')
print(f'~=' * 15)
quant = int(input(f'Quantos jogos você quer que eu faça? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'~=' * 3 + f' SORTEANDO {quant} JOGOS ' + f'~=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print(f'~=' * 5 + f'< BOA SORTE! >' + f'~=' * 5)
