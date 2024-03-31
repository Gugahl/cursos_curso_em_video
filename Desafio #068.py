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

desafio = 'Desafio #068'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

d1 = 'VAMOS JOGAR PAR OU ÍMPAR'
print(f'=-' * 12 + f'\n' + f'{d1:^20}' + f'\n' + f'=-' * 12)

partidas_vencidas = partidas = 0
while True:
    valor = int(input('Diga um valor: '))
    computador = randint(1, 10)
    total = valor + computador
    par_ou_impar = ' '
    while par_ou_impar not in 'PIÍ':
        par_ou_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    partidas += 1
    print(f'-' * 52)
    print(f'Você jogou {valor} e o computador {computador}. Total de {computador+valor} DEU ', end='')
    print(f'PAR!' if total % 2 == 0 else f'ÍMPAR!')
    print(f'-' * 52)
    if par_ou_impar == 'P':
        if total % 2 == 0:
            partidas_vencidas += 1
            print(f'-' * 52 + f'\n' + f'Você VENCEU!' + f'\n' + f'Vamos jogar novamente...' + f'\n' + f'-=' * 26)
        else:
            print(f'-' * 52 + f'\n' + f'Você PERDEU!' + f'\n' + f'-=' * 26)
            break
    elif par_ou_impar in 'IÍ':
        if total % 2 == 1:
            partidas_vencidas += 1
            print(f'-' * 52 + f'\n' + f'Você VENCEU!' + f'\n' + f'Vamos jogar novamente...' + f'\n' + f'-=' * 26)
        else:
            print(f'-' * 52 + f'\n' + f'Você PERDEU!' + f'\n' + f'-=' * 26)
            break
if partidas_vencidas == 0:
    print(f'Você jogou {partidas} partida e perdeu, mais sorte na próxima vez.')
elif partidas_vencidas == 1:
    print(f'Você jogou {partidas} partidas, e venceu {partidas_vencidas} vez.')
elif partidas_vencidas > 1:
    print(f'Você jogou {partidas} partidas, e venceu {partidas_vencidas} vezes.')
