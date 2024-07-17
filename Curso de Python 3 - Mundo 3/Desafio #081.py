"""Desafio #081"""
"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

desafio = f'Desafio #081'
print(f'=~' * 15 + f'\n' + f'{desafio:^30}' + f'\n' + f'~=' * 15)

cont = cinco = 0
valores = []
while True:
    cont += 1
    num = int(input(f'Digite o {cont}º número: '))
    valores.append(num)
    if num == 5:
        cinco += 1
    pergunta = input('Deseja continuar? [S/N] ')[0].upper()
    while pergunta != 'S' and pergunta != 'N':
        pergunta = input('Deseja continuar? [S/N] ')[0].upper()
    if pergunta == 'N':
        break

valores.sort(reverse=True)
print(f'Você digitou {cont} números.')
print(f'A lista em ordem decrescente foi: {valores}')
print(f'Foram digitados {cinco} valores 5 na lista.' if cinco > 0 else f'Não foi encontrado nenhum 5 na lista.')
