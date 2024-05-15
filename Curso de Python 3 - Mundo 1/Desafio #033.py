"""Desafio #033"""
"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

desafio = ' Desafio #033 '
print(f'{desafio:=^30}', '\n')

msg = 'Comparador'

print('=' * 30)
print(f'{msg:^30}')
print('=' * 30, '\n')

numero1 = float(input('Me forneça o primeiro número: '))
numero2 = float(input('Me forneça o segundo número: '))
numero3 = float(input('Me forneça o terceiro número: '))
print(' ')

if numero1 > numero2 and numero1 > numero3:
    print(f'O número {numero1} é o maior.')

if numero2 > numero1 and numero2 > numero3:
    print(f'O número {numero2} é o maior.')

if numero3 > numero1 and numero3 > numero2:
    print(f'O número {numero3} é o maior.')

if numero1 < numero2 and numero1 < numero3:
    print(f'O número {numero1} é o menor.')

if numero2 < numero1 and numero2 < numero3:
    print(f'O número {numero2} é o menor.')

if numero3 < numero2 and numero3 < numero1:
    print(f'O número {numero3} é o menor.')
