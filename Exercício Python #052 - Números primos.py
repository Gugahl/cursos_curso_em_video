"""Desafio #052"""
"""
Faça um programa que leia um número inteiro e diga se ele é ou não é um número primo;
"""

exercicio = ' Exercício #052 '
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

numero = int(input('Me forneça um valor: '))
total_de_divisores = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        total_de_divisores += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {numero} foi divisível {total_de_divisores} vezes.')
if total_de_divisores == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo.')
