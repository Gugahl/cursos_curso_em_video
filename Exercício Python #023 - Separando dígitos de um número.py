"""Desafio 023"""
"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex:
Digite um número: 1834
Unidade: 4 Dezena: 3 Centena: 8 Milhar: 1
"""

exercicio = 'Exercício #023'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

num = int(input('Digite um número(entre 0 e 9999): '))
n = str(num)
print(f'Analisando o número {num}...\n'
      f'Unidade: {n[0]};\n'
      f'Dezena: {n[1]};\n'
      f'Centena: {n[2]};\n'
      f'Milhar: {n[3]}.')
