"""Desafio #031"""
"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem cobrando R$0.50 por Km para viagens até 200Km
e R$0.45 para viagens mais longas.
"""

desafio = ' Desafio #031 '
print(f'{desafio:=^60}', '\n')

msg = 'CalBus - Calcule o valor da sua viagem aqui!'

print(f'=' * 60)
print(f'{msg:^60}')
print(f'=' * 60, '\n')

distancia = float(input('Sua viagem será de quantos quilômetros? '))
print(' ')
ateduzentos = distancia * 0.5
superduzentos = distancia * 0.45
print(f'Sua viagem custar R${ateduzentos}' if distancia <= 200 else f'Sua viagem vai custar R${superduzentos}')
