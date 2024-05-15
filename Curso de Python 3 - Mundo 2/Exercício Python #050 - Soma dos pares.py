"""Desafio #050"""

"""
Faça um programa que leia seis números inteiros e some apenas aqueles que forem pares, se o valor digitado for ímpar, desconsidere.
"""

exercicio = ' Exercício #050 '
print(f'-=' * 15)
print(f'{exercicio:^30}')
print(f'-=' * 15, '\n')

soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c}º valor: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f'Você informou seis valores, desses {cont} eram números pares, a soma deles foi igual a: {soma}.')
