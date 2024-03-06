"""Desafio #051"""
"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final mostre os 10 primeiros termos dessa progressão.
"""

exercicio = ' Exercício #051 '
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

termos_pa = '10 TERMOS DA PA'
print('-=' * 15)
print(f'{termos_pa:^30}')
print('-=' * 15, '\n')

primeiro_termo = int(input('Me forneça o primeiro valor da PA: '))
razao_pa = int(input('Me forneça a razão da PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao_pa
for c in range(primeiro_termo, decimo_termo + razao_pa, razao_pa):
    print(f'{c}', end=' -> ')
print('Acabou')
