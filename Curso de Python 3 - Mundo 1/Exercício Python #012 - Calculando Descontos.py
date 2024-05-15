"""Desafio 012"""
"""
Faça um algorítmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
"""

exercicio = 'Exercício #012'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

n = input('Qual é o nome do produto? ').title()
pi = float(input('Qual é o preço do produto? R$'))
desci = float(input('Quantos % de promoção você quer dar(0 a 100)? '))
descf = desci/100
pp = pi-(pi*descf)

print(f' ')
print(f'='*30)
print(f'{n:^30}')
print(f'='*30)
print(' ')
print(f'O preço inicial de {n} é R${pi}, na promoção Saldão {desci}% de Desconto, o produto fica por R${pp:.2f}')
