"""Desafio #028"""
from random import choice
"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar 
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou 
perdeu.
"""

desafio = ' Desafio #028 '
print(f'{desafio:=^30}')

lista = [0, 1, 2, 3, 4, 5]
numero_sorteado = choice(lista)
msg = 'Eu sou o Gênio dos Desejos, se você adivinhar o número que estou pensando eu realizo seus maiores desejos!!'

print('-=-' * 36)
print(f'{msg:^90}')
print('-=-' * 36, '\n')

numero_escolhido = int(input('Escolha um número entre 0 e 5: '))

if numero_escolhido == numero_sorteado:
    print('Parabens!! Você conseguiu!!')

else:
    print('HAHA! EU VENCI!!!')
