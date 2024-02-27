"""Desafio #038"""
"""
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais 
"""

exercicio = 'Exercício #038'
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')
while True:
    primeiro_valor = float(input('Me forneça um valor numérico: '))
    segundo_valor = float(input('Me forneça outro valor numérico: '))

    if primeiro_valor > segundo_valor:
        print('O primeiro valor é maior.')

    elif segundo_valor > primeiro_valor:
        print('O segundo valor é maior.')

    else:
        print('Os dois valores são iguais.')
    break
