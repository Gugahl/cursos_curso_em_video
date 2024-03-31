"""Exercício Python #071 - Simulador de Caixa Eletrônico"""
"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de:
R$200, R$100, R$50, R$20, R$10, R$5 e R$1.
"""
"""
==============================
           BANCO CEV
==============================
Que valor você quer sacar? R$100
Total de 1 cédula de R$100
==============================
Volte sempre ao BANCO CEV! Tenha um bom dia!
"""

exercicio = 'Exercício #071'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30 + f'\n')

banco = 'BANCO CEV'
print(f'=-' * 15 + f'\n' + f'{banco:^30}' + f'\n' + f'=-' * 15)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco CEV! Tenha um bom dia!')
