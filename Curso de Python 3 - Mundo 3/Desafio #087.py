"""Desafio #087"""
"""
Aprimore o desafio anterior mostrando no final:

A) A soma de todos os valores pares digitados

B) A soma dos valores da terceira coluna

C) O maior valor da segunda linha
"""

desafio = f'Desafio #087'
print(f'=~' * 15 + f'\n' + f'{desafio:^30}' + f'\n' + f'~=' * 15 + f'\n')

matriz = list()
linha = list()
soma_totalpares = soma_3coluna = maior_valor_2linha = 0
for col in range(3):
    for li in range(3):
        valor = int(input(f'Digite o valor que está na posição ({col}, {li}): '))
        if valor % 2 == 0:
            soma_totalpares += valor
        if li == 1:
            if col == 0 or valor > maior_valor_2linha:
                maior_valor_2linha = valor
        if li == 2:
            soma_3coluna += valor
        linha.append(valor)
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

print(f'\n{string}')

print(f'\nA soma de todos os números pares resultou em: {soma_totalpares}')
print(f'A soma de todos os valores da terceira coluna resultou em: {soma_3coluna}')
print(f'O maior valor registrado na segunda linha foi: {maior_valor_2linha}')
