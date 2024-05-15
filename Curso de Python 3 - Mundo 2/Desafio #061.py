"""Desafio #061"""
"""
Refaça o DESAFIO 051, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.
"""

desafio = 'Desafio #061'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

numero_inicial = int(input('Qual o número inicial dessa PA? '))
razao_da_pa = int(input('Qual a razão dessa PA? '))
contagem = 1
termo = numero_inicial
print(' ')
while contagem < 11:
    print(f'{termo} --> {contagem}º termo;')
    termo += razao_da_pa
    contagem += 1
