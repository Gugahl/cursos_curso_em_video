"""Desafio #058"""
from random import randint
"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar mostrando no final quantos palpites
foram necessários para vencer.
"""

exercicio = 'Exercício #058'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30 + f'\n')

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentivas. Parabens!')
