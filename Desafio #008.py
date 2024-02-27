"""DESAFIO 008"""
"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e em milímetros.
"""

desafio = ' DESAFIO 008 '
print(f'{desafio:=^30}')

me = float(input('Quantos metros você mede (ex: 1.71)? '))
print(f'Ok, você mede {me} metros; \n'
      f'Convertendo em centímetros fica {me*100} centímetros; \n'
      f'Convertendo em milímetros fica {me*1000} milímetros.')
