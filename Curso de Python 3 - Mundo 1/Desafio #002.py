"""DESAFIO 002"""
"""
Crie um script Python que leia o dia, mês e ano de nascimento de uma pessoa e mostre uma mensagem com a data
formatada.
"""

desafio = ' DESAFIO 02 '
print(f'{desafio:=^30}')
dia = input('Dia = ')
mes = input('Mês = ').lower()
ano = input('Ano = ')
print(f'Você nasceu no dia {dia} de {mes} de {ano}. Correto? ')
