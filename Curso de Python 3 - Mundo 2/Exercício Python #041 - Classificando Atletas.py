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

exercicio = 'Exercício #041'
print('-=' * 30)
print(f'{exercicio:^30}')
print('-=' * 30, '\n')

ano_de_nascimento = int(input('Qual o ano de nascimento do atleta? '))
idade_do_atleta = date.today().year - ano_de_nascimento

print(f'O atleta tem {idade_do_atleta} anos.')
if idade_do_atleta <= 9:
    print(f'Classificação: MIRIM')

elif idade_do_atleta <= 14:
    print(f'Classificação: INFANTIL')

elif idade_do_atleta <= 19:
    print(f'Classificação: JUNIOR')

elif idade_do_atleta == 20:
    print(f'Classificação: SÊNIOR')
    
else:
    print(f'Classificação: MASTER')
