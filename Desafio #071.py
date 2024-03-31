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

desafio = 'Desafio #071'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

banco = 'Banco CEV'
print(f'=-' * 15 + f'\n' + f'{banco:^30}' + f'\n' + f'=-' * 15)

valor = int(input('Que valor você quer sacar? R$'))
resto = valor
contador_de_cedulas = cedula_de_200 = cedula_de_100 = cedula_de_50 = cedula_de_20 = cedula_de_10 = cedula_de_5 = cedula_de_1 = 0
while resto > 0:
    if resto - 200 >= 0:
        contador_de_cedulas += 1
        cedula_de_200 += 1
        resto -= 200
    elif resto - 100 >= 0:
        contador_de_cedulas += 1
        cedula_de_100 += 1
        resto -= 100
    elif resto - 50 >= 0:
        contador_de_cedulas += 1
        cedula_de_50 += 1
        resto -= 50
    elif resto - 20 >= 0:
        contador_de_cedulas += 1
        cedula_de_20 += 1
        resto -= 20
    elif resto - 10 >= 0:
        contador_de_cedulas += 1
        cedula_de_10 += 1
        resto -= 10
    elif resto - 5 >= 0:
        contador_de_cedulas += 1
        cedula_de_5 += 1
        resto -= 5
    elif resto - 1 >= 0:
        contador_de_cedulas += 1
        cedula_de_1 += 1
        resto -= 1
print(f'Total de {contador_de_cedulas} cédula;' if 0 < contador_de_cedulas < 2 else f'Total de {contador_de_cedulas} cédulas;')
print(f'Sendo: ')
if cedula_de_200 > 0:
    print(f'{cedula_de_200} cédula de 200;' if 0 < cedula_de_200 < 2 else f'{cedula_de_200} cédulas de 200;') 
else:
    print(end='')

if cedula_de_100 > 0:
    print(f'{cedula_de_100} cédula de 100;' if 0 < cedula_de_100 < 2 else f'{cedula_de_100} cédulas de 100;') 
else:
    print(end='')

if cedula_de_50 > 0:
    print(f'{cedula_de_50} cédula de 50;' if 0 < cedula_de_50 < 2 else f'{cedula_de_50} cédulas de 50;') 
else:
    print(end='')

if cedula_de_20 > 0:
    print(f'{cedula_de_20} cédula de 20;' if 0 < cedula_de_20 < 2 else f'{cedula_de_20} cédulas de 20;') 
else:
    print(end='')

if cedula_de_10 > 0:
    print(f'{cedula_de_10} cédula de 10;' if 0 < cedula_de_10 < 2 else f'{cedula_de_10} cédulas de 10;') 
else:
    print(end='')

if cedula_de_5 > 0:
    print(f'{cedula_de_5} cédula de 5;' if 0 < cedula_de_5 < 2 else f'{cedula_de_5} cédulas de 5;') 
else:
    print(end='')

if cedula_de_1 > 0:
    print(f'{cedula_de_1} cédula de 1;' if 0 < cedula_de_1 < 2 else f'{cedula_de_1} cédulas de 1;') 
else:
    print(end='')
