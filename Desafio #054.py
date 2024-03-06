"""Desafio #054"""
from datetime import date
"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.
"""

desafio = ' Desafio #054 '
print(f'{desafio:=^30}', '\n')

maiores = 0
menores = 0
for ano in range(1, 8):
    ano_de_nascimento = int(input('Qual foi o ano do seu nascimento? '))
    if date.today().year - ano_de_nascimento >= 21:
        maiores += 1
    else:
        menores += 1
print(f'{maiores} pessoas atingiram a maioridade, {menores} pessoas ainda não atingiram.')
