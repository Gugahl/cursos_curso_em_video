"""Desafio #035"""
"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

exercicio = ' Exercício #035 '
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

text = ' Analisador de Triângulos '
print('-=' * 20)
print(f'{text:^40}')
print('-=' * 20, '\n')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
