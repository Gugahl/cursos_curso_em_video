"""Exercício Python #070 - Estatísticas em produtos"""
"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
"""
"""
-----------------------------------
       SUPERMERCADO TODO DIA
-----------------------------------
Nome do Produto: Mouse
Preço: R$50
Quer continuar? [S/N] S
Nome do Produto: Caneta
Preço: R$3
Quer continuar? [S/N] S
Nome do Produto: Notebook
Preço: R$2550
Quer continuar? [S/N] S
Nome do Produto: Impressora
Preço: R$800
Quer continuar? [S/N] S
Nome do Produto: Monitor
Preço: R$1250
Quer continuar? [S/N] N
------------- FIM DO PROGRAMA ------------
O total da compra foi R$4653.00
Temos 2 produtos custando mais de R$1000,00
O produto mais barato foi Caneta que custa R$3.00
"""

desafio = 'Desafio #070'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

todo_dia = 'SUPERMERCADO TODO DIA'
print(f'-' * 40 + f'\n' + f'{todo_dia:^40}' + f'\n' + f'-' * 40)

produtos = total = produtos_caros = produto_barato = 0
nome_produto_barato = ' '
while True:
       nome = str(input('Nome do Produto: ')).strip().capitalize()
       preco = float(input('Preço: R$'))
       total += preco
       produtos += 1
       if produtos == 1 or preco < produto_barato:
              nome_produto_barato = nome
              produto_barato = preco
       if preco > 1000:
              produtos_caros += 1
       continuar = ' '
       while continuar not in 'SN':
              continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
       if continuar == 'N':
              break
print(f'Temos {produtos} produto' if produtos == 1 else f'Temos {produtos} produtos')
print(f'O total da compra foi R${total}')
if produtos_caros == 0:
       print(f'Nenhum produto custa mais de R$1000,00')
elif produtos_caros == 1:
       print(f'{produtos_caros} produto custa mais de R$1000,00')
elif produtos_caros > 1:
       print(f'{produtos_caros} produtos custam mais de R$1000,00')
print(f'O produto mais barato foi {nome_produto_barato} que custa R${produto_barato}')
