"""DESAFIO 001"""
"""
Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digita-
do.
"""

desafio = ' DESAFIO 01 '
print(f'{desafio:=^30}')
nome = input('Qual é o seu nome? ').title()
print(f'Olá {nome}! Prazer em te conhecer!')
