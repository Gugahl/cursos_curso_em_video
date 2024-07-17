"""Exercício Python #082 - Dividindo valores em várias listas"""
"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
No final mostre o conteúdo das três listas geradas.
"""

exercicio = f'Exercício Python #082'
print(f'=~' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'~=' * 15)

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('~=' * 30)
print(f'A lista completa é: {num}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')
