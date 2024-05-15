"""Desafio #057"""
"""
Faça um programa que leia o sexo de uma pessoa, mas
só aceite os valores 'M' ou 'F'. Caso esteja errado
peça a digitação novamente até ter o valor correto.
"""

desafio = 'Desafio #057'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

nome = str(input(f'Qual é o seu nome? ')).strip().title()
sexo = str(input(f'Qual é o seu sexo biológico?'
                f'(M - para homens; F - para mulheres): ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print(f'Entrada inválida!')
    sexo = str(input(f'Qual é o seu sexo biológico?'
                f'(M - para homens; F - para mulheres): ')).strip().upper()

if sexo == 'M':
    print(f'Seja bem vindo {nome}!')
if sexo == 'F':
    print(f'Seja bem vinda {nome}!')
