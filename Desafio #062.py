"""Desafio #062"""
"""
Melhore o DESAFIO 061 perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerra quando ele disser
que quer mostrar 0 termos.
"""

desafio = 'Desafio #062'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

numero_inicial = int(input('Qual o número inicial dessa PA? '))
razao_da_pa = int(input('Qual a razão dessa PA? '))
contagem = 1
termo = numero_inicial
qtd_termos = 10
print(' ')

while qtd_termos != 0:
    while contagem < 11:
        print(f'{termo} --> {contagem}º termo;')
        termo += razao_da_pa
        contagem += 1
    qtd_termos = int(input('Quantos termos a mais você quer mostrar? '))
print('FIM.')
