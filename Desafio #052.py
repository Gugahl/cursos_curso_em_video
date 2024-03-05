"""Desafio #052"""
"""
Faça um programa que leia um número inteiro e diga se ele é ou não é um número primo;
"""

desafio = ' Desafio #052 '
print(f'{desafio:=^30}', '\n')
numero_de_divisores = 0
numero = int(input('Me forneça um número: '))
for divisores in range(2, numero + 1):
    if numero % divisores == 0:
        numero_de_divisores += divisores
        if numero_de_divisores == numero:
            print(f'O número {numero} é primo.')
        elif numero_de_divisores > numero:
            print(f'O número {numero} é composto.')
if numero == 1:
    print(f'O número {numero} não é primo e nem composto.')
    
