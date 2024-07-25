"""Exercício Python #086 - Matriz em Python"""
"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela com a formatação completa.
"""

exercicio = f'Exercício Python #086'
print(f'=~' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'~=' * 15 + f'\n')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print(f'~=' * 30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
