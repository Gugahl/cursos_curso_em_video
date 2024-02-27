"""Desafio 006"""
"""
Crie um algorítmo que leia um número e mostre seu dobro, triplo e raíz quadrada.
"""

exercicio = 'Exercício #006'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

n = int(input('Digite um número inteiro: '))
print(f'Seu número foi: {n};\n'
      f'O dobro de {n} é: {n*2};\n'
      f'O triplo de {n} é: {n*3};\n'
      f'A raíz quadrada de {n} é: {(n**0.5):.2f}.')
