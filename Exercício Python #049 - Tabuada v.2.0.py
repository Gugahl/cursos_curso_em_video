"""Desafio #049"""
from time import sleep
"""
Refaça o desafio 009 mostrando a tabuada de um número
que o usuário escolher só que agora utilizando um laço
for.
"""

exercicio = ' Exercício #049 '
print(f'-=' * 15)
print(f'{exercicio:^30}')
print(f'-=' * 15, '\n')

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c:2}')
    