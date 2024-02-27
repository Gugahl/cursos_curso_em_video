"""DESAFIO 005"""
"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

desafio = ' DESAFIO 005 '
print(f'{desafio:=^30}')

num = int(input('Me forneça um número inteiro: '))
print(f'Seu número foi {num} \n Seu sucessor é: {num+1}', end=' e ')
print(f'seu antecessor é: {num-1}.')
