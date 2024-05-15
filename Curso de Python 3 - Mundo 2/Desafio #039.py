"""Desafio #039"""
from datetime import date
"""
Faça um programa que leia o ano de nascimento de um jovem
e informe de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

desafio = ' Desafio #039 '
print(f'{desafio:=^30}')
print(' ')

ano = int(input('Em que ano você nasceu? '))

if date.today().year - ano < 18:
    print(f'Ainda não chegou o ano de se alistar no serviço militar. Faltam {date.today().year - ano} anos.')

elif date.today().year - ano == 18:
    print('É ano de se alistar no serviço militar, você tem seis meses a partir do dia 01 de janeiro.')

elif date.today().year - ano > 18:
    print(f'Já passou do ano de se alistar no serviço militar. Era para você ter se alistado há '
          f'{date.today().year - (ano + 18)} anos.')
