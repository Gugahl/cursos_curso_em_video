"""Desafio #085"""
"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final mostre os valores pares e ímpares em ordem crescente.
"""

desafio = f'Desafio #085'
print(f'=~' * 15 + f'\n' + f'{desafio:^30}' + f'\n' + f'~=' * 15 + f'\n')

pares = list()
impares = list()
matriz = list()
for contagem in range(7):
    num = int(input(f'Digite o {contagem + 1}º valor: '))

    if num % 2 == 0:
        pares.append(num)

    else:
        impares.append(num)

pares = sorted(pares)
impares = sorted(impares)

matriz.append(pares[:])
matriz.append(impares[:])
print(f'\nA matriz inteira foi: {matriz}')
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
