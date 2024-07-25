"""Exercício Python #084 - Lista composta e análise de dados"""
"""
Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista.
No final mostre:

A) Quantas pessoas foram cadastradas.

B) Uma listagem com a(s) pessoa(s) mais pesada(s).

C) Uma listagem com as pessoas mais leves.
"""

exercicio = f'Exercício Python #084'
print(f'=~' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'~=' * 15 + f'\n')

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input(f'Nome: ')))
    temp.append(float(input(f'Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input(f'Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print(f'~=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai} quilos. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men} quilos. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')

