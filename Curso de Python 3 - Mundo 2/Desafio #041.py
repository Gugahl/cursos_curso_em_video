"""Desafio #041"""
from datetime import date
"""
A Confederação Nacional da Notação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria de acordo
com a sua idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""

desafio = ' Desafio #041 '
print(f'{desafio:=^30}')
print(' ')

ano = int(input('Em qual ano você nasceu? '))
idade = date.today().year - ano

if idade <= 9:
    print(f'Você está na categoria MIRIM!')

elif 9 < idade <= 14:
    print(f'Você está na categoria INFANTIL!')

elif 14 < idade <= 19:
    print(f'Você está na categoria JÚNIOR!')

elif idade > 19:
    print(f'Você está na categoria SÊNIOR!')
