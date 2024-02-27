"""Desafio #033"""
"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

exercicio = ' Exercício #033 '
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificando quem é o menor
menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

# Verificando quem é o maior
maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

print(f'O menor valor foi {menor}.')
print(f'O maior valor foi {maior}.')
