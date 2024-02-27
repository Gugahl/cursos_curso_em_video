"""DESAFIO 010"""
"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere U$1.00 = R$4.91.
"""

desafio = ' DESAFIO 010 '
print(f'{desafio:=^30}')
print(' ')
print('Bom dia senhor! Bem vindo aos Estados Unidos da América.\n '
      'Meu nome é Gabriel e irei te ajudar com algumas coisas. \n '
      'Em primeiro lugar precisamos converter seu dinheiro de real para dólar, para que possa gastar aqui.')
print(' ')
real = float(input('Quantos reais você tem na carteira? R$'))
print(' ')
print(f'Ok, se você me der R${real}, com uma cotação de U$1.00 = R$4.91, eu posso te passar U${real/4.91:.2f}')
