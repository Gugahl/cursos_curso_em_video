"""Desafio #044"""
"""
Elabore um programa que calcule o valor a ser pago por um
produto considerando o seu preço normal e a condição de
pagamento:

- Á vista dinheiro/cheque: 10% de desconto
- Cartão de crédito á vista: 5% de desconto
- Cartão de crédito de 2x: Preço normal
- Cartão de crédito de 3x ou mais: 20% de juros
"""

exercicio = 'Exercício #044'
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

preco_normal = float(input(f'Qual é o preço do produto? R$'))
escolha_de_pagamento = ('Escolha qual o seu meio de pagamento:\n'
                        'À vista dinheiro/cheque/PIX: 01;\n'
                        'Cartão de crédito à vista: 02;\n'
                        'Cartão de crédito duas parcelas: 03;\n'
                        'Cartão de crédito de três parcelas para cima: 04.')
print(f'{escolha_de_pagamento}')
escolha = input('Você: ')
escolha_str = str(escolha)
print(' ')

if escolha_str == '01':
    a_vista = preco_normal - (preco_normal * 0.10)
    print(f'PARABÉNS! Você ganhou um desconto de 10%! Seu produto que custava R${preco_normal:.2f}, passará a custar\n'
          f'R${a_vista:.2f}.')

elif escolha_str == '02':
    credito_a_vista = preco_normal - (preco_normal * 0.05)
    print(f'PARABÉNS! Você ganhou um desconto de 5%! Seu produto que custava R${preco_normal:.2f}, passará a custar\n'
          f'R${credito_a_vista:.2f}.')

elif escolha_str == '03':
    credito_duas_parcelas = preco_normal
    print(f'Seu produto custa R${credito_duas_parcelas:.2f}.')

elif escolha_str == '04':
    credito_tres_ou_mais_parcelas = preco_normal + (preco_normal * 0.10)
    print(f'Seu produto custa R${credito_tres_ou_mais_parcelas}.')
