"""Desafio #063"""
"""
Escreva um programa que leia um número n inteiro
qualquer e mostre na tela os n primeiros elementos
de uma Sequência de Fibonacci.

Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

desafio = 'Desafio #063'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

numero = int(input('Digite um número inteiro: '))
antecessor = numero - 1
soma = numero + antecessor
elementos = 1
while elementos != 11:
    antecessor = soma - antecessor
    soma = soma + antecessor
    elementos += 1
    print(soma)
