"""Desafio #086"""
"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela com a formatação completa.
"""

desafio = f'Desafio #086'
print(f'=~' * 15 + f'\n' + f'{desafio:^30}' + f'\n' + f'~=' * 15 + f'\n')

matriz = list()
linha = list()
for li in range(3):
    for col in range(3):
        linha.append(input(f'Digite o valor que está na posição ({col}, {li}): '))
    matriz.append(linha[:])
    linha.clear()

string = ''
for c in range(3):
    if c > 0:
        string += f'\n'
    for l in range(3):
        if l == 0:
            string += f'[{matriz[c][l]:^5}]  '
        elif l == 1:
            string += f'[{matriz[c][l]:^5}]'
        elif l == 2:
            string += f'  [{matriz[c][l]:^5}]'

print(string)
