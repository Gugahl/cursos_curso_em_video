"""Desafio #047"""
"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50;
"""

exercicio = ' Exercício #047 '
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')
