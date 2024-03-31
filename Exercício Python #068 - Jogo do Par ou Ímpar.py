"""Exercício Python #068 - Jogo do Par ou Ímpar"""
from random import randint
"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
VAMOS JOGAR PAR OU ÍMPAR
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Diga um valor: 6
Par ou Ímpar? [P/I] I
-----------------------------
Você jogou 6 e o computador 10. Total de 16 DEU PAR
-----------------------------
Você PERDEU!
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
GAME OVER! Você venceu 0 vezes.

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
VAMOS JOGAR PAR OU ÍMPAR
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Diga um valor: 8
Par ou Ímpar? [P/I] P
-----------------------------
Você jogou 8 e o computador 2. Total de 10 DEU PAR
-----------------------------
Você VENCEU!
Vamos jogar novamente...
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Diga um valor: 3
Par ou Ímpar? [P/I] P
-----------------------------
Você jogou 3 e o computador 2. Total de 5 DEU ÍMPAR
-----------------------------
Você PERDEU!
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
GAME OVER! Você venceu 1 vezes.
"""

exercicio = 'Exercício #068'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30 + f'\n')

d1 = 'VAMOS JOGAR PAR OU ÍMPAR'
print(f'=-' * 12 + f'\n' + f'{d1:^20}' + f'\n' + f'=-' * 12)

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
