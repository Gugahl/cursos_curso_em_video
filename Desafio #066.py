"""Exercício Python #066 - Vários números com flag"""
"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição
de parada. No final mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
"""
"""
Modo de funcionamento:
Digite um valor (999 para parar): 4
Digite um valor (999 para parar): 3
Digite um valor (999 para parar): 5
Digite um valor (999 para parar): 999
A soma dos 3 valores foi 12!
"""

desafio = 'Desafio #066'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

valor = float(input('Digite um valor (999 para parar): '))
if valor != 999:
    soma = valor
    contador = 1
    while valor != 999:
        valor = float(input('Digite um valor (999 para parar): '))
        if valor == 999:
            break
        contador += 1
        soma += valor
    print(f'A soma dos {contador} valores foi {soma}!')
