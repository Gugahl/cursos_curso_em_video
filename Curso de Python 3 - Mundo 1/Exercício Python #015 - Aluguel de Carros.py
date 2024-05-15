"""Desafio 015"""
"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por km rodado.
"""

exercicio = 'Exercício #015'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

print('='*30)
localiza = 'Portal da Localiza'
print(f'{localiza:^30}')
calculo = 'Calcule seu aluguel aqui!'
print(f'{calculo:^30}')
print('='*30)
print(' ')

nome = input('Qual é seu nome? ').title()
dias = float(input('Por quantos dias esse carro foi alugado? '))
km = float(input('Quantos quilômetros esse carro rodou? '))
valor = dias*60 + km*0.15

print(' ')
print('='*30)
msg = f'Bom dia senhor(a) {nome.strip()}!'
print(f'{msg:^30}')
print(f'Vi aqui que você alugou o carro Chevrolet Onix por R$60,00 a diária,\n'
      f'e R$0,15 o quilômetro rodado, logo o valor a pagar será de R${valor}.')
print('='*30)
