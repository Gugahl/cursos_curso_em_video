"""Desafio #029"""
from time import sleep
"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.
"""

exercicio = ' Exercício #029 '
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(' ')
    print(f'MULTADO! Você ultrapassou o limite da via que é 80Km/h.'
          f'\n Processando sua multa...')
    sleep(3)
    print(' ')
    print(f'Você deverá pagar R${multa:.2f}')

else:
    print(' ')
    print('Tudo ok cidadão, muito obrigado por seguir as leis.')

print('Tenha um bom dia! Dirija com segurança!')
