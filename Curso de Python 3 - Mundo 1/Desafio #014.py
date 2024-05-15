"""DESAFIO 014"""
"""
Escreva um programa que converta uma temperatura digitada em graus celsius para graus farenheit.
"""

desafio = ' DESAFIO 014 '
print(f'{desafio:=^30}\n')

term = 'Termometro'
print('=' * 30)
print(f'{term:^30}')
print('=' * 30)
print(' ')

cel = float(input('Informe a temperatura em graus celsius (ºC): '))
far = cel*1.8+32
kel = cel + 273.15

print(f'A temperatura {cel}ºC, convertida para farenheit fica {far}ºF e para kelvin fica {kel}ºK.')
