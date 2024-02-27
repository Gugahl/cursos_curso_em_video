"""Desafio 013"""
"""
Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
"""

exercicio = 'Exercício #013'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

nome = input('Qual é o nome desse funcionário? ').title()
sali = float(input('Qual é o salário atual desse funcionário? R$'))
porci = float(input('Quantos % você deseja dar de aumento para ele(0 a 100)? '))
porcf = porci/100
salf = sali + (sali*porcf)

print(' ')
print('='*25)
print(f'{nome:^25}')
print('='*25)
print(' ')

print(f'O salário atual do funcionário é de: R${sali};\n'
      f'A porcentagem de aumento salarial foi de {porci};%\n'
      f'O salário desse funcionário pós aumento ficou de R${salf}.')
