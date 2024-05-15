"""Desafio #046"""
from time import sleep
"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro 
de fogos de artifícios, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

desafio = ' Desafio #046 '
print(f'{desafio:=^30}')
print(' ')

print('Contagem regressiva:')
for contagem in range(10, 0, -1):
    print(f'{contagem}')
    sleep(1)
print(f'FELIZ ANO NOVO!')
