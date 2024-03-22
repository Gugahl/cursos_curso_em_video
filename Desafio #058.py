"""Desafio #058"""
from random import randint as r
"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar mostrando no final quantos palpites
foram necessários para vencer.
"""

desafio = 'Desafio #058'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

tentativas = 1
computador = r(0, 10)
usuario = int(input('Digite um valor: '))
while usuario != computador:
    tentativas += 1
    print('Você errou! Tente novamente.')
    usuario = int(input('Digite um valor: '))
print(f'Parabéns, você acertou! Precisou de {tentativas} tentativas.')
if tentativas == 1:
    print(f'Parabéns! Você acertou de {tentativas}ª!')
