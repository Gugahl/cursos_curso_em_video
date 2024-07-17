"""Desafio #080"""
"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final mostre a lista ordenada na tela.
"""

desafio = f'Desafio #080'
print(f'=~' * 15 + f'\n' + f'{desafio:^30}' + f'\n' + f'~=' * 15)

lista = []
for c in range(5):
    num = int(input(f'Digite o {c + 1}º valor: '))
    if c == 0 or num >= lista[-1]:
        lista.append(num)
    for pos, numero in enumerate(lista):
        if num < numero:
            lista.insert(pos, num)
            print(f'Valor {num} adicionado no índice {pos}.')
            break

print(lista)
