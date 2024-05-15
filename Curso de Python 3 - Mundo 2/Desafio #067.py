"""Exercício Python #067 - Tabuada v3.0"""
"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para
cada valor digitado pelo usuário. O programa será interrompido quando o número
solicitado for negativo.
"""
"""
Quer ver a tabuada de qual valor? 3
------------------------------
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
------------------------------
"""

desafio = 'Desafio #067'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

continuar = 'S'
c = 0
while continuar == 'S':
    valor = int(input(f'Quer ver a tabuada de qual valor? '))
    print(f'-' * 30 + f'\n', end='')
    if valor < 0:
        break
    while c < 10:
        c += 1
        print(f'{valor} x {c} = {valor*c}')
    print(f'-' * 30)
    c = 0
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
