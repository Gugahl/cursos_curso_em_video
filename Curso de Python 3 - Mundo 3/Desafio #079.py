"""Desafio #079"""
"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados em ordem crescente.
"""

desafio = "Desafio #079"
print(f"-=" * 15 + f"\n" + f"{desafio:^30}" + f"\n" + f"-=" * 15)

cont = 0
lista = []
while True:
    cont += 1
    num = int(input(f'Digite o {cont}º número: '))
    if num not in lista:
        lista.append(num)
    elif num in lista:
        print(f'{num} já foi computado, tente outro número.')
    pergunta = input('Deseja continuar? [S/N] ')[0].upper()
    while pergunta != 'S' and pergunta != 'N':
        pergunta = input('[ERRO!] Deseja continuar? [S/N] ')[0].upper()
    if pergunta == 'N':
        break

lista.sort()
print(f'{lista}')
