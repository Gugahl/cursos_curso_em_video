"""Desafio #048"""
"""
Faça um programa que calcule a soma entre todos os números
ímpares que são múltiplos de três e que se encontram no in-
-tervalo de 1 até 500.
"""

exercicio = ' Exercício #048 '
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

cont = 0
soma = 0
for impar in range(1-1, 500+1):
    if impar % 3 == 0:
        if impar % 2 != 0:
            soma += impar
            cont += 1

print(f'A soma de todos os {cont} valores ímpares, que são múltiplos de três e que se encontram no\n'
    f'intervalo entre 1 e 500 é igual a: {soma}.')
