"""Desafio #050"""

"""
Faça um programa que leia seis números inteiros e some apenas aqueles que forem pares, se o valor digitado for ímpar, desconsidere.
"""

desafio = ' Desafio #050 '
print(f'{desafio:=^39}', '\n')

soma = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print(f'A soma foi: {soma}')
        