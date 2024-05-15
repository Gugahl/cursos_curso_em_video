"""Desafio 027"""
"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Gustavo Henrique Lima Santos
Primeiro nome: Gustavo
Último sobrenome: Santos
"""

desafio = ' Desafio #027 '
print(f'{desafio:=^30}', '\n')

nome_completo = input('Qual é o seu nome completo? ').title()
nome_separado = nome_completo.split()
primeiro_nome = nome_separado[0]
ultimo_sobrenome = nome_separado[len(nome_separado)-1]
print(f'Seu primeiro nome é {primeiro_nome};')
print(f'Seu último sobrenome é {ultimo_sobrenome}.')
