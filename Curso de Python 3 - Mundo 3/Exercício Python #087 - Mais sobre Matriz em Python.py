"""Exercício Python #087 - Mais sobre Matriz em Python"""
"""
Aprimore o desafio anterior mostrando no final:

A) A soma de todos os valores pares digitados

B) A soma dos valores da terceira coluna

C) O maior valor da segunda linha
"""

exercicio = f'Exercício Python #087'
print(f'=~' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'~=' * 15 + f'\n')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print(f'~=' * 30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'~=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
