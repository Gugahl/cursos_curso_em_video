"""Desafio #061"""
"""
Refaça o DESAFIO 051, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.
"""

exercicio = 'Exercício #061'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30 + f'\n')

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razão
    cont += 1
print('FIM.')
