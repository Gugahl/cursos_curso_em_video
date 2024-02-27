"""Desafio #052"""
"""
Faça um programa que leia um número inteiro e diga se ele é ou não é um número primo;
"""

desafio = ' Desafio #052 '
print(f'{desafio:=^30}', '\n')

numero = int(input('Me forneça um número: '))
for c in range(1, int(numero**0.5) + 1):
    if numero % c == 0:
        print('Esse número é primo')
        
    else:
        print('Esse número não é primo')
    
