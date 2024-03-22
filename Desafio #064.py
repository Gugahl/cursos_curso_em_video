"""Desafio #064"""
"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999 que
é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag [999]).
"""

desafio = 'Desafio #064'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

numero = float(input('Digite um valor: '))
soma = numero
quantidade_de_termos = 1
while numero != 999.0:
    numero = float(input('Digite um valor: '))
    if numero != 999.0:
        soma += numero
        quantidade_de_termos += 1

print(f'Você digitou {quantidade_de_termos} números, onde a soma entre todos eles deu: {soma}.')
