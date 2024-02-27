"""Desafio #046"""
from time import sleep
"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro 
de fogos de artifícios, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

exercicio = 'Desafio #046'
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

for contagem in range(10, 0, -1):
    print(f'{contagem}')
    sleep(0.5)
print('BUM, BUM POW!')
