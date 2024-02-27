"""Desafio 023"""
"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""

desafio = ' Desafio #023 '
print(f'{desafio:=^30}', '\n')

numero = input('Digite um número inteiro: ')
print(' ')
print('Com strings: ')

print(f'Unidade: {numero[-1]}')
print(f'Dezena: {numero[-2:-1]}')
print(f'Centena: {numero[-3:-2]}')
print(f'Milhar: {numero[-4:-3]}')

numero2 = int(numero)
print(' ')
print('Com int(): ')
print(f'Unidade: {numero2 % 10}')
print(f'Dezena: {(numero2 // 10) % 10}')
print(f'Centena: {(numero2 // 100) % 10}')
print(f'Milhar: {(numero2 // 1000) % 10}')
