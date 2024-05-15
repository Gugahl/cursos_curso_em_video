"""Desafio #055"""
"""
Faça um programa que leia o peso de cinco pessoas. No final 
mostre qual foi o maior e o menor peso lidos.
"""

desafio = ' Desafio #055 '
print(f'{desafio:=^30}', '\n')

lista = []
maior = 0
menor = 0
for comparar_pesos in range(1, 6):
    peso = float(input('Qual é o seu peso? '))
    lista.append(peso)
maior += max(lista)
menor += min(lista)
print(f'O maior peso foi {maior} kg, e o menor peso foi {menor} kg.')
