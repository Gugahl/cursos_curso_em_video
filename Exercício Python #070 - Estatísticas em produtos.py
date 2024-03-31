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

exercicio = 'Exercício #070'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30 + f'\n')

todo_dia = 'SUPERMERCADO TODO DIA'
print(f'-' * 40 + f'\n' + f'{todo_dia:^40}' + f'\n' + f'-' * 40)

total = totmil = menor = cont = 0
barato = ''
while True:
       produto = str(input('Nome do Produto: '))
       preco = float(input('Preço: R$'))
       cont += 1
       total += preco
       if preco > 1000:
              totmil += 1
       if cont == 1 or preco < menor:
              menor = preco
              barato = produto
       resp = ' '
       while resp not in 'SN':
              resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
       if resp == 'N':
              break
fim = ' FIM DO PROGRAMA '
print(f'''{fim:-^40}
O total da compra foi R${total:.2f}
Temos {total} produtos custando mais de R$1000.00
O produto mais barato foi {barato} que custa R${menor:.2f}''')
