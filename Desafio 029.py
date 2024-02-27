"""Desafio #029"""
import time
"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado

A multa vai custar R$7.00 por cada Km acima do limite.
"""

desafio = ' Desafio #029 '
print(f'{desafio:=^30}', '\n')

pov = 'De - Assistente do Detran'
mensagem = 'Sistema de Calculo de Multas do Detran AL'
print('=' * 30)
print(f'{pov:^30}')
print('=' * 30, '\n')
time.sleep(3)
print(f'{mensagem}', '\n')
velocidade = float(input('A quantos Km/h você estava? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você irá pagar R${multa} de multa.')

else:
    print(f'Parabéns por respeitar o limite da via!')
