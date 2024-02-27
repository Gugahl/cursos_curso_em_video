"""Desafio #048"""
from time import sleep
"""
Faça um programa que calcule a soma entre todos os números
ímpares que são múltiplos de três e que se encontram no in-
-tervalo de 1 até 500.
"""

desafio = ' Desafio #048 '
print(f'{desafio:=^30}')
print(' ')

for impar in range(1-1, 500+1):
    if impar % 3 == 0:
        print(impar)
        sleep(0.5)
print('Fim!')
