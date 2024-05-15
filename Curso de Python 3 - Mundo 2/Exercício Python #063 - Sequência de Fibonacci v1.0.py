"""Desafio #063"""
"""
Escreva um programa que leia um número n inteiro
qualquer e mostre na tela os n primeiros elementos
de uma Sequência de Fibonacci.

Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

exercicio = 'Exercício #063'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30 + f'\n')

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('-' * 30)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~' * 30)
