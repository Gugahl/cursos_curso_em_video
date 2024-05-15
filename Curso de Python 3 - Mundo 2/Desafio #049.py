"""Desafio #049"""
from time import sleep
"""
Refaça o desafio 009 mostrando a tabuada de um número
que o usuário escolher só que agora utilizando um laço
for.
"""

desafio = ' Desafio #049 '
print(f'{desafio:=^30}')
print(' ')

numero_escolhido = int(input('Escolha um número inteiro: '))
for tabuada in range(1, 11):
    print(f'{tabuada} x {numero_escolhido} =', (tabuada * numero_escolhido))
    sleep(1)
