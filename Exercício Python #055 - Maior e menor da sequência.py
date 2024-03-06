"""Desafio #055"""
"""
Faça um programa que leia o peso de cinco pessoas. No final 
mostre qual foi o maior e o menor peso lidos.
"""

exercicio = ' Exercício #055 '
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Qual é o peso da {p}ª pessoa? '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi: {maior} kg.')
print(f'O menor peso lido foi: {menor} kg.')
