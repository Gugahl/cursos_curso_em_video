"""Desafio #044"""
"""
Elabore um programa que calcule o valor a ser pago por um
produto considerando o seu preço normal e a condição de
pagamento:

- Á vista dinheiro/PIX: 10% de desconto
- Cartão de débito/crédito á vista: Preço normal
- Cartão de crédito de 2x até 12x: 20% de juros
"""

desafio = ' Desafio #044 '
print(f'{desafio:=^30}')
print(' ')

preco = float(input('Qual é o preço desse produto? R$'))
print(' ')
pagamento = str(input('Qual é a forma de pagamento?\n'
                      '\n'
                      'Á vista(dinheiro/PIX): 01;\n'
                      'Cartão de débito/crédito á vista: 02;\n'
                      'Cartão de crédito para 2 até 12x: 03;\n'
                      '\n'
                      'Você: '))
print(' ')

if pagamento == '01':
    avista = preco - (preco * 0.10)
    print(f'\033[32mPARABÉNS!\033[m Você conseguiu um desconto de 10% e o produto que era R${preco}\n'
          f'ficou no preço de R${avista}.')

elif pagamento == '02':
    debito_credito = preco
    print(f'O produto está no valor de R${debito_credito}.')

elif pagamento == '03':
    credito_2_12x = preco * 1.20
    print(f'O produto está no valor de R${credito_2_12x}.')