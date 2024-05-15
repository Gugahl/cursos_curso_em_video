"""Desafio #035"""
"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

desafio = ' Desafio #035 '
print(f'{desafio:=^30}', '\n')

cop = float(input('Qual é o valor do primeiro lado? '))
ca = float(input('Qual é o valor do segundo lado? '))
h = float(input('Qual é o valor do terceiro lado? '))

if cop+ca > h and ca+h > cop and cop+h > ca:
    print('É possível criar um triângulo com esses valores.')

else:
    print('Não é possível criar um triângulo com esses valores.')
