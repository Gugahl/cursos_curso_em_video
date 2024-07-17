"""Desafio #082"""
"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
No final mostre o conteúdo das três listas geradas.
"""

desafio = f'Desafio #082'
print(f'~=' * 15 + f'\n' + f'{desafio:^30}' + f'\n' + f'=~' * 15)

cont = 0
valores = []
pares = []
impares = []
while True:
    cont += 1
    num = int(input(f'Digite o {cont}º número: '))
    valores.append(num)
    pergunta = input('Deseja continuar? [S/N] ')[0].upper()
    while pergunta != 'S' and pergunta != 'N':
        pergunta = input('[ERRO!]Deseja continuar? [S/N] ')[0].upper()
    if pergunta == 'N':
        break

for i, num in enumerate(valores):
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)


print(valores)
print(pares)
print(impares)
