"""Desafio #038"""
"""
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais 
"""

desafio = ' Desafio #038 '
print(f'{desafio:=^30}')
print(' ')

valor1 = int(input('Me forneça um valor inteiro: '))
valor2 = int(input('Me forneça um segundo valor inteiro: '))

if valor1 > valor2:
    print('O primeiro valor é maior.')

elif valor2 > valor1:
    print('O segundo valor é maior.')

elif valor1 == valor2:
    print('Não existe valor maior, os dois são iguais.')
