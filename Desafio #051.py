"""Desafio #051"""
from time import sleep
"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final mostre os 10 primeiros termos dessa progressão.
"""

desafio = ' Desafio #051 '
print(f'{desafio:=^30}', '\n')

numero_inicial = int(input('Qual o número inicial dessa PA? '))
razao_da_pa = int(input('Qual a razão dessa PA? '))
for c in range(numero_inicial, numero_inicial + 10 * razao_da_pa, razao_da_pa):
    print(c)
    sleep(1)
print('FIM!')
